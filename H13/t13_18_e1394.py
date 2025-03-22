def ts(expr):
    tokens = []
    i = 0
    while i < len(expr):
        if expr[i].isdigit():
            num = ""
            while i < len(expr) and expr[i].isdigit():
                num += expr[i]
                i += 1
            tokens.append(num)
        else:
            tokens.append(expr[i])
            i += 1
    return tokens

def do_op(a, op, b):
    if op == '+':
        res = a + b
    elif op == '-':
        res = a - b
    elif op == '*':
        res = a * b
    elif op == '/':
        if b == 0:
            raise Exception
        res = a // b
    if res < 0 or len(str(res)) > 90:
        raise Exception
    return res

def calc(expr):
    expr = "".join(expr.split())
    tokens = ts(expr)
    vals = []
    ops = []
    prec = {'+': 1, '-': 1, '*': 2, '/': 2}
    i = 0
    while i < len(tokens):
        t = tokens[i]
        if t.isdigit():
            if len(t) > 90:
                raise Exception
            vals.append(int(t))
        elif t == '(':
            ops.append(t)
        elif t == ')':
            while ops and ops[-1] != '(':
                op = ops.pop()
                b = vals.pop()
                a = vals.pop()
                vals.append(do_op(a, op, b))
            if ops:
                ops.pop()
        else:
            while ops and ops[-1] != '(' and prec[ops[-1]] >= prec[t]:
                op = ops.pop()
                b = vals.pop()
                a = vals.pop()
                vals.append(do_op(a, op, b))
            ops.append(t)
        i += 1
    while ops:
        op = ops.pop()
        b = vals.pop()
        a = vals.pop()
        vals.append(do_op(a, op, b))
    return vals[0]

def extr(s):
    exprs = []
    i = 0
    while i < len(s):
        if s[i] in " \t\n":
            i += 1
            continue
        if s[i].isdigit():
            j = i
            while j < len(s) and s[j].isdigit():
                j += 1
            exprs.append(s[i:j])
            i = j
        elif s[i] == '(':
            cnt = 0
            j = i
            while j < len(s):
                if s[j] == '(':
                    cnt += 1
                elif s[j] == ')':
                    cnt -= 1
                j += 1
                if cnt == 0:
                    break
            exprs.append(s[i:j])
            i = j
        else:
            i += 1
    return exprs


all_input = ""
try:
    while True:
        line = input()
        all_input += line + " "
except EOFError:
    pass
exprs = extr(all_input)
results = []
for e in exprs:
    try:
        res = calc(e)
        results.append(str(res))
    except Exception:
        results.append("Error")
for r in results:
    print(r)