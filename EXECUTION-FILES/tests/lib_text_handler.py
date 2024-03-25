import unittest
import pytest
from gradescope_utils.autograder_utils.decorators import (
    weight,
    visibility,
    partial_credit,
    number,
)

import subprocess
import os

if "PY_VERSION" in os.environ:
    PY_VERSION = os.environ["PY_VERSION"]
else:
    PY_VERSION = "3"

PY_COMMAND = "python" + PY_VERSION


class TestText(unittest.TestCase):
    _file_name = ""
    _sample_input = ""

    def setUp(self) -> None:
        """
        Override this method to set the file name and
        sample input

        Set these to suitable values in your redefinition
        of this method:

        self._file_name :
            the name of the file
        self._sample_input :
            a string of inputs to be passed to the program
            that should make it run without crashing

        """
        pass

    @number("0")
    def test_if_runs(self):
        """
        Test if the program can run without crashing

        """
        if self._file_name != "":
            try:
                result = subprocess.run(
                    [PY_COMMAND, self._file_name],
                    input=self._sample_input,
                    text=True,
                    capture_output=True,
                )

            except Exception as e:
                # Overwrite the test docstring to include file name in student's view
                self._testMethodDoc = "Cannot run program %s" % self._file_name
                self.fail(f"Program {self._file_name} crashed with error:\n\n{e}")
            finally:
                # Overwrite the test docstring to include file name
                self._testMethodDoc = (
                    "Program %s runs without crashing" % self._file_name
                )
                if result.returncode == 0:
                    self.assertTrue(result.returncode == 0)
                else:
                    # return original error msg from program
                    self.fail(
                        f"Program {self._file_name} crashed with error:\n\n{result.stderr}"
                    )
        else:
            self.skipTest("No file name provided")

    def run_subprocess(self, inputs: str) -> str:
        """
        Run the program as a subprocess with the given inputs, and return the output if successful

        Call as helper function in other tests

        """
        try:
            result = subprocess.run(
                [PY_COMMAND, self._file_name],
                input=inputs,
                text=True,
                capture_output=True,
                timeout=5,
            )
        except Exception as e:
            self.fail(f"Program {self._file_name} crashed with error:\n\n{e}")
        else:
            if result.returncode == 0:
                return result.stdout
            else:
                self.fail(
                    f"Program {self._file_name} crashed with error:\n\n{result.stderr}"
                )
