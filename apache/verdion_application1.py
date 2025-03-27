from multiprocessing.reduction import duplicate

import pandas as pd
from fuzzywuzzy import fuzz

df = pd.read_csv("veridion_entity_resolution_challenge.csv")
cols = ['company_name', 'company_legal_names', 'website_domain', "main_city", "main_country_code"]

# Removing duplicates
df = df[cols].drop_duplicates()

# filling nans and convert to string
df["company_name"] = df['company_name'].fillna("").astype(str)
df["website_domain"] = df['website_domain'].fillna("").astype(str)

# create clean columns
df["company_name_clean"] = (
    df["company_name"].str.lower()
    .str.replace("[^a-z0-9]", "", regex=True)
)

df["website_domain_clean"] = (
    df["website_domain"].str.lower()
    .str.replace("www.|http://|https://", "", regex=True)
)


def find_duplicates(df, threshold=85):
    duplicates = []
    #Let's optimize and group by country and city
    grouped = df.groupby(['main_country_code', 'main_city'])
    for _, group in grouped:
        group = group.reset_index(drop=True)
        for i in range(len(group)):
            for j in range(i+1, len(group)):
                name_i = df.iloc[i]["company_name_clean"]
                name_j = df.iloc[j]["company_name_clean"]
                if not name_i or not name_j:
                    continue
                similarity = fuzz.ratio(name_i, name_j)
                website_match = group.loc[i, "website_domain_clean"] == group.loc[j, "website_domain_clean"]
                if similarity > threshold or website_match:
                    duplicates.append((
                        group.loc[i, "company_name"],
                        group.loc[j, "company_name"],
                        similarity,
                        website_match
                    ))
    return duplicates

duplicates = find_duplicates(df)
print(f'I found {len(duplicates)} potential duplicates')

# Seeing the found duplicates
for dup in duplicates:
    print(f"\nSimilaritate {dup[2]}% între:")
    print(f"- {dup[0]}")
    print(f"- {dup[1]}")
    print(f"Website match: {dup[3]}")

