#!/usr/bin/python3

import lark
import rich
import pathlib

class Parser:
    """
    The Lucky Language code parser.
    Parses code using the lark library and sends it over to the LLVM backend for the execution process.
    """
    def __init__(
        self, grammar_file: pathlib.Path, start: str = 'program'
    ):
        if isinstance(grammar_file, str):
            grammar_file = pathlib.Path(grammar_file)

        with grammar_file.open() as grammar_file:
            grammar_data = grammar_file.read()

        self.lark = lark.Lark(grammar_data, start = start, ambiguity = 'explicit')

    def parse(self, file: str | pathlib.Path) -> lark.ParseTree:
        if isinstance(file, str):
            with open(file, 'r') as source_file:
                return self.parse_code(source_file.read())
        elif isinstance(file, pathlib.Path):
            with file.open() as source_file:
                return self.parse_code(source_file.read())

    def parse_code(self, source_code: str) -> lark.ParseTree:
        return self.lark.parse(source_code)

rich.print(Parser('grammar/main.lark').parse('tests/001.lc'))

