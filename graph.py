from typing import TypedDict
from langgraph.graph import StateGraph, END
from ingestion import ingest
from rag_pipeline import index_documents


class State(TypedDict):
    file_paths: list
    records: list
    chunks_indexed: int


def ingest_step(state):
    all_records = []
    for path in state["file_paths"]:
        all_records.extend(ingest(path))
    state["records"] = all_records
    return state


def index_step(state):
    state["chunks_indexed"] = index_documents(state["records"])
    return state


builder = StateGraph(State)
builder.add_node("ingest", ingest_step)
builder.add_node("index", index_step)
builder.set_entry_point("ingest")
builder.add_edge("ingest", "index")
builder.add_edge("index", END)

pipeline_graph = builder.compile()