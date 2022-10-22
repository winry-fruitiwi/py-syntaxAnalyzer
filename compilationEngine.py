from jackTokenizer import *


class CompilationEngine:
    def __init__(self, path):
        self.tokenizer = JackTokenizer(path)
        self.output = open("test.xml", "w")

    # compiles a complete class. This needs to be called immediately after
    # an instance is initialized.
    def compile_class(self):
        pass

    # compiles a static variable or a field declaration.
    def compile_class_var_dec(self):
        pass

    # compiles a complete method, function, or constructor.
    def compile_subroutine_dec(self):
        pass

    # compilers a parameter list. doesn't handle enclosing parentheses.
    def compile_parameter_list(self):
        pass

    # compiles a variable declaration. grammar: var type varName(,varName)*;
    def compile_var_dec(self):
        """
        <varDec>
            <keyword> var </keyword>
            <identifier> SquareGame </identifier>
            <identifier> game </identifier>
            <symbol> ; </symbol>
        </varDec>
        :return:
        """

        pass

    # compiles a sequence of statements. doesn't handle enclosing {}s. grammar:
    # statement*
    # TODO implement compile_statement. That's already difficult enough. The
    #      functions I will use here will not include expressions, as those are
    #      extremely difficult. That means I won't be able to test my functions
    #      for a while.
    def compile_statements(self):
        pass

    # compiles a sequence of statements inside curly brackets
    def compile_statements_in_brackets(self):
        self.eat("{", True)
        self.compile_statements()
        self.eat("}", True)

    # helper functions!

    # compiles a single statement. A helper function for compile_statements.
    # grammar: letStatement|ifStatement|whileStatement|doStatement|returnStatement
    def compile_statement(self):
        """

        :return:
        """
        pass

    # compiles a let statement. grammar: let varName([expression])?=expression;
    def compile_let_statement(self):
        """
        <letStatement>
          <keyword> let </keyword>
          <identifier> game </identifier>
          <symbol> = </symbol>
          <expression>
            <term>
              <identifier> game </identifier>
            </term>
          </expression>
          <symbol> ; </symbol>
        </letStatement>

        :return:
        """
        pass

    # compiles an if statement. grammar: if (expression){statement} (else
    # {statements})?
    def compile_if_statement(self):
        """
        <ifStatement>
          <keyword> if </keyword>
          <symbol> ( </symbol>
          <expression>
            <term>
              <identifier> b </identifier>
            </term>
          </expression>
          <symbol> ) </symbol>
          <symbol> { </symbol>
          <statements>
          </statements>
          <symbol> } </symbol>
          <keyword> else </keyword>
          <symbol> { </symbol>
          <statements>
          </statements>
          <symbol> } </symbol>
        </ifStatement>

        :return:
        """

        # write opening tag, eat if
        self.output.write("<ifStatement>\n")
        self.eat("if", True)

        # eat expression in parens
        self.compile_expr_in_parens()

        # eat statement in brackets
        self.compile_statements_in_brackets()

        # advance the tokenizer, then check if the current token is else. if
        # it is, then eat else and {statements}.
        self.advance()
        if self.tokenizer.current_token == "else":
            self.eat("else", False)
            self.compile_statements_in_brackets()

        # write ending tag to output
        self.output.write("</ifStatement>")

    # compiles a while statement. grammar: while (expression) {statements}
    def compile_while_statement(self):
        """
        <whileStatement>
          <keyword> while </keyword>
          <symbol> ( </symbol>
          <expression>
            <term>
              <identifier> key </identifier>
            </term>
          </expression>
          <symbol> ) </symbol>
          <symbol> { </symbol>
          <statements>
            <letStatement>
              <keyword> let </keyword>
              <identifier> key </identifier>
              <symbol> = </symbol>
              <expression>
                <term>
                  <identifier> key </identifier>
                </term>
              </expression>
              <symbol> ; </symbol>
            </letStatement>
            <doStatement>
              <keyword> do </keyword>
              <identifier> moveSquare </identifier>
              <symbol> ( </symbol>
              <expressionList>
              </expressionList>
              <symbol> ) </symbol>
              <symbol> ; </symbol>
            </doStatement>
          </statements>
          <symbol> } </symbol>
        </whileStatement>

        :return:
        """
        # while + write to output
        self.output.write("<whileStatement>\n")
        self.eat("while", False)

        # compile (expression)
        self.compile_expr_in_parens()

        # compile {statements}
        self.compile_statements_in_brackets()

        # write closing tag
        self.output.write("</whileStatement>\n")

        pass

    # compiles a do statement. grammar: do subRoutineCall;
    def compile_do_statement(self):
        """
        <doStatement>
          <keyword> do </keyword>
          <identifier> moveSquare </identifier>
          <symbol> ( </symbol>
          <expressionList>
          </expressionList>
          <symbol> ) </symbol>
          <symbol> ; </symbol>
        </doStatement>

        :return:
        """

        pass

    # compiles a return statement. grammar: return expression?;
    def compile_return_statement(self):
        # eat return

        pass

    # compiles an expression. Important: do this last! grammar: term (op term)*
    # for now call compile_simple_term here
    def compile_expression(self):
        self.compile_simple_term()

    # compiles an expression within parentheses.
    def compile_expr_in_parens(self):
        self.eat("(", True)
        self.compile_expression()
        self.eat(")", True)

    # compiles a term.
    def compile_term(self):
        pass

    # compiles a massively simplified version of compile_term
    def compile_simple_term(self):
        if self.tokenizer.current_token == "this":
            self.eat("this", False)

        else:
            self.compile_identifier()

    # compiles a comma-separated list of expressions. can be empty.
    def compile_expression_list(self):
        pass

    # compiles an identifier
    def compile_identifier(self):
        self.tokenizer.advance()

        assert self.tokenizer.token_type() == TokenType.IDENTIFIER

        self.output.write(f"<identifier> {self.tokenizer.identifier()} </identifier>\n")

    # advances the tokenizer and checks if it's a delimiter or not a token.
    def advance(self):
        # advance the tokenizer.
        self.tokenizer.advance()

        # get the token type of the tokenizer.
        token_type = self.tokenizer.token_type()

        # if the token is the start of a line or a delimiter, advance again,
        # setting the token type again as well
        while token_type == "delimiter" or token_type == "Not a token.":
            self.tokenizer.advance(

            )
            token_type = self.tokenizer.token_type()

    # asserts that the next token is its first argument. its second argument, a
    # boolean, determines whether to advance. We can sometimes not advance when
    # dealing with expressions.
    def eat(self, token, advance):
        # advance the current character if second argument is true.
        if advance:
            self.advance()
            print("token: " + self.tokenizer.current_token)
            print("advanced!")

        token_type = self.tokenizer.token_type()

        # there are several value that token_type can take on. I used match-case
        # statements here. Depending on the value that token_type takes on, I'll
        # add a tag describing it appropriately.
        match token_type:
            case TokenType.STRING_CONST:
                self.output.write(
                    f"<stringConstant> {self.tokenizer.string_val()} </stringConstant>\n")

            case TokenType.INT_CONST:
                self.output.write(
                    f"<integerConstant> {self.tokenizer.int_val()} </integerConstant>\n")

            case TokenType.SYMBOL:
                print("symbol: " + self.tokenizer.symbol())
                self.output.write(f"<symbol> {self.tokenizer.symbol()} </symbol>\n")

            case TokenType.KEYWORD:
                self.output.write(f"<keyword> {self.tokenizer.key_word()} </keyword>\n")

            case TokenType.IDENTIFIER:
                self.output.write(
                    f"<identifier> {self.tokenizer.identifier()} </identifier>\n")

        print(self.tokenizer.current_token)
        current_token = self.tokenizer.current_token
        assert token == current_token

    # a simple function that tests a single compile statement.
    def test_compile(self):
        self.compile_if_statement()
