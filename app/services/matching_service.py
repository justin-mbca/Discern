from app.ai.llm_interface import LLMSummarizer
from app.ai.embedding_utils import EmbeddingUtils
from app.ai.explainability import Explainability

llm = LLMSummarizer(api_key="YOUR_API_KEY")
embedder = EmbeddingUtils(api_key="YOUR_API_KEY")

def run_matching(user_a_profile: dict, user_b_profile: dict):
    summary_a = llm.summarize_profile(user_a_profile)
    summary_b = llm.summarize_profile(user_b_profile)

    emb_a = embedder.get_embedding(str(user_a_profile))
    emb_b = embedder.get_embedding(str(user_b_profile))
    similarity = embedder.cosine_similarity(emb_a, emb_b)

    wrapped_a = Explainability.wrap_output(summary_a, "Profile summary for human agency review")
    wrapped_b = Explainability.wrap_output(summary_b, "Profile summary for human agency review")

    return {
        "user_a_summary": wrapped_a,
        "user_b_summary": wrapped_b,
        "similarity_score": similarity,
        "decision_must_be_human": True
    }