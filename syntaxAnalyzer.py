from jackTokenizer import *

# add a jackTokenizer
jack_tokenizer = JackTokenizer()

# while there are still more tokens, print out the tokenizer's current character
# and advance the current letter.
while jack_tokenizer.has_more_tokens():
    jack_tokenizer.advance()
    print(jack_tokenizer.current_char)
    print(jack_tokenizer.is_symbol(jack_tokenizer.current_char))
    print(jack_tokenizer.is_delimiter(jack_tokenizer.current_char))
    print("\n")

    # this provides a stop for the infinite loop
    input("press enter:")
