from jackTokenizer import *
from TokenType import *

XML = open("test.xml", "w")
XML.write("<token>")

# add a jackTokenizer
jack_tokenizer = JackTokenizer()

# while there are still more tokens, print out the tokenizer's current character
# and advance the current letter.
while jack_tokenizer.has_more_tokens():
    # advance the current character.
    jack_tokenizer.advance()

    # get the token type of the tokenizer.
    token_type = jack_tokenizer.token_type()

    # there are several value that token_type can take on. I used match-case
    # statements here. Depending on the value that token_type takes on, I'll
    # add a tag describing it appropriately.
    match token_type:
        case TokenType.STRING_CONST:
            XML.write(f"  <stringConstant> {jack_tokenizer.string_val()} </stringConstant>\n")

        case TokenType.INT_CONST:
            XML.write(f"  <integerConstant> {jack_tokenizer.int_val()} </integerConstant>\n")

        case TokenType.SYMBOL:
            XML.write(f"  <symbol> {jack_tokenizer.symbol()} </symbol>\n")

        case TokenType.KEYWORD:
            XML.write(f"  <keyword> {jack_tokenizer.key_word()} </keyword>\n")

        case TokenType.IDENTIFIER:
            XML.write(f"  <identifier> {jack_tokenizer.identifier()} </identifier>\n")

        case "delimiter":
            print("delim")

        case other:
            print("not a token")
            XML.write("\n")

    print("\n")


XML.write("</token>")
XML.write("\n")
XML.close()
