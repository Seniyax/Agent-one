from dotenv import load_dotenv
import os
from openai import OpenAI
from crewai import LLM


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
        model="gpt-4o-mini",  # or gpt-4o / gpt-3.5-turbo
        messages=[
            {"role": "system", "content": "You are a friendly assistant."},
            {"role": "user", "content": "Say hello and tell me the current year."}
        ],
        max_tokens=50
    )

print(response.choices[0].message.content)