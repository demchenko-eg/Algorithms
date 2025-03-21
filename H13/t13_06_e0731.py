class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.op = value if value in {'+', '-', '*', '/'} else None
        self.prec = {'+': 1, '-': 1, '*': 2, '/': 2}.get(value, 100)

def parse(prefix):
    prec = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []
    for token in reversed(prefix):
        if token in prec:
            left = stack.pop()
            right = stack.pop()
            stack.append(Node(token, left, right))
        else:
            stack.append(Node(token))
    return stack.pop()

def to_infix(node, parent_op=None, is_right=False):
    prec = {'+': 1, '-': 1, '*': 2, '/': 2}
    if node.op is None:
        return node.value
    left_expr = to_infix(node.left, node.value, False)
    right_expr = to_infix(node.right, node.value, True)
    expr = left_expr + node.value + right_expr
    if parent_op is not None:
        if node.prec < prec[parent_op]:
            expr = "(" + expr + ")"
        elif node.prec == prec[parent_op] and is_right and parent_op in "-/":
            expr = "(" + expr + ")"
    return expr

def dfg(prefix: str) -> str:
    root = parse(prefix)
    return to_infix(root)
prefix_expr = input().strip()
print(dfg(prefix_expr))