from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()

generaltalk_client = Groq()
MODEL = "llama-3.3-70b-versatile"
client_sql = Groq()



def generaltalk_chain(query):
    prompt=f"""
    You are a Genral conversatation assistant, helpful and friendly chatbot. You can answer generic 
    questions about weather, what you do, your name, and anything else in a single line. 
    
    QUESTION : {query}
    """
    chat_completion = generaltalk_client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt},
        ],
        model=MODEL,
    )

    return chat_completion.choices[0].message.content