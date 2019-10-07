from random import randint


class WorkCPU:

    @staticmethod
    def two_lists():
        for x, y in zip([randint(0, 5) for i in range(0, 20000)], [randint(5, 9) for i in range(0, 20000)]):
            if x - y == 0:
                print("equal")
            else:
                print("not equal")
