import os
import pdfplumber
import docx
import pandas as pd
from models import DocumentRecord


def parse_pdf(file_path):
    records = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                records.append(DocumentRecord(
                    text=text,
                    source_file=os.path.basename(file_path),
                    doc_type="general"
                ))
    return records


def parse_docx(file_path):
    doc = docx.Document(file_path)
    text = "\n".join(p.text for p in doc.paragraphs if p.text)
    if not text:
        return []
    return [DocumentRecord(
        text=text,
        source_file=os.path.basename(file_path),
        doc_type="general"
    )]


def parse_csv(file_path):
    df = pd.read_csv(file_path)
    records = []
    for _, row in df.iterrows():
        line = ", ".join(f"{col}: {row[col]}" for col in df.columns)
        records.append(DocumentRecord(
            text=line,
            source_file=os.path.basename(file_path),
            doc_type="general"
        ))
    return records


def parse_txt(file_path):
    with open(file_path, "r") as f:
        text = f.read()
    if not text:
        return []
    return [DocumentRecord(
        text=text,
        source_file=os.path.basename(file_path),
        doc_type="general"
    )]


def ingest(file_path):
    ext = file_path.split(".")[-1].lower()
    if ext == "pdf":
        return parse_pdf(file_path)
    elif ext == "docx":
        return parse_docx(file_path)
    elif ext == "csv":
        return parse_csv(file_path)
    elif ext == "txt":
        return parse_txt(file_path)
    else:
        print(f"Unsupported file type: {ext}")
        return []