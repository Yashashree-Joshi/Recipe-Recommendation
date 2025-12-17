import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"


def generate_recipe_from_keywords(ingredients, preferences):
    """
    ingredients: list of ingredient strings
    preferences: list of taste preference strings
    returns: generated recipe text
    """

    print("\n🍳 Cooking your recipe... please wait ⏳\n")

    ingredient_text = ", ".join(ingredients)

    preference_text = ""
    if preferences:
        preference_text = f"\nTaste preferences: {', '.join(preferences)}"

    prompt = f"""
Create an eggless sweet recipe using ONLY the following ingredients:
{ingredient_text}
{preference_text}

Rules:
- Do NOT introduce new ingredients
- Keep the recipe simple and quick
- Use common household cooking methods

Provide:
- Recipe name
- Ingredients list
- Step-by-step instructions
"""

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=120)
    response.raise_for_status()

    data = response.json()
    return data["response"]
