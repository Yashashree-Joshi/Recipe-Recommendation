import re

# Common spelling / formatting fixes
CORRECTIONS = {
    "coco powder": "cocoa powder",
    "applepie": "apple pie",
    "choco powder": "cocoa powder",
    "tomatoe": "tomato",
    "chilli": "chili"
}
TASTE_PREFERENCES = {
    "sweet",
    "spicy",
    "tangy",
    "salty",
    "sour"
}


def normalize_keyword(keyword: str) -> str:
    """
    Lowercase, trim spaces, remove extra spaces
    """
    keyword = keyword.lower().strip()
    keyword = re.sub(r"\s+", " ", keyword)
    return keyword

def looks_like_gibberish(word: str) -> bool:
    vowels = set("aeiou")

    # Rule 1: no vowels
    if not any(char in vowels for char in word):
        return True

    # Rule 2: too many consonants in a row
    consonant_streak = 0
    for char in word:
        if char not in vowels:
            consonant_streak += 1
            if consonant_streak >= 4:
                return True
        else:
            consonant_streak = 0

    # Rule 3: suspiciously long single word
    if len(word) > 12:
        return True

    return False


def process_keywords(raw_input: str):
    """
    Splits user input into:
    - ingredients (real items)
    - preferences (taste words)
    - unknowns (unrecognized words)

    Returns:
        ingredients, preferences, unknowns
    """

    parts = raw_input.split(",")

    ingredients = []
    preferences = []
    unknowns = []

    for part in parts:
        kw = normalize_keyword(part)

        if not kw:
            continue

        # Apply correction first
        kw = CORRECTIONS.get(kw, kw)

        # Classify
        if kw in TASTE_PREFERENCES:
            preferences.append(kw)
        else:
            if looks_like_gibberish(kw):
                unknowns.append(kw)
                ingredients.append(kw)  # still allow it
            else:
                ingredients.append(kw)


    # Deduplicate while preserving order
    def dedupe(items):
        seen = set()
        result = []
        for item in items:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result

    return dedupe(ingredients), dedupe(preferences), dedupe(unknowns)
