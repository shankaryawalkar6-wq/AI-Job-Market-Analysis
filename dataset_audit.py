import pandas as pd

df = pd.read_csv(r"C:\Users\shank\Downloads\archive\DataAnalyst.csv")

# Basic Info
print("Shape:", df.shape)

# Remove Unnamed column
if "Unnamed: 0" in df.columns:
    df.drop("Unnamed: 0", axis=1, inplace=True)

# Remove rows with missing Company Name
df.dropna(subset=["Company Name"], inplace=True)

# Company Name Cleaning
df["Company Name"] = (
    df["Company Name"]
    .str.split("\n")
    .str[0]
)

print("\nCleaned Company Names:")
print(df["Company Name"].head(10))



# Duplicate rows
print("\nDuplicate Rows:", df.duplicated().sum())

# Dataset Info
print("\nDataset Info:")
print(df.info())

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Salary Sample
print("\nSalary Sample:")
print(df["Salary Estimate"].sample(20).tolist())

# Company Name Sample
print("\nCompany Name Sample:")
print(df["Company Name"].head(20).tolist())

# Company Age Feature Engineering
df["Company Age"] = df["Founded"].apply(
    lambda x: 2026 - x if x > 0 else None
)

print("\nCompany Age Sample:")
print(df[["Founded", "Company Age"]].head())

# Skill Extraction
skills = [
    "SQL",
    "Python",
    "Excel",
    "Power BI",
    "Tableau",
    "Pandas",
    "NumPy",
    "Machine Learning",
    "Statistics",
    "AWS",
    "Azure"
]

def extract_skills(text):
    found = []

    for skill in skills:
        if skill.lower() in str(text).lower():
            found.append(skill)

    return found

df["Skills Found"] = df["Job Description"].apply(extract_skills)

print("\nSkills Found Sample:")
print(
    df[
        [
            "Job Title",
            "Skills Found"
        ]
    ].head(10)
)

# Salary Columns Check
# print("\nSalary Columns Sample:")

# print(
#     df[
#         [
#             "Salary Estimate",
#             "Min Salary",
#             "Max Salary",
#             "Avg Salary"
#         ]
#     ].head()
# )

# # Clean Company Name
# df["Company Name"] = (
#     df["Company Name"]
#     .str.split("\n")
#     .str[0]
# )

# print("\nCleaned Company Names:")
# print(df["Company Name"].head(10))

# # Save Cleaned Dataset
# df.to_csv(
#     "cleaned_jobs.csv",
#     index=False
# )

# print("\nCleaned dataset saved as cleaned_jobs.csv")

df["Salary Estimate"] = (
    df["Salary Estimate"]
    .str.replace(r"\(.*\)", "", regex=True)
    .str.replace("$", "", regex=False)
    .str.replace("K", "", regex=False)
)

salary_range = df["Salary Estimate"].str.split("-", expand=True)

df["Min Salary"] = pd.to_numeric(salary_range[0], errors="coerce")
df["Max Salary"] = pd.to_numeric(salary_range[1], errors="coerce")

df["Avg Salary"] = (
    df["Min Salary"] + df["Max Salary"]
) / 2


print(
    df[
        [
            "Salary Estimate",
            "Min Salary",
            "Max Salary",
            "Avg Salary"
        ]
    ].head()
)


df.to_csv(
    r"C:\Users\shank\OneDrive\Desktop\project\cleaned_jobs.csv",
    index=False
)

print("Cleaned dataset saved successfully!")


df.drop(columns=["Skills Found"], inplace=True)

df.to_csv(
    "cleaned_jobs_mysql.csv",
    index=False,
    encoding="utf-8-sig"
)

print("File saved successfully")