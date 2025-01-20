recipes = [
    {"name": "Pancakes", "ingredients": ["flour", "milk", "egg"], "type": "Breakfast"},
    {"name": "Omelette", "ingredients": ["egg", "onion", "tomato"], "type": "Breakfast"},
    {"name": "Chicken Curry", "ingredients": ["chicken", "onion", "spices"], "type": "Lunch"},
    {"name": "Salad", "ingredients": ["lettuce", "tomato", "cucumber"], "type": "Dinner"},
]

def menu():
    while True:
        print("\n--- Recipe Finder Menu ---")
        print("1. Search Recipes by Ingredients")
        print("2. Filter Recipes by Type")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            search_recipes()
        elif choice == "2":
            filter_recipes()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def search_recipes():
    search_query = input("Enter ingredients (comma-separated): ").lower().split(",")
    search_query = [ingredient.strip() for ingredient in search_query]
    
    matching_recipes = []
    for recipe in recipes:
        if all(ingredient in [i.lower() for i in recipe["ingredients"]] for ingredient in search_query):
            matching_recipes.append(recipe)
   
    if matching_recipes:
        print("\nMatching Recipes:")
        for recipe in matching_recipes:
            print(f"- {recipe['name']} ({recipe['type']})")
    else:
        print("\nNo recipes found with the given ingredients.")

def filter_recipes():
    recipe_types = {recipe["type"] for recipe in recipes}
    print("\nAvailable Recipe Types:")
    for r_type in recipe_types:
        print(f"- {r_type}")

    selected_type = input("Enter the recipe type you want to filter by: ").strip()
    if selected_type.lower() not in [t.lower() for t in recipe_types]:
        print(f"Invalid type '{selected_type}'. Please choose a valid type.")
        return

    matching_recipes = [recipe for recipe in recipes if recipe["type"].lower() == selected_type.lower()]
    
    if matching_recipes:
        print("\nRecipes of selected type:")
        for recipe in matching_recipes:
            print(f"- {recipe['name']}")
    else:
        print(f"\nNo recipes found for type '{selected_type}'.")

menu()
