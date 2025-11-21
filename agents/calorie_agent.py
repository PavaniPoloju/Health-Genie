import asyncio

ACTIVITY_MULTIPLIERS = {
    "low": 1.2,
    "sedentary": 1.2,
    "light": 1.375,
    "moderate": 1.55,
    "high": 1.725,
    "very_high": 1.9
}

class CalorieAgent:
    def __init__(self):
        pass

    async def compute_calories(self, user_profile: dict):
        """
        Compute BMR (Mifflin–St Jeor) and target calories based on goal.
        Returns dict with bmr, maintenance, target and macro targets.
        """
        weight = float(user_profile.get("weight_kg", 70))
        height = float(user_profile.get("height_cm", 170))
        age = int(user_profile.get("age", 30))
        sex = user_profile.get("sex", "male").lower()
        activity = user_profile.get("activity_level", "moderate").lower()
        goal = user_profile.get("goal", "maintain").lower()

        # BMR
        if sex.startswith("m"):
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        else:
            bmr = 10 * weight + 6.25 * height - 5 * age - 161

        multiplier = ACTIVITY_MULTIPLIERS.get(activity, ACTIVITY_MULTIPLIERS["moderate"])
        maintenance = bmr * multiplier

        if goal == "lose":
            target = maintenance - 500
        elif goal == "gain":
            target = maintenance + 300
        else:
            target = maintenance

        # Macros: protein 1.6 g/kg, fat 25% calories, rest carbs
        protein_g = round(1.6 * weight)
        fat_cal = 0.25 * target
        fat_g = round(fat_cal / 9)
        protein_cal = protein_g * 4
        carbs_cal = target - (protein_cal + fat_cal)
        carbs_g = round(carbs_cal / 4) if carbs_cal > 0 else 0

        await asyncio.sleep(0)  # keep async-friendly
        return {
            "bmr": int(round(bmr)),
            "maintenance": int(round(maintenance)),
            "target": int(round(target)),
            "macros": {
                "calories": int(round(target)),
                "protein_g": int(protein_g),
                "fat_g": int(fat_g),
                "carbs_g": int(carbs_g)
            }
        }
