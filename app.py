from openai import OpenAI
import os
import json


client = OpenAI(api_key="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")

def llm_classify_review(text: str) -> dict:
    prompt = f"""
    Classify this customer feedback about Tonik Bank.

    Feedback:
    {text}

    Return valid JSON with:
    - sentiment: positive, neutral, or negative
    - themes: array of short theme labels
    - urgent: true or false
    - rationale: short explanation
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    content = response.output_text
    return json.loads(content)