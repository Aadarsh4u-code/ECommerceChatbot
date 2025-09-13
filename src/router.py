from semantic_router import Route, SemanticRouter
from semantic_router.encoders import HuggingFaceEncoder



encoder = HuggingFaceEncoder(
    name="sentence-transformers/all-MiniLM-L6-v2"
)

# we could use this as a guide for our chatbot to learn question from conversations
faqs = Route(
    name="faqs",
    utterances=[
        "What is the return policy of the products?",
        "Do I get discount with any credit card?",
        "How can I track my order?",
        "What payment methods are accepted?",
        "What should I do if I receive a damaged product?",
    ],
    score_threshold=0.3
)

# this could be used as an indicator to our chatbot to switch to a more
# conversational prompt
sql = Route(
    name="sql",
    utterances=[
        "I want to buy nike shoes that have 50% discount.",
        "Are there any shoes under Rs. 3000?",
        "Do you have formal shoes in size 9?",
        "Are there any Puma shoes on sale?",
        "What is the price of puma running shoes?",
    ],
    score_threshold=0.3
)

smalltalk = Route(
    name="smalltalk",
    utterances=[
        "How are you?",
        "What is your name?",
        "What do you do?",
        "How is the weather today?",
    ],
    score_threshold=0.3
)


router = SemanticRouter(encoder=encoder, routes=[faqs, sql, smalltalk], auto_sync="local")


# if __name__ == "__main__":
#     print(router("What is your policy on defective product?").name)
#     print(router("Pink Puma shoes in price range 5000 to 1000").name)