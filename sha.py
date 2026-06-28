# import pandas as pd

# df = pd.read_csv("cleaned_jobs.csv")
# print(df.shape)

# import pandas as pd

# df = pd.read_csv("cleaned_jobs.csv")

# print(df.shape)
# print(df.columns.tolist())


# import pandas as pd

# df = pd.read_csv("cleaned_jobs_mysql.csv")

# df = df.iloc[:100]   # fakt 100 rows

# df.to_csv(
#     "test100.csv",
#     index=False,
#     encoding="utf-8-sig"
# )

# print("Done")




# import pandas as pd

# df = pd.read_csv("cleaned_jobs_mysql.csv")

# df.to_csv(
#     "jobs_utf8.csv",
#     index=False,
#     sep=",",
#     encoding="utf-8"
# )

# print("Done")   




# import pandas as pd
# import csv

# df = pd.read_csv("cleaned_jobs.csv")

# df.to_csv(
#     "jobs_mysql_final.csv",
#     index=False,
#     encoding="utf-8-sig",
#     quoting=csv.QUOTE_ALL
# )

# print("jobs_mysql_final.csv created")



# import pandas as pd

# df = pd.read_csv("cleaned_jobs_mysql.csv")

# print(df.shape)

# # Missing values fill kara
# df = df.fillna("")

# # Save fresh CSV
# df.to_csv(
#     "jobs_mysql_fixed.csv",
#     index=False,
#     encoding="utf-8-sig"
# )

# print("Saved jobs_mysql_fixed.csv")


# import pandas as pd

# df = pd.read_csv("cleaned_jobs_mysql.csv")

# print(df.iloc[1511])

import pandas as pd

df = pd.read_csv("jobs_mysql_fixed.csv")

df.drop(columns=["Job Description"], inplace=True)

df.to_csv("jobs_sql.csv", index=False, encoding="utf-8-sig")

print(df.shape)