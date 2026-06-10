OPERATORS = {'+', '-', '*', '/'}


def make_node(value, left=None, right=None):
    return {'value': value, 'left': left, 'right': right}


def is_leaf(node):
    return node['left'] is None and node['right'] is None


def build_expression_tree(tokens):
    stack = []
    for token in tokens:
        if token in OPERATORS:
            right = stack.pop()
            left = stack.pop()
            stack.append(make_node(token, left, right))
        else:
            stack.append(make_node(int(token)))
    return stack[0]


def evaluate(node):
    if is_leaf(node):
        return node['value']

    left_val = evaluate(node['left'])
    right_val = evaluate(node['right'])

    match node['value']:
        case '+': return left_val + right_val
        case '-': return left_val - right_val
        case '*': return left_val * right_val
        case '/': return left_val / right_val


def fold_constants(node):
    if is_leaf(node):
        return node

    folded_left = fold_constants(node['left'])
    folded_right = fold_constants(node['right'])
    new_node = make_node(node['value'], folded_left, folded_right)

    if is_leaf(folded_left) and is_leaf(folded_right):
        return make_node(evaluate(new_node))

    return new_node


def print_tree(node, prefix='', is_left=True):
    if node is None:
        return

    connector = '├── ' if is_left else '└── '
    print(prefix + connector + str(node['value']))
    if not is_leaf(node):
        print_tree(node['left'], prefix + ('│   ' if is_left else '    '), True)
        print_tree(node['right'], prefix + ('│   ' if is_left else '    '), False)


if __name__ == '__main__':
    expressions = [
        '2 5 * 3 +',
        '2 3 + 4 5 * +',
        '10 2 8 * + 3 -',
    ]

    for expr in expressions:
        tokens = expr.split()
        print(f'Выражение: {expr}')

        tree = build_expression_tree(tokens)
        print('Дерево:')
        print_tree(tree)

        result = evaluate(tree)
        print(f'Результат: {result}')

        folded = fold_constants(tree)
        print(f'После constant folding: {folded["value"]}')
        print()
