from enum import Enum
from dataclasses import dataclass


class TokenType(Enum):
    NUMBER = 0
    PLUS = 1
    MINUS = 2
    MULTIPLY = 3
    DIVIDE = 4
    POWER = 5
    RADICAL = 6
    LOG = 7
    SIN = 8
    COS = 9
    TAN = 10
    LPAREN = 11
    RPAREN = 12


@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value is not None else "")
