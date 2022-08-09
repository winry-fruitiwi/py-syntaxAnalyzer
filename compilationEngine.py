class CompilationEngine:
    def __init__(self):
        pass

    # compiles a complete class.
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

    # compiles a sequence of statements. doesn't handle enclosing {}s.
    def compile_statements(self):
        pass

    # compiles an expression.
    def compile_expression(self):
        pass

    # compiles a term.
    def compile_term(self):
        pass

    # compiles a comma-separated list of expressions. can be empty.
    def compile_expression_list(self):
        pass
