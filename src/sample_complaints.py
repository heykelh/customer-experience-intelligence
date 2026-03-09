import pandas as pd

# fichier source
input_file = "data/raw/complaints.csv"

# fichier sortie
output_file = "data/processed/complaints_sample.csv"

chunk_size = 100000
sample_size = 20000

chunks = []
total_rows = 0

print("Reading dataset in chunks...")

for chunk in pd.read_csv(input_file, chunksize=chunk_size):

    chunk = chunk.dropna(subset=["Consumer complaint narrative"])

    chunks.append(chunk)

    total_rows += len(chunk)

    if total_rows >= sample_size:
        break

df = pd.concat(chunks)

df = df.sample(sample_size)

columns_to_keep = [
    "Product",
    "Issue",
    "Consumer complaint narrative",
    "Company",
    "State",
    "Date received"
]

df = df[columns_to_keep]

df.columns = [
    "product",
    "issue",
    "complaint_text",
    "company",
    "state",
    "date_received"
]

df.to_csv(output_file, index=False)

print("Sample created :", output_file)