from backend.file_loader import load_text
from backend.utils import chunk_text
from backend.embeddings import create_embeddings
from backend.rag import create_vectorstore
from backend.llm import extract_characters


def process_story(uploaded_file):
    """
    Processes an uploaded story and returns all required data.
    """

    story = load_text(uploaded_file)

    chunks = chunk_text(story)

    embeddings = create_embeddings(chunks)

    index = create_vectorstore(embeddings)

    characters = extract_characters(story)

    return {
        "story": story,
        "chunks": chunks,
        "index": index,
        "characters": characters
    }