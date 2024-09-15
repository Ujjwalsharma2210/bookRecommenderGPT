import openai
import httpx

openai.api_key = ""

client = openai.OpenAI()

completion = client.chat.completions.create(
                model = "gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "HELLO"},
                    {"role": "user", "content": "SAY ANYTHINg"}
                ],
                
            )

print(completion.choices[0].message.content)
