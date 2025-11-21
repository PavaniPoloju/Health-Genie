import asyncio
from tools.recipe_utils import estimate_calories_simple, format_meal

MEAL_TEMPLATES = {
    "vegetarian": [
        ("Oatmeal with berries", ["oats", "berries", "milk"]),
        ("Chickpea salad", ["chickpeas", "lettuce", "olive oil"]),
        ("Tofu stir-fry", ["tofu", "mixed veg", "soy sauce"]),
        ("Lentil soup", ["lentils", "tomatoes", "spices"]),
        ("Veggie wrap", ["tortilla", "mixed veg", "hummus"])
    ],
    "omnivore": [
        ("Oatmeal with milk & nuts", ["oats", "milk", "nuts"]),
        ("Chicken salad", ["chicken", "lettuce", "olive oil"]),
        ("Grilled salmon & veg", ["salmon", "veg", "lemon"]),
        ("Beef stir-fry", ["beef", "peppers", "soy sauce"]),
        ("Yogurt & fruit", ["yogurt", "fruit", "honey"])
    ]
}

class MealAgent:
    def __init__(self):
        pass

    async def generate_meal_plan(self, user_profile: dict, days=7):
        prefs = user_profile.get("dietary_preferences", [])
        diet_key = "vegetarian" if any("vegetarian" in p for p in prefs) or any("no_pork" in p for p in prefs) else "omnivore"
        templates = MEAL_TEMPLATES.get(diet_key, MEAL_TEMPLATES["omnivore"])

        plan = {"days": []}
        for d in range(1, days+1):
            breakfast_t = templates[(d-1) % len(templates)][0]
            lunch_t = templates[(d) % len(templates)][0]
            dinner_t = templates[(d+1) % len(templates)][0]
            breakfast_cal = estimate_calories_simple([breakfast_t])
            lunch_cal = estimate_calories_simple([lunch_t])
            dinner_cal = estimate_calories_simple([dinner_t])
            day_meals = [
                format_meal(d, "breakfast", breakfast_t, breakfast_cal),
                format_meal(d, "lunch", lunch_t, lunch_cal),
                format_meal(d, "dinner", dinner_t, dinner_cal)
            ]
            plan["days"].append({"day": d, "meals": day_meals})
        await asyncio.sleep(0)
        return plan
