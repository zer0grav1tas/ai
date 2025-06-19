# AI Fitness Coach

## Overview
This project is a demonstration of using an AI and good prompt engineering to create a fitness coach that will critique your fitness levels and provide guidance on what to focus on, and what exercises you should be doing.

Since this is a demonstration, it relies on a csv file containing health data rather than reading from a health application but could be modified to read health data from suitbale sources.

**CSV File Schema**
Date,Weight(KG),Height(CM),BodyFat(%),SubCFat(%),VisFat(%),SkeletalMuscle(%),MetabolicAge(%),RealAge(Y)

**Example Entries**
13-06-2025,105,186,31.9,27.9,13,44,49,41
20-06-2025,100,186,30.1,23.9,15,44,48,41

**AI API Keys**
The AI being used is Claude by [Anthropic](https://console.anthropic.com/dashboard)

Before you can follow this guide you need to get an API key. Log into you Claude dashboard using the link above and click **Get API Key**.

## Running the Coach

**Setting up your local environment**
These intructions assume you are working on Windows.

- This project uses Python which you can install from [python.org](https://www.python.org/)
- I use VSCode as an editor but others will suffice [vscode](https://code.visualstudio.com/)

Once you have installed Python and an editor follow the below steps to run the project

1. Download the projects file and store them locally. Expand them if they are zipped up.
2. Open a command prompt and navigate to the project folder.
3. Create a virtual environment to run in

    python -m venv .\venv

4. Activate the virtual environment.

    .\venv\scripts\activate

5. Install modules

    pip install -r requirements.txt

6. Add your API key to the script. This should not be done in a production environment and is placed in the script for demonstration purposes. The API key should ideally be stored in a vault or local environment variables.

In health_agent.py modify the api_key="" to include your API Key

client = Anthropic(
    api_key="sdfghjklwertyuiopcvbnm123445678",
)

7. Update the files\stats.csv with the stats or use the example ones.

** Running **
Type the below command into the console:

    python app.py

## Output
Once the script has run 2 things will happen:

**Feedback from the coach will show in the console.**

Example:

Changes since last check-in:
- Weight decreased by 5kg (105kg to 100kg) in one week
- Body fat decreased by 1.8% (31.9% to 30.1%)
- Subcutaneous fat decreased significantly by 4% (27.9% to 23.9%)
- Visceral fat increased by 2% (13% to 15%)
- Skeletal muscle percentage remained stable at 44%
- Metabolic age improved slightly from 49 to 48 years

Health summary:
The client is a 41-year-old individual with significant health risks. BMI is approximately 28.9 (down from 30.3), indicating overweight status. Body fat percentage (30.1%) is well above healthy range for males. Visceral fat level is concerning and trending upward. Skeletal muscle percentage is a positive indicator at 44%.

Primary concerns:
1. High overall body fat percentage (>30%)
2. Increasing visceral fat (particularly concerning as it rose despite weight loss)
3. Metabolic age 7-8 years higher than actual age
4. Rate of weight loss (5kg in one week) may be too aggressive

Focus points:
1. Moderate weight loss pace to 0.5-1kg per week through balanced nutrition and regular exercise
2. Incorporate regular cardiovascular exercise (30-45 minutes, 4-5 times weekly) to address visceral fat
3. Maintain strength training to preserve skeletal muscle mass during weight loss
4. Consider consultation with healthcare provider regarding rapid weight fluctuation and visceral fat increase

**A new workout plan will be output to ./files/workout.txt.**

Based on the client's data showing high body fat (31.9% dropping to 30.1%) and high visceral fat (13-15%), while having good skeletal muscle mass (44%), I'll recommend a program focusing on fat loss while maintaining muscle mass.

<answer>
Workout 1: Full Body Resistance Training
- Compound exercises: Squats, Deadlifts, Bench Press, Rows, Shoulder Press
- Core work: Planks, Russian Twists
- 3 sets of 12-15 reps per exercise
- Days: Monday, Thursday

Workout 2: High-Intensity Interval Training (HIIT)
- 30 seconds work, 30 seconds rest
- Exercises: Burpees, Mountain Climbers, Jump Rope, High Knees, Box Steps
- Total duration: 25 minutes
- Days: Tuesday, Friday

Recommended Daily Calorie Intake: 2,300 calories
- Protein: 180g (30%)
- Carbs: 230g (40%)
- Fats: 77g (30%)
- Focus on whole foods, lean proteins, and plenty of vegetables
</answer>