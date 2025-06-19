# AI Fitness Coach

## Overview

This project demonstrates using AI and prompt engineering to create a fitness coach that analyzes health metrics and provides personalized guidance on fitness focus areas and exercise recommendations.

Since this is a demonstration, it relies on a CSV file containing health data rather than reading from a health application, but could be modified to read health data from suitable sources.

## Data Format

### CSV File Schema
```csv
Date,Weight(KG),Height(CM),BodyFat(%),SubCFat(%),VisFat(%),SkeletalMuscle(%),MetabolicAge(%),RealAge(Y)
```

### Example Entries
```csv
13-06-2025,105,186,31.9,27.9,13,44,49,41
20-06-2025,100,186,30.1,23.9,15,44,48,41
```

## Prerequisites

### AI API Key
This project uses Claude by [Anthropic](https://console.anthropic.com/dashboard).

To get an API key:
1. Log into your Claude dashboard using the link above
2. Click **Get API Key**
3. Copy the generated key for use in setup

## Setup Instructions

### Local Environment Setup
*These instructions assume you are working on Windows.*

**Required Software:**
- [Python 3.7+](https://www.python.org/) - Programming language runtime
- [VSCode](https://code.visualstudio.com/) - Recommended editor (or your preferred code editor)

### Installation Steps

1. **Download the project files** and store them locally. Extract if zipped.

2. **Open a command prompt** and navigate to the project folder:
   ```bash
   cd path\to\ai-fitness-coach
   ```

3. **Create a virtual environment:**
   ```bash
   python -m venv .\venv
   ```

4. **Activate the virtual environment:**
   ```bash
   .\venv\Scripts\activate
   ```

5. **Install required modules:**
   ```bash
   pip install -r requirements.txt
   ```

6. **Configure your API key:**
   
   > **Security Note**: In production environments, API keys should be stored in environment variables or secure vaults, not hardcoded in scripts.
   
   In `health_agent.py`, modify the `api_key` parameter:
   ```python
   client = Anthropic(
       api_key="your-actual-api-key-here",
   )
   ```

7. **Update health data:**
   
   Update `files\stats.csv` with your health statistics or use the provided example data.

## Usage

Run the application from the command line:

```bash
python app.py
```

## Output

The script generates two types of output:

### 1. Console Feedback

The AI coach provides detailed analysis directly in the console:

```
Changes since last check-in:
- Weight decreased by 5kg (105kg to 100kg) in one week
- Body fat decreased by 1.8% (31.9% to 30.1%)
- Subcutaneous fat decreased significantly by 4% (27.9% to 23.9%)
- Visceral fat increased by 2% (13% to 15%)
- Skeletal muscle percentage remained stable at 44%
- Metabolic age improved slightly from 49 to 48 years

Health summary:
The client is a 41-year-old individual with significant health risks. BMI is approximately 28.9 
(down from 30.3), indicating overweight status. Body fat percentage (30.1%) is well above healthy 
range for males. Visceral fat level is concerning and trending upward. Skeletal muscle percentage 
is a positive indicator at 44%.

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
```

### 2. Workout Plan File

A personalized workout plan is generated and saved to `./files/workout.txt`:

```
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
```

## Project Structure

```
ai-fitness-coach/
├── app.py                 # Main application file
├── health_agent.py        # AI agent logic
├── requirements.txt       # Python dependencies
├── files/
│   ├── stats.csv         # Health statistics data
│   └── workout.txt       # Generated workout plans
└── README.md             # This file
```

## Technical Features

- **AI Integration**: Uses Anthropic's Claude API for intelligent health analysis
- **Prompt Engineering**: Structured prompts for consistent, actionable output
- **Data Processing**: CSV parsing and analysis using pandas
- **File I/O**: Reads health data and writes workout plans
- **Error Handling**: Robust exception handling for API and file operations

## Future Enhancements

- Integration with fitness tracking APIs (Fitbit, Apple Health, etc.)
- Web interface for easier data input and visualization
- Historical trend analysis and progress tracking
- Meal planning recommendations based on nutritional goals
- Integration with calendar apps for workout scheduling

## Dependencies

See `requirements.txt` for a complete list of Python package dependencies.

## Security Considerations

- API keys should be stored as environment variables in production
- Health data should be encrypted when stored
- Consider implementing user authentication for multi-user scenarios

---

*This project demonstrates practical AI application in health and fitness, showcasing API integration, prompt engineering, and data analysis capabilities.*