import math

def estimate_calories_simple(ingredients):
    """
    Simple placeholder calorie estimator:
    assumes each ingredient contributes ~100 kcal.
    Replace with a real API or DB lookup for production.
    """
    try:
        count = len(ingredients)
    except Exception:
        count = 1
    return 100 * max(1, count)

def format_meal(day, meal_name, recipe, calories, protein_g=None, carbs_g=None, fat_g=None):
    return {
        "day": day,
        "meal": meal_name,
        "recipe": recipe,
        "calories": calories,
        "protein_g": protein_g,
        "carbs_g": carbs_g,
        "fat_g": fat_g
    }
