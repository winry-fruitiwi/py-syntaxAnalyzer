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
        self.eat("}", False)

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
        pass

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
        pass

    # compiles an expression. Important: do this last! grammar: term (op term)*
    def compile_expression(self):
        pass

    # compiles an expression within parentheses.
    def compile_expr_in_parens(self):
        self.eat("(", True)
        self.compile_expression()
        self.eat(")", False)

    # compiles a term.
    def compile_term(self):
        pass

    # compiles a comma-separated list of expressions. can be empty.
    def compile_expression_list(self):
        pass

    # asserts that the next token is its first argument. its second argument, a
    # boolean, determines whether to advance. We can sometimes not advance when
    # dealing with expressions.
    def eat(self, token, advance):
        # advance the current character if second argument is true.
        if advance:
            self.tokenizer.advance()
            print(self.tokenizer.current_token)
            print("advanced!")

        # get the token type of the tokenizer.
        token_type = self.tokenizer.token_type()

        if token_type == "delimiter" or token_type == "Not a token.":
            self.tokenizer.advance()

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
        self.compile_while_statement()
