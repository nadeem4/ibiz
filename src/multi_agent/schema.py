
from __future__ import annotations

from typing import TypedDict

class AgentState(TypedDict, total=False):
    user_query: str
    next: str
    response: str
    context: str
