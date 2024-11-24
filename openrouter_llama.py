import os
from openai import OpenAI

# Retrieve the API key from the environment variable
api_key = os.getenv('OPENROUTER_API_KEY')

if not api_key:
    raise ValueError("The OPENROUTER_API_KEY environment variable is not set.")

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=api_key,
)

completion = client.chat.completions.create(
  # extra_headers={
  #   "HTTP-Referer": $YOUR_SITE_URL, // Optional, for including your app on openrouter.ai rankings.
  #   "X-Title": $YOUR_APP_NAME, // Optional. Shows in rankings on openrouter.ai.
  # },
  model="meta-llama/llama-3.1-70b-instruct:free",
  messages=[
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]
)

print(completion.choices[0].message.content)