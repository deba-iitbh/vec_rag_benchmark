import os
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.settings import Settings


def init_settings():
    llm_model = os.getenv("MODEL", "codellama:7b")
    embedding_model = os.getenv("EMBEDDING_MODEL", "BAAI/bge-small-en-v1.5")

    Settings.llm = Ollama(model=llm_model, temperature=0, request_timeout=30)
    Settings.embed_model = HuggingFaceEmbedding(model_name=embedding_model)
    Settings.chunk_size = 1024
    Settings.chunk_overlap = 20
