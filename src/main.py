
import streamlit as st
from router import router
from faq import ingest_faq_data, faq_chain
from pathlib import Path

st.title("🏙️ E-Commerce Chatbot")


# **************************************** Session Setup ******************************

if "message_history" not in st.session_state:
    st.session_state['message_history'] = []



# **************************************** Ask Query to LLMs ******************************

project_root = Path(__file__).resolve().parent.parent  # one level above src/
faqs_path = project_root / "data/resources/faq_data.csv"

ingest_faq_data(faqs_path)

def ask_query(query):
    print(router(query),'test............')
    route = router(query).name
    print("route", route)
    if route == "faqs":
        return faq_chain(query)
    else:
        return f"Route {route} not implemented yet."




# **************************************** Main UI ************************************

# Loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])



user_input = st.chat_input("Write your query here...")

if user_input:
    # First add the message to chat_history
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)



    response = ask_query(user_input)
    with st.chat_message("assistance"):
        st.text(response)
    st.session_state['message_history'].append({'role': 'assistance', 'content': response})