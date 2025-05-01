import openai

openai.api_key = "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"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # or "gpt-4" if you have access
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": input("Enter a prompt: ")}
    ]
)

print(response.choices[0].message["content"])