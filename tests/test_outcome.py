
from app.evaluators.outcome import OutcomeEvaluator


def test_correct_agent_passes():
    evaluator = OutcomeEvaluator()

    expected = {
        "expected_answer": "Refund request must be verified before approval.",
        "expected_action": "verify_order",
    }

    actual = {
        "answer": "Refund request must be verified before approval.",
        "action": "verify_order",
    }

    result = evaluator.evaluate(expected, actual)

    assert result["passed"] is True
    assert result["score"] == 1.0


def test_broken_agent_fails():
    evaluator = OutcomeEvaluator()

    expected = {
        "expected_answer": "Refund request must be verified before approval.",
        "expected_action": "verify_order",
    }

    actual = {
        "answer": "Task completed successfully.",
        "action": "no_action",
    }

    result = evaluator.evaluate(expected, actual)

    assert result["passed"] is False
    assert result["score"] == 0.0
