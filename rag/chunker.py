from langchain.text_splitter import RecursiveCharacterTextSplitter


def chunk_document(text: str, company_id: str):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=250, separators=["\n\n", "\n", ". ", " ", ""]
    )

    chunks = text_splitter.split_text(text)

    documents = chunks
    metadatas = [
        {"company_id": company_id, "chunk_index": i, "total_chunks": len(chunks)}
        for i in range(len(chunks))
    ]
    ids = [f"{company_id}_chunk_{i}" for i in range(len(chunks))]

    return documents, metadatas, ids
