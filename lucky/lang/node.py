#!/usr/bin/python3

import abc

class Node(abc.ABC):
    """
    Representation of a single character in a Lucky source file.
    """
    def __init__(self, line: int, column: int):
        self.line = line
        self.column = column

class ExpressionNode(Node):
    def __init__(self, line: int, column: int):
        super().__init__(line, column)

class StatementNode(Node):
    def __init__(self, line: int, column: int):
        super().__init__(line, column)

class LiteralNode(ExpressionNode):
    def __init__(self, line: int, column: int, value: int):
        super().__init__(line, column)
        self.value = value

class ReturnStatementNode(StatementNode):
    def __init__(self, line: int, column: int, expression: ExpressionNode):
        super().__init__(line, column)
        assert isinstance(expression, ExpressionNode)
        self.expression = expression

class BlockNode(Node):
    def __init__(self, line: int, column: int, statements: list[StatementNode]):
        super().__init__(line, column)
        assert all([isinstance(n, StatementNode) for n in statements])
        self.statements = statements

class FunctionDefNode(Node):
    def __init__(self, line: int, column: int, type: str, identifier: str, body: BlockNode):
        super().__init__(line, column)
        self.type = type
        self.identifier = identifier
        assert isinstance(body, BlockNode)
        self.body = body

class ProgramNode(Node):
    def __init__(self, line: int, column: int, func_defs: list[FunctionDefNode]) -> None:
        super().__init__(line, column)
        assert all([isinstance(n, FunctionDefNode) for n in func_defs])
        self.func_defs = func_defs

