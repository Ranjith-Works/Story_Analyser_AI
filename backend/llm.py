import os

from dotenv import load_dotenv
from openai import OpenAI

from backend.prompts import CHAT_PROMPT, CHARACTER_LIST_PROMPT

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


def generate_response(prompt):

    response = client.chat.completions.create(
        model="nvidia/nemotron-3-ultra-550b-a55b:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


def ask_llm(context, question):

    prompt = CHAT_PROMPT.format(
        context=context,
        question=question
    )

    return generate_response(prompt)


def extract_characters(story):

    prompt = CHARACTER_LIST_PROMPT.format(
        context=story[:12000]
    )

    response = generate_response(prompt)

    characters = []

    for line in response.split("\n"):

        line = line.strip()

        if line:
            characters.append(line)

    return sorted(list(set(characters)))