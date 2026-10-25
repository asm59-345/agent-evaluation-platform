
from typing import Protocol


class BaseAgent(Protocol):
    """Common interface for evaluation agents."""

    def run(self, task: dict) -> dict:
        """Execute a task and return the agent result."""
        ...
