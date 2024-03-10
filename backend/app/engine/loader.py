import os
from llama_index.core import (
    SimpleDirectoryReader,
)


def get_documents():
    reader = SimpleDirectoryReader(os.getenv("DATA_DIR"))
    documents = reader.load_data()
    return documents
