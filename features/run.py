import os
from subprocess import PIPE, Popen, TimeoutExpired

import pytest


class ProcStatus:

    def __init__(self, stdout, stderr, exitcode):
        self.stdout = stdout
        self.stderr = stderr
        self.exitcode = exitcode

    def output(self):
        return f'{self.stdout}{os.linesep}{self.stderr}'


@pytest.fixture()
def run_shell():

    def run(command_args, timeout):
        with Popen(command_args, stdout=PIPE, stderr=PIPE, encoding='utf8', text=True) as proc:
            try:
                stdout, stderr = proc.communicate(timeout=timeout)
            except TimeoutExpired:
                proc.kill()
                stdout, stderr = proc.communicate()
        return ProcStatus(stdout, stderr, proc.returncode)

    return run
