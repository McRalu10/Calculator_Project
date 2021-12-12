from values import Number
import math


class Interpreter:
    def __init__(self):
        pass

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node)

    def visit_NumberNode(self, node):
        return Number(node.value)

    def visit_AddNode(self, node):
        return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)

    def visit_SubtractNode(self, node):
        return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

    def visit_MultiplyNode(self, node):
        return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)

    def visit_DivideNode(self, node):
        try:
            return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
        except:
            raise Exception("Runtime math error")

    def visit_PowerNode(self, node):
        return Number(math.pow(self.visit(node.node_a).value, self.visit(node.node_b).value))

    def visit_RadicalNode(self, node):
        return Number(math.sqrt(self.visit(node.node).value))

    def visit_LogNode(self, node):
        return Number(math.log(self.visit(node.node).value))

    def visit_SinNode(self, node):
        return Number(math.sin(self.visit(node.node).value))

    def visit_CosNode(self, node):
        return Number(math.cos(self.visit(node.node).value))

    def visit_TanNode(self, node):
        return Number(math.tan(self.visit(node.node).value))


