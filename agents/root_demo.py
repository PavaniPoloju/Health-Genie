import asyncio
import json
import os
import sys
from agents.meal_agent import MealAgent
from agents.workout_agent import WorkoutAgent
from agents.calorie_agent import CalorieAgent
from agents.progress_agent import ProgressAgent
from agents.action_agent import ActionAgent

async def run_demo(user_profile):
    meal_agent = MealAgent()
    workout_agent = WorkoutAgent()
    calorie_agent = CalorieAgent()
    progress_agent = ProgressAgent()
    action_agent = ActionAgent()

    tasks = [
        meal_agent.generate_meal_plan(user_profile, days=7),
        workout_agent.generate_workout_plan(user_profile),
        calorie_agent.compute_calories(user_profile)
    ]
    meal_plan, workout_plan, calorie_plan = await asyncio.gather(*tasks)

    progress_agent.save_run(user_profile.get("id","anon"), meal_plan, workout_plan, calorie_plan)

    pretty_json, structured = action_agent.compile_deliverable(user_profile, meal_plan, workout_plan, calorie_plan)
    print("\n=== FINAL DELIVERABLE (JSON) ===\n")
    print(pretty_json)

    return structured

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join("sample_inputs", "sample_user.json")
    with open(path, "r") as f:
        user_profile = json.load(f)
    asyncio.run(run_demo(user_profile))
