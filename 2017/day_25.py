from collections import defaultdict
from typing import Dict, Tuple


# In state A:
#   If the current value is 0:
#     - Write the value 1.
#     - Move one slot to the right.
#     - Continue with state B.
#   If the current value is 1:
#     - Write the value 0.
#     - Move one slot to the left.
#     - Continue with state C.
def a(tape: Dict[int, bool], cursor: int) -> Tuple[int, str]:
    value = tape[cursor]
    if not value:
        tape[cursor] = True
        return cursor + 1, 'B'
    tape[cursor] = False
    return cursor - 1, 'C'


# In state B:
#   If the current value is 0:
#     - Write the value 1.
#     - Move one slot to the left.
#     - Continue with state A.
#   If the current value is 1:
#     - Write the value 1.
#     - Move one slot to the left.
#     - Continue with state D.
def b(tape: Dict[int, bool], cursor: int) -> Tuple[int, str]:
    value = tape[cursor]
    if not value:
        tape[cursor] = True
        return cursor - 1, 'A'
    tape[cursor] = True
    return cursor - 1, 'D'


# In state C:
#   If the current value is 0:
#     - Write the value 1.
#     - Move one slot to the right.
#     - Continue with state D.
#   If the current value is 1:
#     - Write the value 0.
#     - Move one slot to the right.
#     - Continue with state C.
def c(tape: Dict[int, bool], cursor: int) -> Tuple[int, str]:
    value = tape[cursor]
    if not value:
        tape[cursor] = True
        return cursor + 1, 'D'
    tape[cursor] = False
    return cursor + 1, 'C'


# In state D:
#   If the current value is 0:
#     - Write the value 0.
#     - Move one slot to the left.
#     - Continue with state B.
#   If the current value is 1:
#     - Write the value 0.
#     - Move one slot to the right.
#     - Continue with state E.
def d(tape: Dict[int, bool], cursor: int) -> Tuple[int, str]:
    value = tape[cursor]
    if not value:
        tape[cursor] = False
        return cursor - 1, 'B'
    tape[cursor] = False
    return cursor + 1, 'E'


# In state E:
#   If the current value is 0:
#     - Write the value 1.
#     - Move one slot to the right.
#     - Continue with state C.
#   If the current value is 1:
#     - Write the value 1.
#     - Move one slot to the left.
#     - Continue with state F.
def e(tape: Dict[int, bool], cursor: int) -> Tuple[int, str]:
    value = tape[cursor]
    if not value:
        tape[cursor] = True
        return cursor + 1, 'C'
    tape[cursor] = True
    return cursor - 1, 'F'


# In state F:
#   If the current value is 0:
#     - Write the value 1.
#     - Move one slot to the left.
#     - Continue with state E.
#   If the current value is 1:
#     - Write the value 1.
#     - Move one slot to the right.
#     - Continue with state A.
def f(tape: Dict[int, bool], cursor: int) -> Tuple[int, str]:
    value = tape[cursor]
    if not value:
        tape[cursor] = True
        return cursor - 1, 'E'
    tape[cursor] = True
    return cursor + 1, 'A'


STATES = dict(A=a,
              B=b,
              C=c,
              D=d,
              E=e,
              F=f)


def run_1():
    tape = defaultdict(bool)
    cursor = 0
    state = 'A'
    for _ in range(12172063):
        cursor, state = STATES[state](tape, cursor)
    return len([x for x in tape.values() if x])


print(run_1())
