class JackTokenizer:
    def __init__(self):
        pass

    # detects if the tokenizer has more tokens
    def has_more_tokens(self):
        pass

    # advances the current token to the next token
    def advance(self):
        pass

    # checks the type of the current token
    def token_type(self):
        pass

    # returns current token if it's a keyword
    def key_word(self):
        pass

    # returns current token if it's a symbol
    def symbol(self):
        pass

    # returns current token if it's a identifier
    def identifier(self):
        pass

    # returns current token if it's a integer constant
    def int_val(self):
        pass

    # returns current token if it's a string constant. Does not handle quotes.
    def string_val(self):
        pass
