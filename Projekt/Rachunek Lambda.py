true  = lambda t: lambda f: t
false = lambda t: lambda f: f

to_python_bool = lambda church_bool: church_bool(True)(False)
from_python_bool = lambda b: true if b else false

NOT = lambda b: b(false)(true)
AND = lambda p: lambda q: p(q)(false)
OR  = lambda p: lambda q: p(true)(q)
XOR = lambda p: lambda q: p(q(false)(true))(q)
IF = lambda cond: lambda then_branch: lambda else_branch: cond(then_branch)(else_branch)


def evaluate(expr):
    if isinstance(expr, bool):
        return from_python_bool(expr)
    op, *args = expr
    church_args = list(map(evaluate, args))

    match op:
        case 'not':
            return NOT(church_args[0])
        case 'and':
            return AND(church_args[0])(church_args[1])
        case 'or':
            return OR(church_args[0])(church_args[1])
        case 'xor':
            return XOR(church_args[0])(church_args[1])
        case 'if':
            return IF(church_args[0])(church_args[1])(church_args[2])
        case _:
            raise ValueError(f"Unknown operation: {op}")


if __name__ == "__main__":
    test_cases = [
        ('not true', NOT(true)),
        ('not false', NOT(false)),
        ('and true false', AND(true)(false)),
        ('and true true', AND(true)(true)),
        ('or false false', OR(false)(false)),
        ('or true false', OR(true)(false)),
        ('xor true true', XOR(true)(true)),
        ('xor true false', XOR(true)(false)),
        ("if true then true else false", IF(true)(true)(false)),
        ("if false then true else false", IF(false)(true)(false)),
        ("evaluate: ('and', ('not', True), False)", evaluate(('and', ('not', True), False))),
        ("evaluate: ('if', ('or', True, False), False, True)", evaluate(('if', ('or', True, False), False, True)))
    ]
    for description, result in test_cases:
        print(f"{description} => {to_python_bool(result)}")