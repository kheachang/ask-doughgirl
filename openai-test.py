from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  response_format={"type": "json+object"},
  messages=[  # array of message objects
    # system role: sets behavior
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    # provides request
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(response.choices[0].message.content)
