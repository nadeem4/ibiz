from __future__ import annotations

from multi_agent.schema import AgentState
from multi_agent.vector_store import VectorStore


class SupervisorNode:
    def __init__(self,vector_store: VectorStore):
        self.vector_store = vector_store


    def __call__(self, state: AgentState):
        user_query = state.get("user_query", "")

        res = self.vector_store.query(user_query)
        score = res[0][1]
        print(f"SupervisorNode: score={score}")
        return {
            "next": "rag_agent" if score <= 0.5 else "api_agent",
            "context": res[0][0]
        }

        
