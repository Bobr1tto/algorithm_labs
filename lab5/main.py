OPERATORS = set("+-*/")


class ExpressionNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def is_operator(self):
        return self.value in OPERATORS

    def is_leaf(self):
        return self.left is None and self.right is None


def build_expression_tree(tokens):
    stack = []
    for token in tokens:
        if token in OPERATORS:
            node = ExpressionNode(token)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
        else:
            stack.append(ExpressionNode(int(token)))
    return stack[-1]


def evaluate(root):
    if not root.is_operator():
        return root.value
    left = evaluate(root.left)
    right = evaluate(root.right)
    match root.value:
        case "+": return left + right
        case "-": return left - right
        case "*": return left * right
        case "/": return left / right


def constant_folding(root):
    if not root.is_operator():
        return root
    root.left = constant_folding(root.left)
    root.right = constant_folding(root.right)
    if root.left.is_leaf() and root.right.is_leaf():
        result = evaluate(root)
        return ExpressionNode(int(result) if result == int(result) else result)
    return root


def print_tree(node, prefix="", is_left=True):
    if node is None:
        return
    print(prefix + ("├── " if is_left else "└── ") + str(node.value))
    indent = prefix + ("│   " if is_left else "    ")
    print_tree(node.left, indent, True)
    print_tree(node.right, indent, False)


def demo(expression):
    print(f"Постфикс: {expression}")
    tokens = expression.split()
    root = build_expression_tree(tokens)
    print_tree(root, is_left=False)
    print(f"Результат: {evaluate(root)}")
    folded = constant_folding(build_expression_tree(tokens))
    print(f"После folding: {folded.value}\n")


if __name__ == "__main__":
    demo("2 5 * 3 +")
    demo("2 3 + 4 5 * +")
    demo("10 2 8 * + 3 -")
