from langchain_core.embeddings import Embeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

rag_text = '''
The history of AI has had some embarrassingly optimistic predictions, particularly in the
early years. In short, AI researchers severely underestimated the difficulty of some of the
problems. Though there was success with designing programs that could play chess, it
turned out that recognizing the chess pieces in video was much more difficult.
Futurist Ray Kurzweil continues to publish optimistic predictions. He has popularized the
term "singularity" as it applies to AI (though the term was coined by Vernor Vinge for this
purpose.) The singularity is the point in time when Artificial Intelligence can automatically
improve on itself faster than humans where previously able to. The reason it's called the
singularity is because it is very difficult to know what will happen afterward, since the
future will then depend on the decisions of beings more intelligent than we are.
Kurzweil's predictions are based on a number of observations about the exponential
growth in certain fields, such as nanotechnology, computational power, genetic analysis,
and accuracy of brain scanning. Very basically, his argument is as follows: Brain scanning
technology is getting better at an exponential rate. Therefore, soon we will be able to scan
entire brains at the level of detail necessary to understand everything, physically, we need
to know to create a simulation of a brain in software. The exponential growth of
computational power will allow future computers to be able to process all of this data.
Having a brain in software will allow us to rapidly test and understand how intelligence
works in human beings (as well as other animals.) It will then be a short time before we can
improve on it.
'''

class VectorStore:


    def __init__(self, embedding: Embeddings, collection_name: str, dir: str = './vector_store'):
        self.embedding = embedding
        self.collection_name = collection_name
        self.vector_store = Chroma(
            collection_name=self.collection_name,
            embedding_function=self.embedding,
            persist_directory=dir 
        )

    def index(self):
        doc = Document(page_content=rag_text)
        self.vector_store.add_documents([doc])

    def query(self, query_text: str, n_results: int = 1) -> str:
        results = self.vector_store.similarity_search_with_score(query_text, k=n_results)
        print(f"VectorStore: query_text={query_text}, results={results}")
        return [(doc.page_content, score) for doc, score in results]


