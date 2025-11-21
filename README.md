# HealthGenie — AI Fitness & Meal Coach (Local Demo)

## Quick start (local, Python 3.9)
1. Clone or create the repository folder `HealthGenie/`.
2. Create and activate a Python virtualenv:
   - Windows:
     ```
     python -m venv venv
     venv\Scripts\activate
     ```
   - macOS / Linux:
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```
3. Install dependencies:
pip install -r requirements.txt
4. (Optional) Create `.env` in project root and update values.
5. Run quick test:
python quick_test.py
6. Run demo (prints full JSON deliverable):
python agents/root_demo.py sample_inputs/sample_user.json


