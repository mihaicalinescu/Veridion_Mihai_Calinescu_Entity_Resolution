from multiprocessing.reduction import duplicate

import pandas as pd
from fuzzywuzzy import fuzz

df = pd.read_csv("veridion_entity_resolution_challenge.csv")
cols = ['company_name', 'company_legal_names', 'website_domain', "main_city", "main_country_code"]

# Removing duplicates
df = df[cols].drop_duplicates()

# Normalization of company name and website domains
df["company_name_clean"] = df['company_name'].str.lower().str.replace('^a-z0-9', "", regex=True)


def find_duplicates(df, threshold=85):
    duplicates = []
    for i in range(len(df)):
        for j in range(i+1, len(df)):
            # conditions for avoiding unnecessary comparison
            same_country = df.iloc[i]['main_country_code'] == df.iloc[j]['main_country_code']
            same_city = df.iloc[i]['main_city'] == df.iloc[j]['main_city']

            if same_country and same_city:
                name_similarity = fuzz.ratio(
                    df.iloc[i]['company_name_clean'],
                    df.iloc[j]['company_name_clean']
                )
                website_match = df.iloc[i]['website_domain_clean'] == df.iloc[j]['website_domain_clean']

                if name_similarity > threshold or website_match:
                    duplicate.append((i, j, name_similarity, website_match))

    return duplicates

duplicates = find_duplicates(df)
print(f'I found {len(duplicates)} potential duplicates')

# Seeing the found duplicates
for i, j, similarity, website_match in duplicates:
    print(f"\nPotrivire între:")
    print(f"- {df.iloc[i]['company_name']} ({df.iloc[i]['main_city']}, {df.iloc[i]['website_domain']})")
    print(f"- {df.iloc[j]['company_name']} ({df.iloc[j]['main_city']}, {df.iloc[j]['website_domain']})")
    print(f"Similaritate nume: {similarity}%, Website match: {website_match}")