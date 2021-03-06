#!/usr/local/bin/bash

# Date: 2022-01-21
# Author: Gustav Collin Rasmussen
# Purpose: BASH workflow that inserts data in database.

# python3 src/CRUD/insert.py --datatype real --dates 2022-07-21  # 2022-03-02,2022-03-03  # --workout_number 2
# echo 'data inserted in database. Preparing figures ..'
python3 src/model/plot_model.py --datatype real --pgm gvt
# open img/real_fitted_data_squat_gvt.png
# open img/real_fitted_data_barbell_bench_press_gvt.png
# open img/real_fitted_data_squat_splines.png
# open img/real_fitted_data_deadlift_splines.png
# open img/real_fitted_data_seated_row_splines.png
# open img/real_fitted_data_barbell_bench_press_splines.png
