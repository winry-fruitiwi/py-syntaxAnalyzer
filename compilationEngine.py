class CompilationEngine:
    def __init__(self):
        pass

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

    # compiles a variable declaration.
    def compile_var_dec(self):
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
        pass

    # compiles a let statement. grammar: let varName([expression])?=expression;
    def compile_let_statement(self):
        pass

    # compiles an if statement. grammar: if (expression){statement} (else
    # {statements})?
    def compile_if_statement(self):
        pass

    # compiles a while statement. grammar: while (expression){statement}
    def compile_while_statement(self):
        pass

    # compiles a do statement. grammar: do subRoutineCall;
    def compile_do_statement(self):
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
        pass
