import openai

def generate_gpt_response(user_message):
    prompt = f"User: {user_message}\nAI Developer:"
    message = [
        {"role": "system", "content": "You are a friendly AI Developer"},
        {"role": "user", "content": prompt}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=message,
        temperature=0.2,
        max_tokens=4000,
        frequency_penalty=0.9
    )

    gpt_message = response.choices[0].message.content
    return gpt_message