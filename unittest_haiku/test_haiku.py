from haiku import HaikuValidation as Haiku
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
        """ verifies Assertion error is raised when string of 200+ chars is submitted """
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


class TestReturnValueIsHaiku(unittest.TestCase):
    """ inputs and the expected returned values """
    @parameterized.expand([
        ([5, 7, 5], "yes"),
        ([2, 1, 1], "no"),
        ("string", "no"),
        (12345, "no"),
    ])
    def test_haiku_return_value(self, input_val, expected_return):
        """ tests if 'yes' or 'no' return values are as expected """
        self.assertEqual(Haiku.is_haiku(input_val), expected_return)


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
