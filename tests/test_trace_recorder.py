
from app.telemetry.trace_recorder import TraceRecorder


def test_trace_recorder_records_events():
    recorder = TraceRecorder()

    recorder.record(
        "task_started",
        {"task_id": "task_001"},
    )

    recorder.record(
        "agent_response",
        {"answer": "Test response"},
    )

    events = recorder.get_events()

    assert len(events) == 2
    assert events[0]["sequence"] == 1
    assert events[1]["sequence"] == 2
    assert events[0]["event_type"] == "task_started"
