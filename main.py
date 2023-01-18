import openai
import api_key

openai.api_key = api_key.API_KEY

response = openai.Completion.create(engine="text-curie-001",
                                    prompt="What is the capital of Germany?",
                                    max_tokens=10,
                                    temperature=0.1)

print(response)
