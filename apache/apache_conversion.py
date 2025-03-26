import pandas as pd

df = pd.read_parquet("veridion_entity_resolution_challenge.snappy.parquet")
df.to_csv("veridion_entity_resolution_challenge.csv", index=False)