from dataclasses import dataclass
import math


@dataclass
class NumberNode:
    value: any

    def __repr__(self):
        return f"{self.value}"


@dataclass
class AddNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}+{self.node_b})"


@dataclass
class SubtractNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}-{self.node_b})"


@dataclass
class MultiplyNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}*{self.node_b})"


@dataclass
class DivideNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}/{self.node_b})"


@dataclass
class PowerNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({pow(self.node_a,self.node_b)})"


@dataclass
class LogNode:
    node: any

    def __repr__(self):
        return f"({math.log(self.node)})"


@dataclass
class RadicalNode:
    node: any

    def __repr__(self):
        return f"({math.sqrt(self.node)})"


@dataclass
class SinNode:
    node: any

    def __repr__(self):
        return f"({math.sin(self.node)})"


@dataclass
class CosNode:
    node: any

    def __repr__(self):
        return f"({math.cos(self.node)})"


@dataclass
class TanNode:
    node: any

    def __repr__(self):
        return f"({math.tan(self.node)})"


@dataclass
class PlusNode:
    node: any

    def __repr__(self):
        return f"(+{self.node})"


@dataclass
class MinusNode:
    node: any

    def __repr__(self):
        return f"(-{self.node})"
