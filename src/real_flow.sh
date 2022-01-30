#!/usr/local/bin/bash

# Date: 2022-01-21
# Author: Gustav Collin Rasmussen
# Purpose: BASH workflow that inserts data in database.

python3 src/CRUD/insert.py real 2022-01-30
echo 'data inserted in database. Preparing figures ..'
python3 src/model/plot_model.py real
# open img/real_fitted_data_squat.png
# open img/real_fitted_data_deadlift.png
open img/real_fitted_data_seated_row.png
# open img/real_fitted_data_barbell_bench_press.png
