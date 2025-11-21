import json
import os
import time

MEM_DB = "progress_db.json"

class ProgressAgent:
    def __init__(self, db_path=MEM_DB):
        self.db_path = db_path
        if not os.path.exists(self.db_path):
            with open(self.db_path, "w") as f:
                json.dump({}, f)

    def save_run(self, user_id, meal_plan, workout_plan, calorie_plan):
        with open(self.db_path, "r") as f:
            try:
                data = json.load(f)
            except Exception:
                data = {}
        data.setdefault(str(user_id), [])
        data[str(user_id)].append({
            "timestamp": int(time.time()),
            "meal_plan": meal_plan,
            "workout_plan": workout_plan,
            "calorie_plan": calorie_plan
        })
        with open(self.db_path, "w") as f:
            json.dump(data, f, indent=2)
        return True

    def get_history(self, user_id):
        with open(self.db_path, "r") as f:
            try:
                data = json.load(f)
            except Exception:
                return []
        return data.get(str(user_id), [])
