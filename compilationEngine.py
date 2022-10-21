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

    # compiles a while statement. grammar: while (expression){statement}
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
        self.tokenizer.advance()
        current_token = self.tokenizer.current_token
        assert token == current_token
