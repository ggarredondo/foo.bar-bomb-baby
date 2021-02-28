

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


optimal = Node(0, 0, 2**31 - 1)

def backtracking(mach, facula, node):
    left = node.left_child()
    right = node.right_child()
    stack = [left, right]
    global optimal

    if node.n_mach() == mach and node.n_facula() == facula:
        optimal = node
    else:
        while len(stack) > 0:
            if stack[0].n_mach() <= mach and stack[0].n_facula() <= facula and stack[0].get_generation() < optimal.get_generation():
                backtracking(mach, facula, stack[0])
            stack.pop(0)


def solution(mach, facula):
    root = Node(1, 1, 0)
    backtracking(int(mach), int(facula), root)
    result = "impossible"
    if optimal.n_mach() != 0:
        result = str(optimal.get_generation())

    return result