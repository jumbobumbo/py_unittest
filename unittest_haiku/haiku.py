class HaikuValidation:

    def __init__(self, haiku):
        self.haiku = haiku
        self.char = ""

    def input_validation(self):
        """
        checks if the input is of the right len, lines, char or case
        haiku will always come through from cucumber as a str
        this does not check if its a Haiku
        """
        if type != str:
            raise AssertionError("type must be a string")  # value is not a str type (just in case not using cucumber)
        if len(self.haiku) > 200:  # too many characters
            raise AssertionError("input too long, not a Haiku")
        if len(self.haiku.split("/")) != 3:  # not enough lines
            raise AssertionError(f"{len(self.haiku.split('/'))} lines is incorrect, must be 3")
        if any(self.char.isdigit() for self.char in self.haiku):  # contains a digit
            raise AssertionError(f"{self.char} is a digit, not allowed in a Haiku")
        if any(self.char.isupper() for self.char in self.haiku):  # contains an upper case letter
            raise AssertionError(f"Cannot contain CAPs ({self.char}), failing")

    def return_syllables(self):
        """ verifies if input string is actually a haiku """
        vowels = ["a", "e", "i", "o", "u", "y"]
        # split the string into its lines
        lines = self.haiku.split("/")
        # iterate over each line
        results = []
        for line in lines:
            syllables = 0
            words = line.split()
            # iterate over each word from the current line
            for word in words:
                for i, l in enumerate(word):  # index, letter
                    if l in vowels:
                        # check we aren't at the end of the list. Also check if the next letter is a vowel.
                        if i != (len(word) - 1) and word[i + 1] in vowels:
                            continue  # don't add 1 to total, next loop round will cover that.
                        syllables += 1
            results.append(syllables)
        return results  # return total list of results

    @staticmethod
    def is_haiku(count):
        """
        check if the counted syllables are correct
        count: list of ints """
        if count == [5, 7, 5]:
            return "yes"
        else:
            return "no"
