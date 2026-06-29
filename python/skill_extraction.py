import pandas as pd
import re

# Load Dataset
df = pd.read_csv(r"C:\Users\shank\OneDrive\Desktop\project\cleaned_jobs.csv")

# Check Columns
print(df.columns)

# Skills List
skills = [
    "SQL",
    "Python",
    "Excel",
    "Power BI",
    "Tableau",
    "AWS",
    "Azure",
    "Snowflake",
    "Spark",
    "Hadoop",
    "Machine Learning",
    "Deep Learning",
    "Statistics",

    "SAS",
    "Looker",
    "BigQuery",
    "TensorFlow",
    "PyTorch",
    "Pandas",
    "NumPy",
    "Git",
    "Docker",
    "Kafka",
    "ETL",
    "Data Warehouse",
    "Oracle",
    "SQL Server",
    "MySQL",
    "PostgreSQL"
]

# Skill Extraction Function
def extract_skills(job_description):

    found_skills = []

    text = str(job_description).lower()

    for skill in skills:

        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text):
            found_skills.append(skill)

    return found_skills


# Create New Column
df["AI Skills"] = df["Job Description"].apply(extract_skills)

# Display Output
print("\nAI Skills Sample:\n")
print(df[["Job Title", "AI Skills"]].head(10))

# Save New Dataset
df.to_csv(
    r"C:\Users\shank\OneDrive\Desktop\project\jobs_ai.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nAI dataset saved successfully!")


from collections import Counter

all_skills = []

for skill_list in df["AI Skills"]:
    all_skills.extend(skill_list)

skill_counts = Counter(all_skills)

print("\nTop 20 Skills:\n")

for skill, count in skill_counts.most_common(20):
    print(f"{skill}: {count}")


    from collections import Counter

all_skills = []

for skill_list in df["AI Skills"]:
    all_skills.extend(skill_list)

skill_counts = Counter(all_skills)

skills_df = pd.DataFrame(
    skill_counts.items(),
    columns=["Skill", "Job Count"]
)

skills_df = skills_df.sort_values(
    by="Job Count",
    ascending=False
)

skills_df.to_csv(
    r"C:\Users\shank\OneDrive\Desktop\project\skills_frequency.csv",
    index=False
)

print("\nskills_frequency.csv saved successfully!")