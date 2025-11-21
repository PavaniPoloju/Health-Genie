import json

class ActionAgent:
    def __init__(self):
        pass

    def compile_deliverable(self, user_profile, meal_plan, workout_plan, calorie_plan):
        obj = {
            "user": {
                "id": user_profile.get("id"),
                "name": user_profile.get("name"),
                "goal": user_profile.get("goal"),
                "fitness_level": user_profile.get("fitness_level")
            },
            "calorie_plan": calorie_plan,
            "workout_plan": workout_plan,
            "meal_plan": meal_plan
        }
        return json.dumps(obj, indent=2), obj
