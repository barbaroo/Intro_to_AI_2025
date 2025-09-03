from logic import *

# Define your symbols:
colors = ["red", "blue", "green", "yellow"]
symbols = []
for i in range(4):
    for color in colors:
        symbols.append(Symbol(f"{color}{i}"))

# Initialize your knowledge base:
knowledge = And()

# TO DO:

# Encode in the knowledge base what you know: each color has a position.


# Encode in the knowledge base what you know: only one position per color (if a color is in a position, another color cannot be in the same position).


# Encode in the knowledge base what you know: only one color per position.


# Add to the knowledge base what you have learned with the first round (case with 2 correct positions)

# Add to the knowledge base what you have learned with the first round (case with 0 correct positions)


# Run the model checking algorithm for each symbol, to see which are entailed by the knowledge base


