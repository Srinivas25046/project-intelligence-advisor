from ingestion import ingest

records = ingest("sample_docs/notes.txt")
for r in records:
    print(r)