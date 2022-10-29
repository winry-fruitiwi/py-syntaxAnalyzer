from jackTokenizer import *


class CompilationEngine:
    def __init__(self, path):
        self.tokenizer = JackTokenizer(path)
        self.output = open("test.xml", "w")

        # signals to eat() if we need to skip advance()
        self.skip_advance = False

    # compiles a complete class. This needs to be called immediately after
    # an instance is initialized.
    def compileClass(self):
        # eat class
        self.eat("class")

        # compile an identifier
        self.compileIdentifier()

        # eat {
        self.eat("{")

        self.advance()
        self.skip_advance = True

        # compile statements. TODO change this to classVarDec and subRoutineDec
        while self.tokenizer.current_token in ["static", "field"]:
            self.compileClassVarDec()
            self.advance()
            self.skip_advance = True

        while self.tokenizer.current_token in ["constructor", "function",
                                               "method"]:
            self.compileSubRoutineDec()
            self.advance()
            self.skip_advance = True

        # eat }
        self.eat("}")

    # compiles a static variable or a field declaration.
    def compileClassVarDec(self):
        # eat either static or field
        if not self.skip_advance:
            self.advance()
        self.skip_advance = True

        if self.tokenizer.current_token == "static":
            self.eat("static")
        else:
            self.eat("field")

        # advance
        self.advance()
        self.skip_advance = True

        # compile a type
        self.compileType()

        # compile an identifier
        self.compileIdentifier()

        # advance
        self.advance()
        self.skip_advance = True

        # while the next token is a comma, eat a comma and compile an identifier
        while self.tokenizer.current_token == ",":
            self.eat(",")
            self.compileIdentifier()

            self.advance()
            self.skip_advance = True
        self.eat(";")

    # compiles the inside of a subroutine declaration
    def compileSubRoutineBody(self):
        # eat {
        self.eat("{")

        # advance
        self.advance()
        self.skip_advance = True

        # while the current token is var, compile varDec
        while self.tokenizer.current_token == "var":
            self.compileVarDec()
            self.advance()
            self.skip_advance = True

        # compile statements
        self.compileStatements()

        # eat }
        self.eat("}")
        pass

    # compiles a complete method, function, or constructor.
    def compileSubRoutineDec(self):
        # advance, then check for either constructor, function, or method
        if not self.skip_advance:
            self.advance()
        self.skip_advance = True

        match self.tokenizer.current_token:
            case "constructor":
                self.eat("constructor")
            case "function":
                self.eat("function")
            case "method":
                self.eat("method")

        # advance, then check for void or type
        self.advance()
        self.skip_advance = True

        if self.tokenizer.current_token == "void":
            self.eat("void")
        else:
            self.compileType()

        # compile an identifier
        self.compileIdentifier()

        # eat (
        self.eat("(")

        # compile parameterList (empty function for now)
        self.compileParameterList()

        # eat )
        self.eat(")")

        # compile subRoutineBody. for now, this can just be a compile statement
        # for statements in brackets.
        self.compileSubRoutineBody()

    # compilers a parameter list. doesn't handle enclosing parentheses.
    def compileParameterList(self):
        self.advance()
        self.skip_advance = True
        if (self.tokenizer.current_token in ["int", "char", "boolean"] or
                self.tokenizer.tokenType() == TokenType.IDENTIFIER):
            # compile type
            self.compileType()

            # compile identifier
            self.compileIdentifier()

            # advance
            self.advance()
            self.skip_advance = True

            # while the token is a comma, eat it, compile type and identifier,
            # then advance.
            while self.tokenizer.current_token == ",":
                self.eat(",")
                self.advance()
                self.skip_advance = True
                self.compileType()
                self.compileIdentifier()

                self.advance()
                self.skip_advance = True

    # compiles a variable declaration. grammar: var type varName(,varName)*;
    def compileVarDec(self):
        """
        <varDec>
            <keyword> var </keyword>
            <identifier> SquareGame </identifier>
            <identifier> game </identifier>
            <symbol> ; </symbol>
        </varDec>
            :return:
        """

        # eat var
        self.eat("var")

        # advance
        self.advance()
        self.skip_advance = True

        # compile a type
        self.compileType()

        # compile an identifier
        self.compileIdentifier()

        # advance
        self.advance()
        self.skip_advance = True

        # while the next token is a comma, eat a comma and compile an identifier
        while self.tokenizer.current_token == ",":
            self.eat(",")
            self.compileIdentifier()

            self.advance()
            self.skip_advance = True
        self.eat(";")

    # compiles a sequence of statements. doesn't handle enclosing {}s. grammar:
    # statement*
    def compileStatements(self):
        # advance
        if not self.skip_advance:
            self.advance()
        self.skip_advance = True

        # while the current token is do, while, if, let, or return, call
        # compileStatement
        while self.tokenizer.current_token in ["while", "do", "if", "let",
                                               "return"]:
            self.compileStatement()

            self.advance()
            self.skip_advance = True
            print("\n\nstatement done!\n\n")

        # at the end of each iteration, advance
        pass

    # compiles a sequence of statements inside curly brackets
    def compileStatementsInBrackets(self):
        self.eat("{")
        self.compileStatements()
        self.eat("}")

    # helper functions!

    # compiles a type
    def compileType(self):

        # eat int, char, boolean, or an identifier
        match self.tokenizer.current_token:
            case "int":
                self.eat("int")
                return
            case "char":
                self.eat("char")
                return
            case "boolean":
                self.eat("boolean")
                return
        if self.tokenizer.tokenType() == TokenType.IDENTIFIER:
            self.compileIdentifier()

        pass

    # compiles a single statement. A helper function for compile_statements.
    # grammar: letStatement|ifStatement|whileStatement|doStatement|returnStatement
    def compileStatement(self):
        # match-case for do, while, return, let, and if statements
        # for each case, compile the respective statement.

        match self.tokenizer.current_token:
            case "do":
                self.compileDoStatement()
            case "if":
                self.compileIfStatement()
            case "while":
                self.compileWhileStatement()
            case "let":
                self.compileLetStatement()
            case "return":
                self.compileReturnStatement()

    # compiles a let statement. grammar: let varName([expression])?=expression;
    def compileLetStatement(self):
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
        # add opening tag
        self.output.write("<letStatement>\n")

        # eat let
        self.eat("let")

        # compile an identifier
        self.compileIdentifier()

        # advance and check for a bracket. If there is one, eat [, compile
        # expression, and then eat ]. If not, continue.
        self.advance()
        self.skip_advance = True
        if self.tokenizer.current_token == "[":
            self.eat("[")
            self.compileExpression()
            self.eat("]")

        # eat =
        self.eat("=")

        # compile expression
        self.compileExpression()

        # eat ;
        self.eat(";")

        self.output.write("</letStatement>\n")

    # compiles an if statement. grammar: if (expression){statement} (else
    # {statements})?
    def compileIfStatement(self):
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
        self.eat("if")

        # eat expression in parens
        self.compileExprInParens()

        # eat statement in brackets
        self.compileStatementsInBrackets()

        # advance the tokenizer, then check if the current token is else. if
        # it is, then eat else and {statements}.
        self.advance()
        self.skip_advance = True
        if self.tokenizer.current_token == "else":
            self.eat("else")
            self.compileStatementsInBrackets()

        # write ending tag to output
        self.output.write("</ifStatement>\n")

    # compiles a while statement. grammar: while (expression) {statements}
    def compileWhileStatement(self):
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
        self.eat("while")

        # compile (expression)
        self.compileExprInParens()

        # compile {statements}
        self.compileStatementsInBrackets()

        # write closing tag
        self.output.write("</whileStatement>\n")

        pass

    # compiles a do statement. grammar: do subRoutineCall;
    def compileDoStatement(self):
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

        # eat do
        self.output.write("<doStatement>\n")
        self.eat("do")

        # compile subRoutineCall
        self.compileSubRoutineCall()

        # eat ;
        self.eat(";")

        # ending tag
        self.output.write("</doStatement>\n")

        pass

    # compiles a return statement. grammar: return expression?;
    def compileReturnStatement(self):
        # eat return
        self.output.write("<returnStatement>\n")
        self.eat("return")

        # advance, set skip_advance to true
        self.advance()
        self.skip_advance = True

        # if the current token is "this" or type identifier, compile a term
        if (self.tokenizer.current_token == "this" or
                self.tokenizer.tokenType() == TokenType.IDENTIFIER):
            self.compileExpression()

        # no matter what happened previously, eat ";"
        self.eat(";")

        # write output tag
        self.output.write("</returnStatement>\n")

    # compiles an expression. Important: do this last! grammar: term (op term)*
    # for now call compile_simple_term here
    def compileExpression(self):
        self.compileSimpleTerm()

    # compiles an expression within parentheses.
    def compileExprInParens(self):
        self.eat("(")
        self.compileExpression()
        self.eat(")")

    # compiles a term.
    def compileTerm(self):
        pass

    # compiles a massively simplified version of compile_term
    def compileSimpleTerm(self):
        if not self.skip_advance:
            self.advance()
            self.skip_advance = True
        if self.tokenizer.current_token == "this":
            self.eat("this")

        else:
            self.compileIdentifier()

    # compiles a comma-separated list of expressions. can be empty.
    def compileExpressionList(self):
        self.advance()
        self.skip_advance = True
        # if simpleTerm's requirements are met:
        if (self.tokenizer.current_token == "this" or
                self.tokenizer.tokenType() == TokenType.IDENTIFIER):
            # compile an expression
            self.compileExpression()

            # while commas are detected, eat a comma and then compile an
            # expression.
            self.advance()
            self.skip_advance = True
            while self.tokenizer.current_token == ",":
                self.eat(",")
                self.compileExpression()
                self.advance()
                self.skip_advance = True

    # compiles an identifier
    def compileIdentifier(self):
        if not self.skip_advance:
            self.advance()
        else:
            self.skip_advance = False

        assert self.tokenizer.tokenType() == TokenType.IDENTIFIER

        self.output.write(
            f"<identifier> {self.tokenizer.identifier()} </identifier>\n")

    def compileStrConst(self):
        if not self.skip_advance:
            self.advance()
        else:
            self.skip_advance = False

        assert self.tokenizer.tokenType() == TokenType.STRING_CONST

        self.output.write(
            f"<stringConstant> {self.tokenizer.stringVal()} </stringConstant>\n")

    def compileIntConst(self):
        if not self.skip_advance:
            self.advance()
        else:
            self.skip_advance = False

        assert self.tokenizer.tokenType() == TokenType.STRING_CONST

        self.output.write(
            f"<integerConstant> {self.tokenizer.intVal()} </integerConstant>\n")

    def compileKeyword(self):
        if not self.skip_advance:
            self.advance()
        else:
            self.skip_advance = False

        assert self.tokenizer.tokenType() == TokenType.KEYWORD

        self.output.write(f"<keyword> {self.tokenizer.keyword()} </keyword>\n")

    # advances the tokenizer and checks if it's a delimiter or not a token.
    def advance(self):
        # advance the tokenizer.
        self.tokenizer.advance()

        # get the token type of the tokenizer.
        token_type = self.tokenizer.tokenType()

        # if the token is the start of a line or a delimiter, advance again,
        # setting the token type again as well
        while token_type == "delimiter" or token_type == "Not a token.":
            self.tokenizer.advance(

            )
            token_type = self.tokenizer.tokenType()

    # asserts that the next token is its first argument. its second argument, a
    # boolean, determines whether to advance. We can sometimes not advance when
    # dealing with expressions.
    def eat(self, token):
        # advance the current character if second argument is true.
        if not self.skip_advance:
            self.advance()
        else:
            self.skip_advance = False

        token_type = self.tokenizer.tokenType()

        # there are several value that token_type can take on. I used match-case
        # statements here. Depending on the value that token_type takes on, I'll
        # add a tag describing it appropriately.
        match token_type:
            case TokenType.STRING_CONST:
                self.output.write(
                    f"<stringConstant> {self.tokenizer.stringVal()} </stringConstant>\n")

            case TokenType.INT_CONST:
                self.output.write(
                    f"<integerConstant> {self.tokenizer.intVal()} </integerConstant>\n")

            case TokenType.SYMBOL:
                self.output.write(
                    f"<symbol> {self.tokenizer.symbol()} </symbol>\n")

            case TokenType.KEYWORD:
                self.output.write(
                    f"<keyword> {self.tokenizer.keyword()} </keyword>\n")

            case TokenType.IDENTIFIER:
                self.output.write(
                    f"<identifier> {self.tokenizer.identifier()} </identifier>\n")

        current_token = self.tokenizer.current_token
        assert token == current_token

    # a simple function that tests a single compile statement.
    def testCompile(self):
        self.compileExpressionList()

    # an unneeded subroutine call method for use in terms and do statements.
    def compileSubRoutineCall(self):
        # compile an identifier
        self.compileIdentifier()

        # eat (
        self.eat("(")

        # compile an expression
        self.compileExpression()

        # eat )
        self.eat(")")

        pass
