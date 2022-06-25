# Fitness-Tracker

Full stack fitness tracking application using TinyDB and FastAPI.
Add weight-training logs continuously to db.json and query the data through the browser.
Visually inspect your progression through dates and exercises

[![Documentation Status](https://readthedocs.org/projects/fitness-tracker/badge/?version=latest)](https://fitness-tracker.readthedocs.io/en/latest/?badge=latest)

![fitness-tracker-wf](https://github.com/TheNewThinkTank/Fitness-Tracker/actions/workflows/fitness-tracker-wf.yml/badge.svg)

![simulation-wf](https://github.com/TheNewThinkTank/Fitness-Tracker/actions/workflows/simulation-wf.yml/badge.svg)

Below: key exercises for overall strength indications.<br>
Each figure displays workout-date vs 1-rep-max estimate for different training programs,<br>
together with their regression fits/trendlines using 68% confidence intervals.<br>
Each program is shown in the legend)

|            ![fitted_data_deadlift](img/real_fitted_data_deadlift_splines.png)            |      ![fitted_data_squat](img/real_fitted_data_squat_splines.png)      |
| :--------------------------------------------------------------------------------------: | :--------------------------------------------------------------------: |
| ![fitted_data_barbell_bench_press](img/real_fitted_data_barbell_bench_press_splines.png) | ![fitted_data_seated_row](img/real_fitted_data_seated_row_splines.png) |

<!-- Below: comparison between first leg workout of program 1
and last leg workout of program 2 for three selected exercises.<br>

| ![first_leg_workout_pgm1](img/workout_2021-12-11.png) | ![last_leg_workout_pgm2](img/workout_2022-05-28.png) |
| :---------------------------------------------------: | :--------------------------------------------------: | -->

## Features

- Program logging (Located in folder: logs)
- Plotting (with the Seaborn library. Located in folder: img)
- Documentation (auto-generated by Sphinx and hosted on readthedocs: https://fitness-tracker.readthedocs.io/en/latest/index.html# )
- Multiple unit test suites (Pytest)
- BDD (Behavior Driven Development, using the Behave framework)
- Multiple GitHub Actions workflows
- Data quality validation (Great Expections)
- Package dependency management (Poetry)
- KPI tracking: 1-Rep-Max estimation (Epley and Brzycki formulas)
- Realistic workout data simulation (with naturally progressing trend over time)
- Catalogue of musclegroups, corresponding exercises and suggested weight ranges (for simulations)

<!-- ## Upcoming features
- Add muscle groups to log file name
- ML models (Scikit Learn)
- YAML-support
- Bodily strength-ratio tracking (determine baseline, ideal-ranges, and compare the two)
- Dashboard
- Add key exercises (benchpress, squat, deadlift) to dashboard
- Hosting on PyPi (automated deploy with GitHub Actions)
- Identify musclegroups and exercises with best or worst progression
- Add cardio tracking (integrate app with Strava) -->
