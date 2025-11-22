# HealthGenie — AI Fitness & Meal Coach (Local Demo)

**A Multi-Agent Architecture for Automated Fitness & Nutrition Planning**
**1. Problem Statement**
In today’s world, people want personalized fitness plans but often struggle with:
1. Not knowing how many calories they should consume
2. Not knowing what workouts fit their level
3. Not knowing what meals match their preferences
4. Getting overwhelmed by information
5. Wanting simple, daily recommendations without manual effort

Traditional fitness apps offer static, one-size-fits-all plans. They rarely adapt to a person’s:
- Height, weight, age
- Diet type
- Activity leve
- Restrictions (ex: no sugar)
- Fitness goal (lose/gain/maintain)
So creating a **fully automated, dynamic, AI-driven system** that generates:
1. Personalized calorie breakdown
2. 7-day workout plan
3. 7-day meal plan
4. Final structured output (JSON)

**2. Why Agents?**
Why use multiple agents instead of one big model?
Because this problem has different expert domains:
| Task                | Needs Expertise In                             |
| ------------------- | ---------------------------------------------- |
| Calorie calculation | Physiology, BMR formulas, activity multipliers |
| Workout planning    | Exercise science, fitness levels               |
| Meal planning       | Nutrition, diet types, calories                |
| Final coaching      | Summarization, reasoning                       |

A single agent would mix all logic and become messy.
Instead, we design modular agents:
1. Each agent does one job well.
2. Each agent can be improved or replaced independently.
3. They communicate like a team.
This is the core idea of a multi-agent architecture.

**3. What I Created — System Architecture**
**Multi-Agent Workflow (Diagram)**
                ┌────────────────────────────┐
                │      User Profile Agent     │
                │ Extracts goals & constraints│
                └──────────────┬─────────────┘
                               │
        ┌──────────────────────┼──────────────────────────┐
        │                      │                          │
┌──────────────┐     ┌────────────────────┐     ┌───────────────────┐
│ Workout Agent│     │ Meal Plan Agent    │     │ Calorie Agent     │
│ Personalized │     │ Nutrition planning │     │ Calorie math &    │
│ exercises    │     │ & recipes          │     │ deficit tracking  │
└──────────────┘     └────────────────────┘     └───────────────────┘
        │                      │                          │
        └──────────────────────┬──────────────────────────┘
                               │
                ┌────────────────────────────┐
                │        Coach Agent          │
                │ Final plan + guidance       │
                └────────────────────────────┘

**Final Output**
Delivered in **structured JSON**, easy for web apps, dashboards, or mobile apps.

**4. Demo Output** 
Here is the final JSON generated for:
1. **Name:** Jungkook
2. **Goal:** Maintenance
3. **Diet:** Non-veg, no sugar
4. **Height:** 177 cm
5. **Weight:** 71 kg
6. **Age:** 28
7. **Activity Level:** Medium

**5. The Build – Tools & Technologies Used**
1. **Python 3.9**
Core programming language.
2. **Multi-Agent Architecture**
Each module independently performs a specific function.
3. **No external APIs required**
The system works offline, using pure logic.
4. **JSON-based input/output**
**Name:** Jungkook
**Goal:** Maintenance
**Diet:** Non-veg, no sugar
**Height:** 177 cm
**Weight:** 71 kg
**Age:** 28
**Activity Level:** Medium

**5. The Build – Tools & Technologies Used**
->**Python 3.9**
Core programming language.
->**Multi-Agent Architecture**
Each module independently performs a specific function.
->**No external APIs required**
The system works offline, using pure logic.
->**JSON-based input/output**
For compatibility with:
- Kaggle Notebooks
- GitHub projects
- Web dashboards
- REST APIs

**How Everything Works Internally**
1️.User Profile Agent
Parses the user JSON input and extracts:
->Age, height, weight
->Diet type
->Goal (lose/gain/maintain)
->Restrictions
->Activity level

2️.Calorie Agent
Uses:
1. Mifflin-St Jeor BMR Formula
2. Activity multiplier
3. Goal adjustment
Example (your output):
1. BMR: 1681
2. Maintenance: 2606
3. Macros:
    1.Protein: 114 g
    2.Fat: 72 g
   Carbs: 375 g

3️.Workout Agent
Creates a 7-day plan with:
-Strength days
-Cardio days
-Core days
-Mobility day
Simplified but functional.

4️.Meal Agent
Creates 7 days × 3 meals:
-Oatmeal
-Chicken salad
-Salmon
-Yogurt + fruit
-Beef stir-fry
**Calories currently**: 100 per meal (placeholder values).

5️.Coach Agent
Merges everything into one **final JSON**.

**6. Demo Explanation**
returns:
-Calorie breakdown
-Workout plan
-Meal plan
-Final merged JSON
This proves the **multi-agent pipeline** works end-to-end.

**7. If I Had More Time… (Future Improvements)**
1. Connect real nutrition APIs
2. Smarter workout generator
3. Add a progress Agent
4. Add Gemini/OpenAI LLM for Meal creativity
5. Deploy as a Web App
6. Add a Recommendation Engine

**8. Conclusion**
HealthGenie successfully demonstrates:

1. A complete multi-agent system
2. Personalized AI-generated fitness & nutrition plans
3. Clean JSON output
4. Fully offline capability
5. Modular, expandable architecture

This project is ideal for:
Kaggle AI/ML competitions
->University capstone submissions
->GitHub portfolio
->AI engineering practice
