import azure.functions as func
import os
import openai
import json
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="completionAPI", methods=["POST", "GET"])  # Allow both POST and GET for simplicity
def completionAPI(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request for completionAPI.')

    # ... [your existing code for setting up OPENAI_API_KEY] ...

    # Initialize prompt with a default value or use the user's input
    default_prompt = "Who was Deborah Sampson."
    user_prompt = req.params.get('prompt', default_prompt)

    if req.method == 'GET' and user_prompt == default_prompt:
        # If it's a GET request and the user didn't provide a prompt, ask for it
        return func.HttpResponse("Please enter a search request", status_code=200)

    # Ensure OPENAI_API_KEY is set
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    if not OPENAI_API_KEY:
        logging.error("The OPENAI_API_KEY environment variable is not set.")
        return func.HttpResponse("Server error: OPENAI_API_KEY not set", status_code=500)

    openai.api_key = OPENAI_API_KEY

    # Initialize prompt with a default value
    prompt = "Who was Deborah Sampson"

    try:
        data = req.get_json()
        prompt = data.get('prompt', prompt)  # Override default prompt if provided
    except ValueError:
        logging.error("Received request without a valid JSON body.")
        return func.HttpResponse("Invalid JSON data. Please send a valid JSON with a 'prompt' key.", status_code=400)
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return func.HttpResponse("Error processing your request", status_code=500)

    # Prepare the request body for OpenAI API
    request_body = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 200,
        "temperature": 0.5
    }

    logging.info("Request body: %s", json.dumps(request_body, indent=2))

    try:
        response = openai.chat.completions.create(**request_body)
        # The response object now contains the completion directly
        message_content = response.choices[0].message.content
        response_json = json.dumps({"content": message_content})
        return func.HttpResponse(response_json, mimetype="application/json", status_code=200)
    except Exception as e:
        logging.error(f"Error calling OpenAI API: {str(e)}")
        return func.HttpResponse("Error processing your request with OpenAI", status_code=500)

@app.route(route="basicazurefunction")
def basicazurefunction(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request for basicazurefunction.')

    name = req.params.get('name', None)
    if not name:
        try:
            req_body = req.get_json()
            name = req_body.get('name')
        except ValueError:
            pass

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )

# Additional routes and functions can be added here following the same pattern.
