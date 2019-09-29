from unittest_haiku.haiku import HaikuValidation as Haiku
import unittest
from parameterized import parameterized


class TestHaikuInputValidation(unittest.TestCase):
    """ inputs that are not the right type, lines, char or case """
    @parameterized.expand([
        (56, ),
        "test/0/yes",
        "1234",
        "HI/THERE/TEST",
        "not/enough",
        "this / that / t / t",
    ])
    def test_input_validation(self, value):
        """ verifies the input validation raises an Assertion error when incorrect input is supplied """
        haiku = Haiku(value)
        with self.assertRaises(AssertionError):
            haiku.input_validation()

    def test_input_too_long(self):
        """ verifies Assertion error is raised when string over 200 chars is submitted """
        long_str = "".join("a" for i in range(0, 201))  # 200 char string
        haiku = Haiku(long_str)
        with self.assertRaises(AssertionError):
            haiku.input_validation()


class TestHaikuReturnSyllables(unittest.TestCase):
    """ inputs and the expected returned values """
    @parameterized.expand([
        ("man/mine/mean", [1, 2, 1]),
        ("time/team/green", [2, 1, 1]),
        ("tan time/fine wine", [3, 4]),
    ])
    def test_syllable_return_values(self, string, syllables):
        """ verfies the expected number of syllables of an input str is returned """
        haiku = Haiku(string)
        self.assertEqual(haiku.return_syllables(), syllables)


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
