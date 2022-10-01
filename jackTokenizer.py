class JackTokenizer:
    def __init__(self):
        # open the input file.
        self.input_file = open("test.jack").readlines()

        # a list of all the symbols in the jack language.
        self.symbols = [
            '{',
            '}',
            '(',
            ')',
            '[',
            ']',
            '.',
            ',',
            ';',
            '+',
            '-',
            '*',
            '/',
            '&',
            '|',
            '<',
            '>',
            '=',
            '~'
        ]

        # a list of the file's lines that will be stripped of whitespace, new
        # lines, full line comments, and inline comments.
        self.stripped_lines = []

        for line in self.input_file:
            # strip the whitespace, then newlines and whitespace before the
            # newlines.
            stripped_line = line.strip(" ").strip("\n").strip(" ")
            try:
                # if the stripped line is an empty space, don't append it to
                # the list of stripped lines.
                if stripped_line == "":
                    continue

                # if the stripped line starts with a //, it's a comment, so we
                # don't append it to the list of stripped lines.
                if stripped_line[0:2] == "//":
                    continue

                # this is why there's a try-except block. index() returns a
                # ValueError if the substring doesn't exist. in this block,
                # I'm checking if there is a //, which signals the beginning
                # of a comment no matter where it is.
                if stripped_line.index("//"):
                    # if there is an index, then take a slice from 0 to the
                    # index.
                    stripped_line = stripped_line[0:stripped_line.index("//")]

                    # most inline comments will have whitespace between them
                    # and the code that they're explaining. We need to strip
                    # that.
                    stripped_line = stripped_line.strip(" ")

                # finally, if the stripped line is now just an empty line,
                # signaling that this was a full-line comment, then we don't
                # have to append the line to self.stripped_lines anymore.
                if stripped_line == "":
                    continue

            # if there is no //, then a ValueError will be raised and the
            # except block will fire.
            except ValueError:
                pass

            self.stripped_lines.append(stripped_line)

        # the two indices below handle where I am in my list of stripped lines.
        self.current_line_index = 0
        self.current_char_index = 0

        # the current character
        self.current_char = None

    # detects if the tokenizer has more tokens
    def has_more_tokens(self):
        # return if the current character index is the same as
        # the maximum character index for this line. then do the same for the
        # line index. after finding the result, reverse it.
        return not (self.current_char_index == len(
            self.stripped_lines[self.current_line_index])-1
                    and self.current_line_index == len(self.stripped_lines) - 1)

    # advances the current token to the next token
    def advance(self):
        # the current line's length
        curr_line = self.stripped_lines[self.current_line_index]
        current_line_length = len(curr_line) - 1

        # if the current character is None, initialize it.
        if self.current_char is None:
            self.current_char = self.stripped_lines[0][0]

        # if there are characters left in the line, I increment current_char_index
        elif self.current_char_index < current_line_length:
            self.current_char_index += 1

        # elif there are no more characters left in the line and there are still
        # more lines, increment current_line_index and reset current_char_index
        elif (self.current_char_index == current_line_length
              and self.current_line_index < len(self.stripped_lines) - 1):
            self.current_line_index += 1
            self.current_char_index = 0

        # update the current character
        self.current_char = self.stripped_lines[self.current_line_index][
            self.current_char_index]

        # a list of all the delimiters I have encountered
        delimiter_list = [0]

        # appends the index of every delimiter found to delimiter_list
        for char_index in range(len(self.stripped_lines[self.current_line_index])):
            char = self.stripped_lines[self.current_line_index][char_index]
            if self.is_delimiter(char):
                delimiter_list.append(char_index)
                if self.is_symbol(char):
                    delimiter_list.append(char_index+1)

        # a list of all the slices I can make out of my delimiter list
        slice_list = []

        # print a list of slices of the current line's tokens
        for index in range(len(delimiter_list) - 1):
            next_index = index+1
            slice_list.append(curr_line[delimiter_list[index]:delimiter_list[next_index]])

        print(slice_list)

    # checks the type of the current token
    def token_type(self):
        pass

    # returns current token if it's a keyword
    def key_word(self):
        pass

    # returns current token if it's a symbol
    def symbol(self):
        pass

    # returns current token if it's an identifier
    def identifier(self):
        pass

    # returns current token if it's a integer constant
    def int_val(self):
        pass

    # returns current token if it's a string constant. Does not handle quotes.
    def string_val(self):
        pass

    # returns if current character is a symbol.
    def is_symbol(self, char):
        return char in self.symbols

    # returns if current character is a symbol, whitespace, or newline.
    def is_delimiter(self, char):
        return (self.is_symbol(char) or
                char == "\n" or
                char == " "
                )
