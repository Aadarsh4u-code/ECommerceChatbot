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


## 🛠️ Tech Stack
- **Language Model:** LLama3.3 LLM
- **Frontend:** Streamlit (prototype)
- **Databases:**
  - Chromadb → FAQ vector storage
  - SQLite → Product & pricing storage
- **Routing:** Semantic router


## ✅ Success Criteria
- Fully functional chatbot capable of handling FAQs and product inquiries.
- Accurate & efficient ingestion of FAQs into Chromadb.
- Smooth integration with XYZ’s e-commerce website with minimal downtime.

---

# 📂 Repository Structure (example)
```
.
├── data/               # FAQ and product datasets
├── notebooks/          # Experimentation and model testing
├── src/                # Core chatbot code
│   ├── ingestion/      # Scripts for FAQ data ingestion into Chromadb
│   ├── routing/        # Semantic router logic
│   └── frontend/       # Streamlit app
├── tests/              # Unit and integration tests
└── README.md           # Project documentation
```


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
