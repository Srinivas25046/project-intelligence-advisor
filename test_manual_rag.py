import os
import shutil

# Clear old vector store data BEFORE importing anything that opens it
shutil.rmtree("vectorstore", ignore_errors=True)

from graph import pipeline_graph
from rag_pipeline import search

sample_dir = "sample_docs"
file_paths = [os.path.join(sample_dir, f) for f in os.listdir(sample_dir)]

result = pipeline_graph.invoke({
    "file_paths": file_paths,
    "records": [],
    "chunks_indexed": 0
})

print(f"Files processed: {len(file_paths)}")
print(f"Records ingested: {len(result['records'])}")
print(f"Chunks indexed: {result['chunks_indexed']}")

test_queries = [
    "what are the risks?",
    "java program",
    "circle and arc",
    "industry agriculture forestry",
]

for query in test_queries:
    print(f"\nQuery: {query}")
    results = search(query, top_k=3)
    for r in results:
        print(f"- ({r['source']}) {r['text'][:100]}")