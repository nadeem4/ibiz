from __future__ import annotations

import argparse

from langchain_core.messages import HumanMessage

from multi_agent.config import settings
from multi_agent.graph import build_graph

from multi_agent.embedding import EmbeddingService
from multi_agent.vector_store import VectorStore


def run_once(question: str) -> str:
    graph = build_graph(settings)

    final_state = graph.invoke({"user_query":question})
    return final_state["response"]


def interactive():
    print("LangGraph multi-agent (type 'exit' to quit)")
    graph = build_graph(settings)

    state = {"user_query": ""}
    while True:
        question = input("\nYou> ").strip()
        if not question:
            continue
        if question.lower() in {"exit", "quit"}:
            break

        state = graph.invoke({"user_query": question})
    
        print(f"\nAssistant> {state['response']}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--question", type=str, default="")
    parser.add_argument("--index", action="store_true", help="Whether to index the data.")
    args = parser.parse_args()

    if args.index:
        vector_store = VectorStore(EmbeddingService.get_embedding(), collection_name='rag_data')
        vector_store.index()
        return 


    if args.question:
        print(run_once(args.question))
    else:
        interactive()


if __name__ == "__main__":
    main()
