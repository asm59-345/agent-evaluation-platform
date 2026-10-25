
class ScriptedAgent:
    """A deterministic agent for testing without an LLM API."""

    def __init__(self, mode: str = "correct"):
        self.mode = mode

    def run(self, task: dict) -> dict:
        if self.mode == "broken":
            return {
                "answer": "Task completed successfully.",
                "action": "no_action",
            }

        return {
            "answer": task["expected_answer"],
            "action": task["expected_action"],
        }
