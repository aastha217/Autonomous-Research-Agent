import chromadb
import uuid

client = chromadb.PersistentClient(path="data/chroma_db")

collection = client.get_or_create_collection(
    name="research_documents"
)


def store_chunks(chunks, embeddings, title, url):
    ids = [str(uuid.uuid4()) for _ in chunks]

    metadatas = [
        {
            "title": title,
            "url": url
        }
        for _ in chunks
    ]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas
    )


def search(query_embedding, n_results=5):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results


def clear_collection():
    global collection

    try:
        client.delete_collection("research_documents")
    except Exception:
        # Ignore if the collection doesn't exist yet
        pass

    collection = client.get_or_create_collection(
        name="research_documents"
    )