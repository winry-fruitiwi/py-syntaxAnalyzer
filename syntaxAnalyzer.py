from jackTokenizer import *
from TokenType import *

# add a jackTokenizer
jack_tokenizer = JackTokenizer()

# while there are still more tokens, print out the tokenizer's current character
# and advance the current letter.
while jack_tokenizer.has_more_tokens():
    jack_tokenizer.advance()
    print("current character: " + jack_tokenizer.current_char)
    print("current token: " + jack_tokenizer.current_token)
    print(jack_tokenizer.current_char_index)
    print(jack_tokenizer.is_symbol(jack_tokenizer.current_char))
    print(jack_tokenizer.is_delimiter(jack_tokenizer.current_char))

    token_type = jack_tokenizer.token_type()

    match token_type:
        case TokenType.STRING_CONST:
            print(jack_tokenizer.string_val())

        case TokenType.INT_CONST:
            print(jack_tokenizer.int_val())

        case TokenType.SYMBOL:
            print(jack_tokenizer.symbol())

        case TokenType.KEYWORD:
            print(jack_tokenizer.key_word())

        case TokenType.IDENTIFIER:
            print(jack_tokenizer.identifier())

        case other:
            print("not a token")

    print("\n")


file = open("test.xml", "w")
file.write("<tokens>hello!</tokens>")
