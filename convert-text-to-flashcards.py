text = "Expressions of location in Chinese may include a preposition, placed before the noun; a postposition, placed after the noun; both preposition and postposition; or neither. Chinese prepositions are commonly known as coverbs – see the Coverbs section"
convert_to_flashcards(text, count=3)
# Should print:
# What are Chinese prepositions commonly known as? | coverbs
# What do expressions of location in Chinese include? | postpositions and prepositions
# What is a postposition? | a location-related word placed after a noun

text = "discord.js is a powerful Node.js  module that allows you to easily interact with the Discord API."
convert_to_flashcards(text, count=2)
# Should print:
# What is discord.js? | a Node.js module that allows you to easily interact with the Discord API.
# What is a Node.js module allows you to easily interact with the Discord API? | discord.js

text = "Gradient descent (also often called steepest descent) is a first-order iterative optimization algorithm for finding a local minimum of a differentiable function. The idea is to take repeated steps in the opposite direction of the gradient (or approximate gradient) of the function at the current point, because this is the direction of steepest descent. Conversely, stepping in the direction of the gradient will lead to a local maximum of that function; the procedure is then known as gradient ascent."
convert_to_flashcards(text, count=6)
# Should print:
