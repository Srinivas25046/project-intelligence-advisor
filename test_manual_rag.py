from graph import pipeline_graph
from rag_pipeline import search

# Step 1: Run ingestion + indexing through the LangGraph pipeline
result = pipeline_graph.invoke({
    "file_paths": ["sample_docs/notes.txt"],
    "records": [],
    "chunks_indexed": 0
})

print(f"Records ingested: {len(result['records'])}")
print(f"Chunks indexed: {result['chunks_indexed']}")

# Step 2: Test retrieval with a sample query
query = "what are the risks?"
results = search(query)

print(f"\nQuery: {query}")
for r in results:
    print(f"- ({r['source']}) {r['text'][:100]}")