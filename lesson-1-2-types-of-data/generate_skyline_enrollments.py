# generate_skyline_enrollments.py
# Lesson 1.2: Types of Data and Where to Find It
# Author: [A. Chris Yi]
# Date: [09/15/2026]
#
# Generates a synthetic dataset of 100 fictional Skyline University students
# illustrating the four scales of measurement (nominal, ordinal, interval,
# ratio). Saves the result as skyline_enrollments.csv.

import random
import numpy as np
import pandas as pd

random.seed(123)
np.random.seed(123)

n_students = 100

# enrollment_id (nominal scale: categorical with no order)
enrollment_ids = [f"ENR-{random.randint(000000, 999999)}" for _ in range(n_students)]

# course_name (nominal scale: categorical with no order)
course_names = np.random.choice(
    ["Intro to Analytics", "Python for Beginners", "SQL Basics", "Tableau Fundamentals", "Statistics 101"],
    size=n_students,
)

# enrollment_year (interval scale: ordered with equal gaps, no true zero)
enrollment_years = np.random.randint(2022, 2026, size=n_students)

# final_grade (ordinal scale: ordered categories with unequal gaps)
final_grades = np.random.choice(
    ["A", "B", "C", "D", "F"],
    size=n_students,
    p=[0.20, 0.35, 0.25, 0.15, 0.05]
)

# hours_studied (ratio scale: ordered, equal gaps, true zero)
hours_studied = np.random.normal(loc=30, scale=15, size=n_students)
hours_studied = np.maximum(hours_studied, 0)  # Ensure non-negative values

# completion_status (nominal scale: categorical with no order)
completion_status = np.random.choice(
    ["Completed", "In Progress", "Dropped"],
    size=n_students,
    p=[0.70, 0.20, 0.10]
)

skyline_enrollments = pd.DataFrame({
    "enrollment_id": enrollment_ids,
    "course_name": course_names,
    "enrollment_year": enrollment_years,
    "final_grade": final_grades,
    "hours_studied": hours_studied,
    "completion_status": completion_status,
})

print(skyline_enrollments.head(10))
print(f"\nShape: {skyline_enrollments.shape}")
print(f"\nColumn types:\n{skyline_enrollments.dtypes}")

output_path = "skyline_enrollments.csv"
skyline_enrollments.to_csv(output_path, index=False)
print(f"\nDataset saved to {output_path}")
