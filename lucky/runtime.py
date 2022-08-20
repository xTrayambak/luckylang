#!/usr/bin/env python

from lucky.lang.build_ast import ASTBuilder
from lucky.lang.parser import Parser

class Runtime:
    def __init__(self, file: str, mode: int = 0):
        self.parser = Parser('grammar/main.lark')
        self.ast_builder = ASTBuilder()

        tree = self.parser.parse(file)
        import rich

        rich.print(tree)

        transformed = ASTBuilder().transform(tree)
        rich.print(transformed)
