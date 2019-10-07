import unittest
from parameterized import parameterized
import psutil
import threading
from cpu_work import WorkCPU as WC


class Asserter:

    @staticmethod
    def assert_less(self, current, maximum):
        """
        asserts current is below maximum
        self: unittestObject
        current: int/float
        maximum: int/float
        """
        self.assertLess(current, maximum, f"{current}% cpu usage is higher than max val: {maximum}")


class TestCpu(unittest.TestCase):
    """ Various tests regarding the host systems CPU """

    def test_cpu_before_compute(self):
        """ should fail if the machine is idling at 5 + % """
        Asserter.assert_less(self, psutil.cpu_percent(), 20)

    @parameterized.expand([
        (50, ),
        (25, ),
    ])
    def test_cpu_load_after_compute(self, max_util):
        """ tests cpu usage after heavy lifting """
        WC.two_lists()
        Asserter.assert_less(self, psutil.cpu_percent(), max_util)

    @parameterized.expand([
        (60,),
        (40,),
        (30,),
    ])
    def test_cpu_during_compute(self, max_util):
        """ verify cpu usage isn't above stated values during compute """
        w = threading.Thread(name="lists_gen", target=WC.two_lists())
        t = threading.Thread(name="cpu_assert", target=Asserter.assert_less(self, psutil.cpu_percent(), max_util))
        w.start()
        t.start()
        w.join()
        t.join()
