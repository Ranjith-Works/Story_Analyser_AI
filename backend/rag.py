import faiss
import numpy as np


def create_vectorstore(embeddings):
    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    return index


def retrieve_chunks(query, model, index, chunks, k=3):
    query_embedding = model.encode([query])

    distances, indices = index.search(
        np.array(query_embedding),
        k
    )

    retrieved_chunks = []

    for idx in indices[0]:
        retrieved_chunks.append(chunks[idx])

    return retrieved_chunks