from typing import TypeVar, Generic, List

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.__container: List[T] = []

    def push(self, item: T) -> None:
        self.__container.append(item)

    def pop(self) -> T:
        return self.__container.pop()

    def __repr__(self) -> str:
        return repr(self.__container)

def setup_hanoi():
    return Stack(), Stack(), Stack(), 3

def solve_hanoi(begin, end, temp, num_discs) -> None:
    if num_discs == 1:
        end.push(begin.pop())

    else:
        solve_hanoi(begin, temp, end, num_discs - 1)
        solve_hanoi(begin, end, temp, 1)
        solve_hanoi(temp, end, begin, num_discs - 1)

if __name__ == '__main__':
    begin, end, temp, num_discs = setup_hanoi()
    for i in range(1, num_discs + 1):
        begin.push(i)
    solve_hanoi(begin, end, temp, num_discs)
    print(begin)
    print(temp)
    print(end)