# 🏏 Cricket Score Predictor

A beginner-friendly Python project that estimates the final score of a cricket innings using the current run rate and a wicket-based scoring adjustment. When a team is chasing, it also calculates the required run rate needed to reach the target.

## 📌 About

This project takes the current match situation as input and provides basic scoring predictions.

The program considers:

* Current score
* Overs completed
* Wickets lost
* Total overs
* Whether the team is chasing
* Target score when chasing

It calculates the current run rate, predicted final score, and a wicket-adjusted scoring rate. For a chasing team, it additionally calculates the required run rate.

## 🧮 How It Works

### 1. Current Run Rate

The current run rate is calculated using:

`Current Run Rate = Current Runs / Overs Completed`

For example:

`85 / 10 = 8.5 runs per over`

### 2. Predicted Final Score

The current run rate is projected across the remaining overs:

`Predicted Score = Current Runs + (Current Run Rate × Overs Remaining)`

### 3. Wicket-Adjusted Scoring Rate

The program applies a simple heuristic based on wickets lost:

| Wickets Lost | Adjustment |
| ------------ | ---------- |
| 0–2          | +5%        |
| 3–5          | -5%        |
| 6–8          | -20%       |
| 9+           | -40%       |

The adjustment is intended to represent the assumption that scoring ability changes as wickets are lost.

These percentages are **heuristic assumptions for this educational project** and are not derived from historical cricket data.

### 4. Required Run Rate

The required run rate is calculated only when the team is chasing.

`Required Run Rate = Runs Needed / Overs Remaining`

Where:

`Runs Needed = Target Score - Current Score`

For example:

```text
Target Score:       180
Current Score:       85
Overs Remaining:     10

Runs Needed:         95
Required Run Rate:   9.5
```

## 💻 Example 1 — Team Chasing

```text
Team is chasing: yes
Current score: 85
Overs completed: 10
Wickets lost: 2
Total overs: 20
Target: 180

Current run-rate: 8.5
Predicted score: 170.0
Wicket-adjusted scoring rate: 8.925
Required run-rate: 9.5
```

The required run rate is higher than the current run rate, meaning the team needs to increase its scoring rate to reach the target.

## 💻 Example 2 — Team Batting First

```text
Team is chasing: no
Current score: 85
Overs completed: 10
Wickets lost: 5
Total overs: 20

Current run-rate: 8.5
Predicted score: 170.0
Wicket-adjusted scoring rate: 8.075
No required run-rate for team batting first
```

A required run rate is not calculated because the team is setting the target.

## 🛠️ Technologies Used

* Python

## 📚 Python Concepts Practiced

This project was created to practice:

* Variables
* User input
* Type conversion
* Arithmetic operations
* Functions
* `if / elif / else`
* Boolean expressions
* Conditional execution
* Basic mathematical modelling

## 🚀 Future Improvements

Possible future versions:

* [ ] Improve input validation
* [ ] Add exception handling
* [ ] Use wicket-adjusted scoring rate in the final score prediction
* [ ] Add ball-by-ball scoring
* [ ] Handle overs and balls separately
* [ ] Add powerplay, middle-over and death-over adjustments
* [ ] Compare projected score with the target
* [ ] Add historical cricket match data
* [ ] Build a data-driven prediction model
* [ ] Explore machine learning for score prediction
* [ ] Add a graphical user interface

## ⚠️ Disclaimer

This is an educational project and uses a simple mathematical heuristic. The predictions are not intended to represent accurate real-world cricket forecasting.

The wicket-adjustment percentages are assumptions made for learning purposes and are not statistically validated.

## 👤 Project Status

**Version:** 1.0

This project will be improved gradually as new Python and data-analysis concepts are learned.
