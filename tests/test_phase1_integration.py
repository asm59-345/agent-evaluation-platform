import json
from pathlib import Path

from app.agents.scripted import ScriptedAgent
from app.telemetry.trace_recorder import TraceRecorder
from app.evaluators.outcome import OutcomeEvaluator


def test_broken_agent_gets_failing_score():
    task_path = (
        Path(__file__).resolve().parents[1]
        / "datasets"
        / "support"
        / "task_001.json"
    )

    task = json.loads(task_path.read_text(encoding="utf-8"))

    agent = ScriptedAgent(mode="broken")
    recorder = TraceRecorder()
    evaluator = OutcomeEvaluator()

    recorder.record("task_started", {"task_id": task["task_id"]})

    result = agent.run(task)
    recorder.record("agent_response", result)

    expected = {
        "expected_answer": task["expected_answer"],
        "expected_action": task["expected_action"],
    }

    evaluation = evaluator.evaluate(expected, result)
    recorder.record("evaluation_completed", evaluation)

    assert evaluation["passed"] is False
    assert evaluation["score"] == 0.0
    assert len(recorder.get_events()) == 3
