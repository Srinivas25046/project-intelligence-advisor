from ingestion import ingest
import os

sample_dir = "sample_docs"
for filename in os.listdir(sample_dir):
    path = os.path.join(sample_dir, filename)
    print(f"\n--- Testing {filename} ---")
    records = ingest(path)
    if records:
        print(f"Success: {len(records)} record(s) extracted")
        print(f"Preview: {records[0].text[:80]}")
    else:
        print("No records returned (empty file or unsupported type)")