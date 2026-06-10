import random
import socket
from flask import Flask
app = Flask(__name__)

# A simple list of completely neutral jokes
JOKES = [
    # "Why don't scientists trust atoms? Because they make up everything!",
    # "Why did the scarecrow win an award? Because he was outstanding in his field!",
    # "Why don't skeletons fight each other? They don't have the guts!",
    # "Why did the bicycle fall over? Because it was two-tired!",
    # "Why did the tomato turn red? Because it saw the salad dressing!"

    # New jokes added for version 2.0
    "Why did the math book look sad? Because it had too many problems.",
    "Why did the coffee file a police report? It got mugged.",
    "Why don't programmers like nature? It has too many bugs.",
]

@app.route('/')
def tell_a_joke():
    joke = random.choice(JOKES)
    hostname = socket.gethostname()
    return f"{joke}\n[V2.0] (from {hostname})"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)