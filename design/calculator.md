## Q
Implement a basic calculator, supporting operators such as +, -, *, / and operands like ( and ).

For example:
`"(1+2) *10 -25/(1-7)" -> 34`

## A
I think that maybe there is an error in the example above. The expression should be : (1+2)*10-24/(1-7) -> 34
Here is some implementation, convert infix notation in reverse pollish notation and calculate it
``` python
import collections

def is_digit(ch):
    return ch >= '0' and ch <= '9'

def calc(op2, op1, ch):
    if ch == '-':
        return op1 - op2
    elif ch == '+':
        return op1 + op2
    elif ch == '/':
        return op1 / op2
    elif ch == '*':
        return op1 * op2
    else:
        return 0

def higher_priority(op1, op2):
    if op1 == '*' or op1 == '/':
        return True
    if op2 == '+' or op2 == '-':
        return True
    return False

def simple_calculator(exp):
    st = collections.deque()
    op = collections.deque()
    digit = 0
    has_digit = False
    for i in range(len(exp)):
        if is_digit(exp[i]):
            has_digit = True
            digit = digit * 10 + int(exp[i])
        else:
            if has_digit:
                has_digit = False
                st.append(digit)
                digit = 0
            if exp[i] == '(':
                op.append('(')
            elif exp[i] == ')':
                while op[-1] != '(':
                    st.append(calc(st.pop(), st.pop(), op.pop()))
                op.pop()
            else:
                while op and op[-1] != '(' and higher_priority(op[-1], exp[i]):
                    st.append(calc(st.pop(), st.pop(), op.pop()))
                op.append(exp[i])
    if has_digit:
        st.append(digit)
    while op:
        st.append(calc(st.pop(), st.pop(), op.pop()))
    return st[-1]

```
