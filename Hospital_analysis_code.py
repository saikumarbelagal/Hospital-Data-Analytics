"""
Hospital Data Analyzer - Mini Project
Reads hospital_data.csv, analyses patient admissions, stay, cost and satisfaction,
and saves charts and a processed file.
Requirements: pip install pandas matplotlib numpy
"""
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# 1. Load and clean
df = pd.read_csv("hospital_data.csv", parse_dates=["Admission_Date"])
print("Rows, columns:", df.shape)
print("Missing values:", int(df.isnull().sum().sum()))
df = df.drop_duplicates()

# 2. Feature engineering
df["Month"] = df["Admission_Date"].dt.to_period("M").astype(str)
df["Age_Group"] = pd.cut(df["Age"], [0, 17, 35, 50, 65, 120],
                         labels=["0-17", "18-35", "36-50", "51-65", "65+"])
df["Cost_Per_Day"] = (df["Treatment_Cost"] / df["Stay_Days"]).round(0)

# 3. Key statistics
print("\n--- Overall ---")
print(f"Total patients: {len(df)}")
print(f"Average stay: {df['Stay_Days'].mean():.1f} days")
print(f"Average cost: Rs {df['Treatment_Cost'].mean():,.0f}")
print(f"Total revenue: Rs {df['Treatment_Cost'].sum():,.0f}")
print(f"Average satisfaction: {df['Satisfaction_Rating'].mean():.2f} / 5")
readm_rate = (df["Readmitted"] == "Yes").mean() * 100
print(f"Readmission rate: {readm_rate:.1f}%")

dept = df.groupby("Department").agg(Patients=("Patient_ID", "count"),
                                    Avg_Stay=("Stay_Days", "mean"),
                                    Avg_Cost=("Treatment_Cost", "mean"),
                                    Avg_Rating=("Satisfaction_Rating", "mean")).round(1)
print("\n--- Department-wise ---")
print(dept.sort_values("Patients", ascending=False))

print("\n--- Busiest doctors (top 5) ---")
print(df["Doctor"].value_counts().head(5))

print("\n--- Admission type ---")
print(df["Admission_Type"].value_counts())

corr_stay_cost = df["Stay_Days"].corr(df["Treatment_Cost"])
corr_stay_rating = df["Stay_Days"].corr(df["Satisfaction_Rating"])
print(f"\nCorrelation (Stay vs Cost): {corr_stay_cost:.2f}")
print(f"Correlation (Stay vs Satisfaction): {corr_stay_rating:.2f}")

# 4. Charts
order = dept.sort_values("Patients", ascending=False)
plt.figure(figsize=(8, 5))
b = plt.bar(order.index, order["Patients"], color="steelblue")
plt.bar_label(b)
plt.title("Patients by Department"); plt.ylabel("Number of Patients")
plt.xticks(rotation=30, ha="right"); plt.tight_layout()
plt.savefig("patients_by_department.png", dpi=150); plt.close()

monthly = df.groupby("Month").size()
plt.figure(figsize=(8, 5))
plt.plot(monthly.index, monthly.values, marker="o", color="teal")
plt.title("Monthly Admissions Trend"); plt.ylabel("Admissions")
plt.xticks(rotation=45); plt.grid(alpha=0.3); plt.tight_layout()
plt.savefig("monthly_admissions.png", dpi=150); plt.close()

plt.figure(figsize=(8, 5))
b = plt.bar(order.index, dept.loc[order.index, "Avg_Cost"], color="darkorange")
plt.title("Average Treatment Cost by Department"); plt.ylabel("Cost (Rs)")
plt.xticks(rotation=30, ha="right"); plt.tight_layout()
plt.savefig("avg_cost_by_department.png", dpi=150); plt.close()

plt.figure(figsize=(7, 5))
plt.scatter(df["Stay_Days"], df["Treatment_Cost"], alpha=0.6, color="purple")
m, c = np.polyfit(df["Stay_Days"], df["Treatment_Cost"], 1)
xs = np.sort(df["Stay_Days"].unique())
plt.plot(xs, m * xs + c, color="red", label="Trend line")
plt.xlabel("Stay (days)"); plt.ylabel("Treatment Cost (Rs)")
plt.title("Length of Stay vs Treatment Cost"); plt.legend(); plt.grid(alpha=0.3)
plt.tight_layout(); plt.savefig("stay_vs_cost.png", dpi=150); plt.close()

ag = df["Age_Group"].value_counts().reindex(["0-17", "18-35", "36-50", "51-65", "65+"])
plt.figure(figsize=(6, 5))
plt.pie(ag, labels=ag.index, autopct="%1.0f%%", startangle=90)
plt.title("Patients by Age Group"); plt.tight_layout()
plt.savefig("age_group_distribution.png", dpi=150); plt.close()

# 5. Save processed output
df.to_csv("processed_hospital_data.csv", index=False)
print("\nSaved: 5 charts + processed_hospital_data.csv")
