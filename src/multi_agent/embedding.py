from __future__ import annotations

from langchain_core.embeddings import Embeddings
from langchain_openai import OpenAIEmbeddings
from typing import Optional
from multi_agent.config import settings

class EmbeddingService:

    _instance: Optional[Embeddings] = None

    @classmethod
    def get_embedding(cls) -> Embeddings:
        if cls._instance is None:
            cls._instance = OpenAIEmbeddings(model=settings.embedding_model, api_key=settings.openai_api_key)
        return cls._instance
    
    