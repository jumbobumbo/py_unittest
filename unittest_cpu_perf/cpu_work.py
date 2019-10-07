from random import randint
import time
from pathlib import Path


class WorkCPU:

    @staticmethod
    def two_lists():
        with open(Path("output", str(str(time.time()) + "_equal_log.txt")), "w") as f:
            for x, y in zip([randint(0, 6) for i in range(0, 20000)], [randint(4, 9) for i in range(0, 20000)]):
                if x - y == 0:
                    f.write(f"{x}\n")
