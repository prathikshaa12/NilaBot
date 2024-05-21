import re

# Expanded implicit dataset of cat-related questions and answers
cat_data = {
    "what do cats eat": "Cats are obligate carnivores, which means they primarily eat meat. A balanced diet for a cat includes proteins, fats, and a small amount of carbohydrates.",
    "how long do cats live": "The average lifespan of an indoor cat is around 15 years, but some cats can live into their 20s. Outdoor cats generally have a shorter lifespan.",
    "why do cats purr": "Cats purr for various reasons, including contentment, to calm themselves when they're sick or stressed, and even as a healing mechanism.",
    "how do you train a cat": "Training a cat involves positive reinforcement, like treats and praise. You can teach cats to use a litter box, scratch posts, and even do tricks!",
    "what is the best way to groom a cat": "Regular grooming helps keep a cat's coat clean and reduces shedding. Use a brush suited for your cat's fur type, and be gentle to avoid causing stress.",
    "why do cats knead": "Cats knead with their paws when they're feeling happy or content. It is thought to be a comforting behavior that originates from kittenhood.",
    "how can you tell if a cat is happy": "A happy cat often shows it through behaviors such as purring, kneading, having a relaxed posture, and showing interest in play and interaction.",
    "why do cats have whiskers": "Cats use their whiskers to sense their environment. Whiskers help them detect objects and navigate spaces, especially in the dark.",
    "how do cats communicate": "Cats communicate through a combination of vocalizations (like meowing and purring), body language (such as tail position and ear orientation), and scent marking.",
    "what are some common health problems in cats": "Some common health problems in cats include dental issues, obesity, urinary tract infections, and respiratory infections. Regular vet check-ups are important for early detection and treatment.",
}

def is_cat_query(query):
    cat_keywords = ["cat", "cats", "kitty", "kitties", "kitten", "kittens"]
    pattern = re.compile(r'\b(' + '|'.join(cat_keywords) + r')\b', re.IGNORECASE)
    return pattern.search(query) is not None

def find_answer(query):
    query = query.lower()
    for question in cat_data:
        if question in query:
            return cat_data[question]
    return None

def sweet_response(query, answer):
    return f"Aww, I love talking about cats! Here's something I found about \"{query}\": {answer} Cats are truly wonderful, aren't they?"

def chatbot():
    print("Hi there! I'm your friendly chatbot. Ask me anything about cats, and I'll be happy to chat!")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye! Have a purrfect day!")
            break
        if is_cat_query(user_input):
            print("Chatbot: Notifying... 🐱")
            answer = find_answer(user_input)
            if answer:
                print("Chatbot:", sweet_response(user_input, answer))
            else:
                print("Chatbot: I'm not sure about that. But I love all things cat-related!")
        else:
            print("Chatbot: I'm here to talk about cats! Ask me anything about our feline friends.")

if __name__ == "__main__":
    chatbot()
