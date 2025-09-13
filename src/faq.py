from pathlib import Path
import pandas as pd
import chromadb
from chromadb.utils import embedding_functions
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()


os.environ["TOKENIZERS_PARALLELISM"] = "false"
# faqs_path = Path(__file__).parents[1]/"data/resources/faq_data.csv"
chroma_client = chromadb.Client()
collection_name_faq = 'faqs'
EMB_FUN = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="sentence-transformers/all-MiniLM-L6-v2")
MODEL = "llama-3.3-70b-versatile"
gorq_client = Groq()


def ingest_faq_data(path):
    if collection_name_faq not in [c.name for c in chroma_client.list_collections()]:
        collection = chroma_client.get_or_create_collection(
            name = collection_name_faq,
            embedding_function = EMB_FUN
        )
        df = pd.read_csv(path)
        docs = df['question'].to_list()
        metadata = [{'answer': ans } for ans in df['answer'].to_list()]
        ids = [f"id_{i}" for i in range(len(docs))]
        
        collection.add(
            documents=docs,
            metadatas=metadata,
            ids=ids
        )
        print(f"FAQ Data successfully ingested into Chroma collection: {collection_name_faq}")
    else:
        print(f"Collection: {collection_name_faq} already exist!")

def get_relevant_qa(query):
    collection = chroma_client.get_collection(name=collection_name_faq)
    result = collection.query(
        query_texts=[query],
        n_results=2
    )
    return result


def faq_chain(query):
    result = get_relevant_qa(query)
    context = ''.join([res.get('answer') for res in result['metadatas'][0]])
    answer = generate_answer(query, context)
    return answer

def generate_answer(query, context):
    
    prompt = f""" Given the question and context below, generate the answer based on the context only. If you don't find the answer inside the context then say "I don't know".
    Do not make things up.

    Question: {query} 

    context: {context}
    """

    # Call LLMs
    chat_completion = gorq_client.chat.completions.create(
        model=MODEL,
        messages=[
        {
            "role": "user",
            "content": prompt
        }
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=True,
        stop=None
    )

    response_text = ""
    for chunk in chat_completion:
        delta = chunk.choices[0].delta.content
        if delta:  # only append if not None
            response_text += delta

    return response_text


# if __name__ == "__main__":
#     ingest_faq_data(faqs_path)
#     query = "What is the return policy of the products?"
#     result = faq_chain(query)
#     print("result", result)