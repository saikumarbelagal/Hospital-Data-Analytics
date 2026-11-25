# Hospital Data Analyzer - Mini Project

A Python data analytics project that analyses 300 hospital patient records:
admissions by department, length of stay, treatment cost, doctor workload,
patient satisfaction and readmission rate.

## Files
- `hospital_data_analysis.py` - main Python source code
- `hospital_data.csv` - sample dataset (fictional)
- `processed_hospital_data.csv` - output with Month, Age_Group and Cost_Per_Day added
- `Hospital_Data_Analytics_Report.pdf` - project report
- `patients_by_department.png` - patients per department
- `monthly_admissions.png` - monthly admissions trend
- `avg_cost_by_department.png` - average treatment cost per department
- `stay_vs_cost.png` - length of stay vs cost scatter plot
- `age_group_distribution.png` - patients by age group

## What the project does
1. Loads and cleans the dataset (missing values, duplicates)
2. Creates Month, Age_Group and Cost_Per_Day columns
3. Calculates overall statistics: average stay, cost, revenue, satisfaction, readmission rate
4. Compares departments and finds the busiest doctors
5. Checks correlation of stay with cost and with satisfaction
6. Generates five charts and saves the processed data

## Requirements
```
pip install pandas matplotlib numpy
```

## Run
Keep the CSV and Python file in the same folder, then run:
```
python hospital_data_analysis.py
```

## Key findings
- General Medicine has the most patients (66 of 300); Emergency is second
- Cardiology, Orthopedics and Neurology have the highest average treatment cost
- Longer stays mean higher cost (correlation about 0.57)
- Average satisfaction is about 3.98 / 5 and readmission rate is 6.0%

The dataset is fictional and created for academic demonstration.
