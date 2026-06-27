import ollama
import re

SYSTEM_PROMPT = """
You are an expert claim extractor and classifier.

You will receive the FULL transcript of a video.

Your tasks are:

1. Extract ONLY meaningful claims.
2. Ignore greetings.
3. Ignore filler words.
4. Ignore incomplete sentences.
5. Ignore "Like and Subscribe".
6. Split long paragraphs into separate claims.
7. Every extracted claim must be complete and understandable on its own.
8. Classify every extracted claim.

Allowed categories:

FACT
PERSONAL
OPINION
QUESTION

Definitions:

FACT
A statement that can be verified using reliable evidence.

PERSONAL
A statement about someone's personal feelings, intentions or experiences.

OPINION
A subjective belief or judgment.

QUESTION
Any sentence asking for information.

Return ONLY valid JSON.

Example:

[
    {
        "sentence": "India has 28 states.",
        "category": "FACT"
    },
    {
        "sentence": "Calculus is used to calculate the area under a curve.",
        "category": "FACT"
    },
    {
        "sentence": "Pizza is the best food.",
        "category": "OPINION"
    }
]

Return ONLY JSON.
"""


def classify(transcript):

    response = ollama.chat(
        model="gemma3:4b",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": transcript
            }
        ]
    )

    content = response["message"]["content"].strip()

    # Remove markdown fences
    content = content.replace("```json", "")
    content = content.replace("```", "")

    # Remove thinking blocks
    content = re.sub(
        r"<think>.*?</think>",
        "",
        content,
        flags=re.DOTALL
    ).strip()

    # Keep only JSON
    start = content.find("[")
    end = content.rfind("]")

    if start != -1 and end != -1:
        content = content[start:end + 1]

    return content