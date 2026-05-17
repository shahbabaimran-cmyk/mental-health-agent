from groq import Groq 
from dotenv import load_dotenv
import os

load_dotenv(os.path.join(os.path.dirname(__file__), "..", "venv", "secret.env"))

api_key=os.getenv("groq_api")

client = Groq(api_key=api_key)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": "Hello, how are you?"}
    ]
)

print(response.choices[0].message.content) 