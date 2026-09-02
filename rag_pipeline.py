from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma(collection_name="project_docs", embedding_function=embeddings, persist_directory="./vectorstore")


def index_documents(records):
    texts = []
    metadatas = []
    for record in records:
        chunks = splitter.split_text(record.text)
        for chunk in chunks:
            texts.append(chunk)
            metadatas.append({"source_file": record.source_file, "doc_type": record.doc_type})

    if texts:
        vectorstore.add_texts(texts=texts, metadatas=metadatas)
    return len(texts)


def search(query, top_k=3):
    results = vectorstore.similarity_search(query, k=top_k)
    return [{"text": r.page_content, "source": r.metadata.get("source_file")} for r in results]