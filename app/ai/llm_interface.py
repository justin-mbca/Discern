import openai

class LLMSummarizer:
    def __init__(self, api_key: str):
        openai.api_key = api_key

    def summarize_profile(self, user_profile: dict) -> str:
        prompt = (
            "Summarize this relationship profile for human matchmaker review. "
            "Focus on values, priorities, and patterns. Avoid judgment. "
            f"Profile: {user_profile}"
        )
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']

    def reflect_conversation(self, transcript: str) -> str:
        prompt = (
            "Reflect on this relationship conversation for discernment. "
            "Identify alignment, emerging friction, and missing information. "
            f"Conversation transcript: {transcript}"
        )
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
