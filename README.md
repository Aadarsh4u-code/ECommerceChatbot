# E-Commerce Chatbot

# 📝 Project Overview
The **E-Commerce Chatbot** is an AI-powered assistant designed to enhance the user experience on XYZ’s e-commerce platform. It assists users with:
- **Frequently Asked Questions (FAQs)**
- **Product inquiries (pricing & availability)**

This solution drives engagement, improves customer satisfaction, and supports seamless interaction between customers and the platform.



# 🚀 Project Objective

**Objective 1:** Build a chatbot prototype with core functionalities for FAQs and product inquiries.

1. **FAQ Data Ingestion into Chromadb** – Efficient ingestion and vectorization of FAQs into the Chromadb vector database.
2. **Streamlit Chatbot Frontend** – Interactive, user-friendly chatbot interface built with Streamlit.
3. **Route Support:**
   - FAQs → Answers retrieved from the FAQ database.
   - Product Inquiries → Product & pricing information pulled from SQLite database.


**Objective 2:** Expand chatbot capabilities and deploy on the e-commerce website (Integration).

1. **Full-scale Deployment** – Transition from Streamlit to a production-ready environment for large-scale interactions.
2. **Website Integration** – Embed chatbot seamlessly into XYZ’s website to support live customer queries.
3. **Performance Optimization & Testing** – High accuracy and minimal latency for real-time interactions.


# 🛠️ Tech Stack
- **Language Model:** LLama3.3 LLM
- **Frontend:** Streamlit (prototype)
- **Databases:**
  - Chromadb → FAQ vector storage
  - SQLite → Product & pricing storage
- **Routing:** Semantic router


# 📊 **Workflow**  
1. **User Input (Streamlit UI)** – User types a query into the chatbot (e.g., “Do you accept cash on delivery?” or “Show me top Nike shoes under 80 with rating >4.3”).

2. **Semantic Router** – Classifies the query type:
    - FAQ – general queries (payment, return policy, etc.)
    - Product – product search and filtering queries

3. **FAQ Flow (RAG Retrieval)**
    - Query sent to ChromaDB (vector database).
    - Retrieves relevant answers from stored FAQs.
    - LLM refines response → generates natural-language Answer.  

4. **Product Flow (SQL Retrieval)**
    - Query passed to LLM, which converts it into an SQL query
    - SQL query executed on SQLite database (product catalog)
    - Retrieved Records + Question are sent back to the LLM
    - LLM composes a user-friendly Answer with product details

5. **Response Delivery** – Final answer displayed in Streamlit UI, including links, product details, and recommendations.  


# 🖥️ **Example Usage**  

**Input:**  
```  
Q.1. What is the return policy of the products?
Q.2. How do I use a promo code during checkout? 
```  
**Output:**  
```  
Answer 1: The return policy of the products is that you can return them within 30 days of delivery, and you need to contact the support team within 48 hours for a replacement or refund.
Answer 2: To use a promo code during checkout, enter your promo code in the designated field..
``` 


## ✅ Success Criteria
- Fully functional chatbot capable of handling FAQs and product inquiries.
- Accurate & efficient ingestion of FAQs into Chromadb.
- Smooth integration with XYZ’s e-commerce website with minimal downtime.

---

# ▶️ Getting Started

### Prerequisites
- Python 3.10+
- Virtual environment (recommended)

### Installation
```bash
git clone https://github.com/Aadarsh4u-code/ECommerceChatbot
cd ecommerce-chatbot
pip install -r requirements.txt
```

### Run the Streamlit Chatbot
```bash
streamlit run src/frontend/app.py
```
---

## 📜 License
This project is licensed under the [MIT License](LICENSE).
