from google import genai
from dotenv import load_dotenv
import os
load_dotenv()
GEMINI_API_KEY = os.getenv("api_key2")

client = genai.Client(api_key=GEMINI_API_KEY)

if GEMINI_API_KEY:
    print("API Key loaded successfully.")
# Use api_key in your application
else:
    print("Error: GEMINI_API_KEY not found in environment.")

stream = client.interactions.create(
model="gemini-3.1-flash-lite",
input="Count from 1 to 25.",
stream=True,

)
for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="", flush=True)