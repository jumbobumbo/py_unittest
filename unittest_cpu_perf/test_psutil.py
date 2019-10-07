import unittest
from parameterized import parameterized
import psutil
from cpu_work import WorkCPU as WC


class TestCpu(unittest.TestCase):
    """ Various tests regarding the host systems CPU """
    @parameterized.expand([
        (50, ),
        (20, ),
    ])
    def test_cpu_load_after_compute(self, max_util):
        WC.two_lists()
        cpu_usage = psutil.cpu_percent()
        self.assertLess(cpu_usage, max_util, f"{cpu_usage}% cpu usage is too high")
