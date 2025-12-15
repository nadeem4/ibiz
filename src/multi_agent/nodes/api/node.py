from __future__ import annotations
from multi_agent.schema import AgentState
import requests

def call_api() -> str:
    # Simulated API call
    response = requests.get("https://jsonplaceholder.typicode.com/albums")
    return "API call successful, retrieved albums data."

class APINode:
    def __init__(self):
        pass

    def __call__(self, state: AgentState):
        response = call_api()
        return {
            "response": response,
            "next": "end"
        }