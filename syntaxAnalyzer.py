"""
The main file, where I make JackTokenizers and CompilationEngines!

Files I've tested with the current version of code:
    10/Square/Main.jack
    10/Square/Square.jack
    10/Square/SquareGame.jack

"""

from compilationEngine import *
from TokenType import *

XML = open("test.xml", "w")
XML.write("<tokens>\n")

# the root of all files I'll need to test here.
file_root = ""

compilation_engine = CompilationEngine(file_root + "test.jack")


def mainLoop(ce):
    # # while there are still more tokens, print out the tokenizer's current character
    # # and advance the current letter.
    while ce.tokenizer.hasMoreTokens():
        # get the current token of the tokenizer.
        current_token = ce.tokenizer.current_token

        # use a match-case statement to check for possible lexical elements for the
        # compilation engine to compile
        match current_token:
            case "while":
                print(current_token)
                ce.compileWhileStatement()
                continue

        # advance the current character.
        ce.tokenizer.advance()

        # get the token type of the tokenizer.
        token_type = ce.tokenizer.tokenType()

        # there are several value that token_type can take on. I used match-case
        # statements here. Depending on the value that token_type takes on, I'll
        # add a tag describing it appropriately.
        match token_type:
            case TokenType.STRING_CONST:
                XML.write(
                    f"<stringConstant> {ce.tokenizer.stringVal()} </stringConstant>\n")

            case TokenType.INT_CONST:
                XML.write(
                    f"<integerConstant> {ce.tokenizer.intVal()} </integerConstant>\n")

            case TokenType.SYMBOL:
                XML.write(
                    f"<symbol> {ce.tokenizer.symbol()} </symbol>\n")

            case TokenType.KEYWORD:
                XML.write(
                    f"<keyword> {ce.tokenizer.keyword()} </keyword>\n")

            case TokenType.IDENTIFIER:
                XML.write(
                    f"<identifier> {ce.tokenizer.identifier()} </identifier>\n")

        print("\n")


XML.write("</tokens>")
XML.write("\n")
XML.close()


compilation_engine.testCompile()
