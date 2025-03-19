# You are given the following string:

# quote = "The best way to get started is to quit talking and begin doing."

# Write code to:

# a) Slice the string to print only the first 15 characters.

# b) Replace the word "quit" with "stop".

# c) Find how many times the word "to" appears in the string.

quote = "The best way to get started is to quit talking and begin doing."

quote = quote.replace("quit", "stop")
print(quote[0:15])
print(quote.count("to"))
print(quote)