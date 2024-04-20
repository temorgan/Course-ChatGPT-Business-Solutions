import azure.functions as func
import os
import openai
import json
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="completionAPI", methods=["POST"])
def completionAPI(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Ensure OPENAI_API_KEY is set
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    if OPENAI_API_KEY is None:
        raise ValueError("The OPENAI_API_KEY environment variable is not set.")
    openai.api_key = OPENAI_API_KEY

    prompt = "Who was Count Dante."

    # Prepare the request body with default values
    request_body = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    # Read the JSON from the HTTP request if present
    try:
        data = req.get_json()
        request_body.update(data)  # Allow overriding the prompt or other fields
    except ValueError:
        logging.info("No JSON body sent with request or unable to parse JSON.")

    # Call the OpenAI API
    try:
        response = openai.chat.completion.create(**request_body)
        # Serialize the OpenAI API response to JSON string
        response_json = json.dumps(response)
        return func.HttpResponse(body=response_json, mimetype="application/json", status_code=200)
    except Exception as e:
        logging.error(f"Failed to call OpenAI API: {e}")
        return func.HttpResponse("Failed to process the request", status_code=500)
