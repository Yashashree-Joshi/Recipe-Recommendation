from ollama_engine import generate_recipe_from_keywords
from keyword_processor import process_keywords
from google_search import search_recipes


def get_ingredients():
    raw = input("\nEnter ingredients (comma-separated, min 5): ").strip()

    if raw.lower() == "bye":
        return None

    ingredients, preferences, unknowns = process_keywords(raw)
    return ingredients, preferences, unknowns


def main():
    print("🍽️ Welcome to the Recipe Assistant!")
    print("Type 'bye' anytime to exit.\n")

    while True:
        print("\nChoose an option:")
        print("1. Generate recipe using AI")
        print("2. Search recipe using Google")

        choice = input("Enter choice (1/2): ").strip().lower()

        if choice == "1":
            mode = "generate"
        elif choice == "2":
            mode = "search"
        elif choice == "bye":
            print("👋 Goodbye! Happy cooking!")
            break
        else:
            print("⚠️ Invalid choice.")
            continue

        result = get_ingredients()

        if result is None:
            print("👋 Goodbye! Happy cooking!")
            break

        ingredients, preferences, unknowns = result

        if len(ingredients) < 5:
            print("❌ Please enter at least 5 ingredients.")
            continue

        # 🔍 PREVIEW
        print("\n🧺 Detected ingredients:")
        print(", ".join(ingredients))

        if preferences:
            print("\n🌶️ Taste preferences:")
            print(", ".join(preferences))

        if unknowns:
            print("\n⚠️ Warning: Some inputs may be unclear:")
            print(", ".join(unknowns))

        #  GOOGLE SEARCH MODE
        if mode == "search":
            print("\n🔎 Searching recipes on Google...\n")
            results = search_recipes(ingredients)

            if not results:
                print("❌ No recipes found.")
                continue

            for i, item in enumerate(results, start=1):
                print(f"{i}. {item.get('title')}")
                print(f"   🔗 {item.get('link')}")
                print(f"   {item.get('snippet', '')}\n")

            continue  # skip AI generation

     
        recipe = generate_recipe_from_keywords(ingredients, preferences)
        print("\n" + recipe)

        exit_choice = input("\nType 'bye' to exit or press Enter to continue: ").strip().lower()
        if exit_choice == "bye":
            print("👋 Goodbye! Happy cooking!")
            break


if __name__ == "__main__":
    main()
