import pandas as pd
from fuzzywuzzy import fuzz
import networkx as nx

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


def cluster_duplicates(df, threshold=85):
    # Let's group duplicated records using similarity of name or domain
    graph = nx.Graph()

    # Let's add all recordings as nodes
    grouped = df.groupby(['main_country_code', 'main_city'])
    for _, group in grouped:
        group_indices = group.index
        for i in range(len(group_indices)):
            for j in range(i+1, len(group_indices)):
                idx_i = group_indices[i]
                idx_j = group_indices[j]

                name_i = df.iloc[i]["company_name_clean"]
                name_j = df.iloc[j]["company_name_clean"]

                similarity = fuzz.ratio(name_i, name_j)
                website_match = (df.loc[idx_i, "website_domain_clean"] ==
                                df.loc[idx_j, "website_domain_clean"])
                if similarity > threshold or website_match:
                    graph.add_edge(idx_i, idx_j)

    # Here we identify clusters
    clusters = list(nx.connected_components(graph))

    # Each cluster gets a specific id
    cluster_mapping = {}
    for cluster_id, cluster in enumerate(clusters):
        for idx in cluster:
            cluster_mapping[idx] = cluster_id
    df['cluster_id'] = df.index.map(cluster_mapping)
    return df

df_clustered = cluster_duplicates(df)

# Showing all results
print(f"Număr total de companii unice identificate: {df_clustered['cluster_id'].nunique()}")
print("\nExemple de clustere (duplicate):")
for cluster_id in df_clustered['cluster_id'].unique()[:3]:  # Showing just the first 3 clusters
    cluster = df_clustered[df_clustered['cluster_id'] == cluster_id]
    print(f"\nCluster {cluster_id} (size: {len(cluster)}):")
    for _, row in cluster.iterrows():
        print(f"- {row['company_name']} (website: {row['website_domain']})")

# Saving in CSV file
output_file = "deduplicated_companies.csv"
df_clustered.to_csv(output_file, index=False)
print(f"\nRezultatele au fost salvate în '{output_file}'.")