import os
import hashlib

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import (
    GROQ_API_KEY,
    GROQ_BASE_URL,
    MODEL_NAME,
    EMBEDDING_MODEL,
    CHROMA_PERSIST_DIR,
    COLLECTION_NAME,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    KNOWLEDGE_BASE_PATH,
    SYSTEM_PROMPT,
)


def init_embeddings():
    return HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)


def load_and_chunk_document(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n## ", "\n### ", "\n\n", "\n", " ", ""],
    )
    return splitter.create_documents([text])


def _get_file_hash(file_path: str) -> str:
    with open(file_path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()


def init_vector_store(embeddings):
    hash_file = os.path.join(CHROMA_PERSIST_DIR, ".doc_hash")
    current_hash = _get_file_hash(KNOWLEDGE_BASE_PATH)

    # Re-use existing store if document hasn't changed
    if os.path.exists(CHROMA_PERSIST_DIR) and os.path.exists(hash_file):
        with open(hash_file, "r") as f:
            stored_hash = f.read().strip()
        if stored_hash == current_hash:
            print("Loading existing vector store...")
            return Chroma(
                collection_name=COLLECTION_NAME,
                embedding_function=embeddings,
                persist_directory=CHROMA_PERSIST_DIR,
            )

    # Build new vector store
    print("Building vector store from knowledge base...")
    documents = load_and_chunk_document(KNOWLEDGE_BASE_PATH)

    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        collection_name=COLLECTION_NAME,
        persist_directory=CHROMA_PERSIST_DIR,
    )

    # Save hash for future runs
    os.makedirs(CHROMA_PERSIST_DIR, exist_ok=True)
    with open(hash_file, "w") as f:
        f.write(current_hash)

    print(f"Indexed {len(documents)} chunks.")
    return vector_store


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def build_rag_chain(retriever):
    llm = ChatOpenAI(
        base_url=GROQ_BASE_URL,
        api_key=GROQ_API_KEY,
        model=MODEL_NAME,
        streaming=True,
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", "Context:\n{context}\n\nQuestion: {question}"),
    ])

    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return chain


def initialize_rag():
    print("Initializing RAG pipeline...")
    embeddings = init_embeddings()
    vector_store = init_vector_store(embeddings)
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    chain = build_rag_chain(retriever)
    print("RAG pipeline ready.")
    return chain
