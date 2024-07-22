
from groq import Groq
key = "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"
client = Groq(
    api_key=key
    # api_key="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",
)




def take_action(data, system_prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": data,
            },
        ],
        model="llama3-70b-8192",
    )
    return chat_completion.choices[0].message.content
