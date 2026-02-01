class Explainability:
    @staticmethod
    def wrap_output(ai_output: str, context: str) -> dict:
        """
        Presents AI output alongside clear explanation about its use.
        Example context: 'This summary highlights key areas for human review only. No decisions automated.'
        """
        return {
            "ai_output": ai_output,
            "explanation": context,
            "for_decision": False
        }