from jackTokenizer import *
from TokenType import *

# add a jackTokenizer
jack_tokenizer = JackTokenizer()

file = open("test.xml", "w")
file.write("<token>\n")

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
            file.write(f"  <string>{jack_tokenizer.current_token}</string>\n")

        case TokenType.INT_CONST:
            print(jack_tokenizer.int_val())
            file.write(f"  <int>{jack_tokenizer.current_token}</int>\n")

        case TokenType.SYMBOL:
            print(jack_tokenizer.symbol())
            file.write(f"  <symbol>{jack_tokenizer.current_token}</symbol>\n")

        case TokenType.KEYWORD:
            print(jack_tokenizer.key_word())
            file.write(f"  <keyword>{jack_tokenizer.current_token}</keyword>\n")

        case TokenType.IDENTIFIER:
            print(jack_tokenizer.identifier())
            file.write(f"  <identifier>{jack_tokenizer.current_token}</identifier>\n")

        case other:
            print("not a token")

    print("\n")

file.write("</token>")
