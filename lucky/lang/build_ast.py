from lark import Token, Transformer

import lucky.lang.node as nodes

class ASTBuilder(Transformer):
    def LITERAL(self, item: Token) -> nodes.LiteralNode:
        return nodes.LiteralNode(item.line, item.column, int(item.value))

    def expr(self, items: list) -> nodes.ExpressionNode:
        return items[0]

    def return_stmt(self, items: list) -> nodes.ReturnStatementNode:
        expr = items[1]
        return nodes.ReturnStatementNode(expr.line, expr.column, expr)

    def block(self, items: list) -> nodes.BlockNode:
        statements = items[1:-1]
        return nodes.BlockNode(items[0].line, items[0].column, statements)

    def func_def(self, items: list) -> nodes.FunctionDefNode:
        type = items[0].value
        identifier = items[1].value
        body = items[2]
        return nodes.FunctionDefNode(items[0].line, items[0].column, type, identifier, body)

    def program(self, items: list) -> nodes.ProgramNode:
        return nodes.ProgramNode(0, 0, items)

