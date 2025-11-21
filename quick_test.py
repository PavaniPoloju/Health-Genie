import asyncio
import json
import sys
from agents.root_demo import run_demo

async def test_run():
    try:
        user = json.load(open("sample_inputs/sample_user.json"))
    except Exception as e:
        print("Could not open sample_inputs/sample_user.json:", e)
        sys.exit(1)

    print("Running HealthGenie quick test...")
    out = await run_demo(user)
    # Basic assertions
    assert "calorie_plan" in out, "Missing calorie_plan in output"
    assert "meal_plan" in out, "Missing meal_plan in output"
    assert "workout_plan" in out, "Missing workout_plan in output"
    print("\nQuick test passed: meal_plan, workout_plan and calorie_plan present.")

if __name__ == "__main__":
    asyncio.run(test_run())
