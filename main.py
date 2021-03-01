import solution
import random


def gen_test():
    M = random.randint(1, 8)
    F = random.randint(1, 8)
    print ("Objective: " + str(M) + "M " + str(F) + "F")
    return M, F


def main():
    print(solution.solution('2', '4'))


if __name__ == '__main__':
    main()