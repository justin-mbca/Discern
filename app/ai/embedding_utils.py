import openai
import numpy as np

class EmbeddingUtils:
    def __init__(self, api_key: str):
        openai.api_key = api_key

    def get_embedding(self, text: str) -> list:
        response = openai.Embedding.create(
            input=text,
            model="text-embedding-ada-002"
        )
        return response['data'][0]['embedding']

    @staticmethod
    def cosine_similarity(vec1, vec2) -> float:
        v1 = np.array(vec1)
        v2 = np.array(vec2)
        return float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))