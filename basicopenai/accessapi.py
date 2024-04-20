import azure.functions as func
import os
import openai
import json
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="openai", methods=["GET", "POST"])  # Ensure methods are specified if needed
def completionAPI(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Ensure OPENAI_API_KEY is set
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    if OPENAI_API_KEY is None:
        logging.error("The OPENAI_API_KEY environment variable is not set.")
        return func.HttpResponse(
            "Server error: OPENAI_API_KEY not set", status_code=500
        )
    
    openai.api_key = OPENAI_API_KEY

    # Prepare the request body with default values
    try:
        # Attempt to read the JSON payload for dynamic prompts
        data = req.get_json()
        prompt = data.get('prompt', "Explain the song 'Pale Shelter' by Tears for Fears.")
    except ValueError:
        # Use a default prompt if JSON is invalid or not provided
        prompt = "Explain the song 'Pale Shelter' by Tears for Fears."

    request_body = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 200,  # Default value
        "temperature": 0.5  # Default value
    }

    # Log the entire request body in a readable JSON format for better debugging
    logging.info("Request body: %s", json.dumps(request_body, indent=2))

    try:
        # Call the OpenAI API
        response = openai.ChatCompletion.create(**request_body)
        
        # Extract and format the response
        response_message = response.choices[0].message.content

        # Log the response message before the function returns a response
        logging.info("Response message: %s", response_message)
        return func.HttpResponse(response_message, status_code=200)
    except Exception as e:
        logging.error(f"Error calling OpenAI: {str(e)}")
        return func.HttpResponse("Error processing your request", status_code=500)
