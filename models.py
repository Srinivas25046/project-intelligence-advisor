from pydantic import BaseModel

class DocumentRecord(BaseModel):
    text: str
    source_file: str
    doc_type: str

class QueryRequest(BaseModel):
    query: str