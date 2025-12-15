from __future__ import annotations

from multi_agent.schema import AgentState

class RAGNode:
    
    def __init__(self, llm):
        self.llm = llm


    def __call__(self, state: AgentState):
        user_query = state.get("user_query", "")
        context = state.get("context", "")

        prompt = f"Use the following context to answer the question.\n\nContext: {context}\n\nQuestion: {user_query}\n\nAnswer:"

        response = self.llm.chat([{"role": "user", "content": prompt}])

        return {
            "response": response['choices'][0]['message']['content'],
            "next": "end"
        }