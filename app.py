from ollama import chat

response = chat(
    model='gemma2:2b',
    messages=[
        {'role': 'user', 'content': 'Hello from my app!'}
    ]
)

print(response.message.content)