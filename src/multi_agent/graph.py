from __future__ import annotations

from typing import Annotated, Literal, TypedDict

from langchain_core.messages import BaseMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from pydantic import BaseModel, Field

from multi_agent.config import Settings
from multi_agent.schema import AgentState
from multi_agent.nodes.rag.node import RAGNode
from multi_agent.nodes.supervisor.node import SupervisorNode
from multi_agent.vector_store import VectorStore
from multi_agent.embedding import EmbeddingService
from multi_agent.nodes.api.node import APINode






def build_graph(settings: Settings):
    llm = ChatOpenAI(api_key=settings.openai_api_key, model=settings.openai_model)
    workflow = StateGraph(AgentState)

    workflow.add_node('supervisor', SupervisorNode(VectorStore(EmbeddingService.get_embedding(),  collection_name='rag_data')))
    workflow.add_node('api_agent', APINode())
    workflow.add_node('rag_agent', RAGNode(llm))

    workflow.set_entry_point('supervisor')

    def route(state: AgentState) -> Literal['api_agent', 'rag_agent']:
        return state['next']
    
    workflow.add_conditional_edges('supervisor', route, {'api_agent': 'api_agent', 'rag_agent': 'rag_agent'})
    workflow.add_edge('api_agent', END)
    workflow.add_edge('rag_agent', END)
    

    return workflow.compile()
