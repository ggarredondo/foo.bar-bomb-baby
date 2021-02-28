from collections import deque


class Node:
    def __init__(self, mach, facula, generation):
        self.mach = mach
        self.facula = facula
        self.generation = generation

    def left_child(self):
        return Node(self.mach, self.mach+self.facula, self.generation+1)

    def right_child(self):
        return Node(self.mach+self.facula, self.facula, self.generation+1)

    def n_mach(self):
        return self.mach

    def n_facula(self):
        return self.facula

    def get_generation(self):
        return self.generation

    def empty(self):
        return self.mach==0 and self.facula==0 and self.generation==0


def solution(mach, facula):
    imach = int(mach)
    ifacula = int(facula)
    root = Node(1, 1, 0)
    optimal = Node(0, 0, 0)
    stack = deque([root])

    equal = imach == ifacula and imach > 1
    zero = imach == 0 or ifacula == 0
    while len(stack) > 0 and optimal.empty() and not equal and not zero:
        current = stack.popleft()
        if current.n_mach() == imach and current.n_facula() == ifacula:
            optimal = current
        elif current.n_mach() <= imach and current.n_facula() <= ifacula:
            stack.append(current.left_child())
            stack.append(current.right_child())

    result = "impossible"
    if not optimal.empty():
        result = str(optimal.get_generation())

    return result