
class OutcomeEvaluator:
    """Checks whether an agent achieved the expected outcome."""

    def evaluate(self, expected: dict, actual: dict) -> dict:
        checks = {
            "answer_correct": (
                actual.get("answer") == expected.get("expected_answer")
            ),
            "action_correct": (
                actual.get("action") == expected.get("expected_action")
            ),
        }

        passed = all(checks.values())

        return {
            "passed": passed,
            "score": 1.0 if passed else 0.0,
            "checks": checks,
        }
