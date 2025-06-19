from anthropic import Anthropic
import pandas as pd

client = Anthropic(
    api_key="", # Replace with your actual API key
)

whoistheassistant = "You are a health and fitness analyst tasked with reviewing a client's health statistics and providing recommendations."

def generate_workout(stats, workout):
    msg = f"""
    {whoistheassistant} 
    
    You will be given the client's dataset showing their health statistics {stats} over time. Your task is to analyze this information and provide a concise, professional report.
    Examine the dataset of health statistics. Each line represents the same person at different check-ins, each line is date stamped in format DD-MM-YYYY:

    You will provide a two week workout plan {workout} aligned to the client current state and objectives, you will only adjust the workout plan if needed.
    You will provide a recommended calorie intake during the 2 week period before the next review.

    Provide your complete response within <answer> tags, structured as follows:

    <answer>
    Workout 1: Description
    Workout 1: Reps and sets, or time
    Workout 1: Days of week e.g. days 1, 3, 5
    Workout 2: Description
    Workout 2: Reps and sets, or time
    Workout 2: Days of week e.g. days 1, 3, 5
    </answer>

    if there is no change to the workout respond in the <answer> tags with:
    
    <answer>
    NOCHANGE
    </answer>
    """
    
    response = client.messages.create(
        max_tokens=1024,
        model="claude-3-5-sonnet-latest",
        system=whoistheassistant,
        messages=[
            {
                "role": "user",
                "content": msg
            }
        ],
    )

    return response.content[0].text

def assess_health(stats):
    msg = f"""

    {whoistheassistant} 
    
    You will be given the clients health statistics {stats} over time. Your task is to analyze this information and provide a concise, professional report.
    Examine the dataset of health statistics. Each line represents the same person at different check-ins, each line is date stamped in format DD-MM-YYYY:

    <dataset>
    {stats}
    </dataset>

    Analyze the data and prepare a report with the following components:

    1. Brief comparison of changes since the last check-in (if there is one)
    2. Summary of overall health
    3. Primary concerns
    4. Next 2 week focus points

    When analyzing the data:
    - Pay particular attention to trends in body fat percentage, BMI, and other key health indicators.
    - Consider the rate of change between check-ins.
    - Identify any metrics that are outside of healthy ranges.

    When making recommendations:
    - Be specific and actionable in your advice.
    - If there are serious health concerns, don't hesitate to recommend medical intervention.

    Present your analysis and recommendations in a clear, concise manner. Use professional language and avoid unnecessary elaboration. 

    Provide your complete response within <answer> tags, structured as follows:

    <answer>
    Changes since last check-in:
    [Your analysis here]

    Health summary:
    [Your summary here]

    Primary concerns:
    [List concerns here]

    Focus points:
    [List focus points here]

    </answer>
    """
    response = client.messages.create(
        max_tokens=1024,
        model="claude-3-5-sonnet-latest",
        system=whoistheassistant,
        messages=[
            {
                "role": "user",
                "content": msg
            }
        ],
    )

    print(response.content[0].text)

stats_file = "./files/stats.csv"
workout_file = "./files/workout.txt"

try:
    stats = pd.read_csv(stats_file)
    assess_health(stats)
except Exception as e:
    print(f"Error reading CSV: {e}")

try:
    stats = pd.read_csv(stats_file)
    with open(workout_file) as f:
        current_workout = f.read()
    new_workout = generate_workout(stats, current_workout)
except Exception as e:
    print(f"Error reading workout: {e}")

if "NOCHANGE" in new_workout:
    print("Workout plan unchanged")
else:
    with open(workout_file, "w") as f:
        f.write(new_workout)
    print("Workout plan updated!")  
    print(new_workout)  