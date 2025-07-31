# Lacrosse Team Match & Player Performance Analysis

## Dataset Overview
This project analyzes Syracuse Women’s Lacrosse 2025 team performance using two CSV files:
- `syracuse_lacrosse_2025_cleaned.csv`: Match-level statistics (score, opponent, date, result).
- `syracuse_lacrosse_2025_player_stats.csv`: Player performance statistics (goals, assists, games played, etc.).

## Key Questions
This analysis focuses on team outcomes and individual contributions by answering:
1. How many games were played?
2. What is the team’s win-loss record?
3. Who was the top goal scorer?
4. Which player had the highest points-per-game?
5. What was the closest game?
6. Which game had the most goals scored?
7. Who was the most consistent scorer?
8. Who led in assists?
9. How many games were narrow losses (≤3 goals)?
10. What was the biggest win margin?

## LLM Interaction
Large Language Model (LLM) prompts were used to simulate querying the dataset using natural language.  
The Python results were compared with LLM-generated answers for evaluation and improvement.  
This creates a framework for AI-driven exploratory sports analysis.

## Tools & Technologies
- Python 3.10
- Pandas (data analysis)
- Jupyter Notebook / .py script
- OpenAI LLM for QA simulation
- CSV files for structured data input

## Interesting Insights
- The team played 17 games and won 12.
- Emma Muchnick was the top scorer with 34 goals.
- Emma Ward led assists with 46 and had the highest points/game.
- Olivia Adamson had a 3.33 goals/game ratio (highest efficiency).
- The closest game was a 1-point win against Maryland.
- The biggest victory was a 16-goal margin vs. Harvard.

## How to Run

### 1. Ensure you have Python and required packages installed:
```bash
pip install pandas
```



### 3. Run the script:
```bash
python llm.py
```

The script will output 10 summarized insights to your terminal.
