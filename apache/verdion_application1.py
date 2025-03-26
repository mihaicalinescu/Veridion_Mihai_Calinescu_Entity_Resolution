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
    for i in range(len(df)):
        for j in range(i+1, len(df)):
            # conditions for avoiding unnecessary comparison
            name_i = df.iloc[i]["company_name_clean"]
            name_j = df.iloc[j]["company_name_clean"]

            if not name_i or not name_j:
                continue

            same_country = df.iloc[i]["main_country_code"] == df.iloc[j]["main_country_code"]
            same_city = df.iloc[i]["main_city"] == df.iloc[j]["main_city"]


            if same_country and same_city:
                name_similarity = fuzz.ratio(name_i, name_j)
                website_match = df.iloc[i]["website_domain_clean"] == df.iloc[j]["website_domain_clean"]

                if name_similarity > threshold or website_match:
                    duplicates.append((i, j, name_similarity, website_match))

    return duplicates

duplicates = find_duplicates(df)
print(f'I found {len(duplicates)} potential duplicates')

# Seeing the found duplicates
for i, j, similarity, website_match in duplicates:
    print(f"\nPotrivire între:")
    print(f"- {df.iloc[i]['company_name']} ({df.iloc[i]['main_city']}, {df.iloc[i]['website_domain']})")
    print(f"- {df.iloc[j]['company_name']} ({df.iloc[j]['main_city']}, {df.iloc[j]['website_domain']})")
    print(f"Similaritate nume: {similarity}%, Website match: {website_match}")

