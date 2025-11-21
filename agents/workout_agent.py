import asyncio

DEFAULT_EXERCISES = {
    "beginner": {
        "strength": ["Bodyweight Squats", "Incline Push-ups (knees)", "Bent-over Dumbbell Rows (light)"],
        "cardio": ["Jumping Jacks", "High Knees", "March in Place"],
        "core": ["Plank 30s", "Bicycle Crunches", "Leg Raises"],
        "mobility": ["Dynamic Stretching - 10 min"]
    },
    "intermediate": {
        "strength": ["Goblet Squats", "Push-ups", "Dumbbell Rows"],
        "cardio": ["Burpees", "Sprints 30s", "Jump Rope"],
        "core": ["Plank 60s", "Hanging Leg Raises", "Russian Twists"],
        "mobility": ["Yoga Flow - 15 min"]
    }
}

class WorkoutAgent:
    def __init__(self):
        pass

    async def generate_workout_plan(self, user_profile: dict):
        level = user_profile.get("fitness_level", "beginner")
        minutes = int(user_profile.get("minutes_per_day", 30))
        goal = user_profile.get("goal", "maintain")

        level_key = "intermediate" if level in ("intermediate","advanced") else "beginner"
        exercises = DEFAULT_EXERCISES.get(level_key, DEFAULT_EXERCISES["beginner"])

        week = []
        for day in range(1, 8):
            if day % 6 == 0:
                plan_type = "mobility"
            elif day % 3 == 0:
                plan_type = "core"
            elif day % 2 == 0:
                plan_type = "cardio"
            else:
                plan_type = "strength"
            day_ex = exercises.get(plan_type, [])
            plan = {
                "day": day,
                "type": plan_type,
                "duration_min": minutes,
                "exercises": day_ex
            }
            week.append(plan)

        await asyncio.sleep(0)
        return {"week": week, "summary": f"{level_key} {goal} plan, {minutes} min/day"}
