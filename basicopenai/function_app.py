import azure.functions as func
import os
import openai
import json
import logging

app = func.FunctionApp()

@app.route(route="/basicopenai", methods=["GET", "POST"], auth_level=func.AuthLevel.ANONYMOUS)
def basicopenai(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

# Ensure OPENAI_API_KEY is set
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_API_KEY is None:
    raise ValueError("The OPENAI_API_KEY environment variable is not set.")
openai.api_key = OPENAI_API_KEY

prompt = "Explain the song 'Pale Shelter' by Tears for Fears."

# Prepare the request body with default values
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
print("Request body:", json.dumps(request_body, indent=2))

# Call the OpenAI API
response = openai.chat.completions.create(**request_body)
      
# Extract and format the response
response_message = response.choices[0].message.content

# Log the response message before the function returns a response
print("Response message:", response_message)