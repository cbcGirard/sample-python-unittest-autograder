from lib_text_handler import TestText
from gradescope_utils.autograder_utils.decorators import number, weight

class TestHello(TestText):
    def setUp(self) -> None:
        self._file_name = "hello.py"
        self._sample_input = "$NAME$\n"

    @number("5")
    @weight(5)
    def test_text(self):
        """ Test if greeter greets correctly"""
        output = self.run_subprocess("$NAME$")
        self.assertIn("Hello, $NAME$!", output)