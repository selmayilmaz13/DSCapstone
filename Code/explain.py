import os
from openai import OpenAI


def build_explanation_prompt(result: dict) -> str:
    return f"""
You are helping explain an automation-risk prediction for a career insights app.

Here is the structured result for one occupation:

Occupation: {result["occupation_title"]}
Predicted automation probability: {result["predicted_automation_probability"]:.4f}
Employment in 2024: {result["employment_2024"]}
Employment in 2034: {result["employment_2034"]}
Employment change (numeric): {result["employment_change_numeric_2024_34"]}
Employment change (percent): {result["employment_change_percent_2024_34"]}

Write a short explanation for a general user.

Requirements:
- Keep it to 3-5 sentences.
- Explain what the automation probability suggests in plain English.
- Mention the 10-year employment outlook.
- Do not invent numbers.
- Do not mention model names or technical details.
- Be balanced: automation risk does not always mean the whole job disappears.

Return only the explanation text.
""".strip()


def generate_explanation(result: dict, client: OpenAI) -> str:
    prompt = build_explanation_prompt(result)

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text.strip()


if __name__ == "__main__":
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set in your environment.")

    client = OpenAI(api_key=api_key)

    sample_result = {
        "occupation_title": "Data scientists",
        "predicted_automation_probability": 0.3353,
        "employment_2024": 245.9,
        "employment_2034": 328.3,
        "employment_change_numeric_2024_34": 82.5,
        "employment_change_percent_2024_34": 33.5,
    }

    explanation = generate_explanation(sample_result, client)

    print("\nExplanation:\n")
    print(explanation)