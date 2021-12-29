import os
from subprocess import PIPE, Popen, TimeoutExpired

import pytest


class ProcStatus:

    def __init__(self, stdout, stderr, exitcode):
        self.stdout = stdout
        self.stderr = stderr
        self.exitcode = exitcode

    def output(self):
        return f'{self.stdout}{os.linesep}{self.stderr}'.strip()


@pytest.fixture()
def run_shell(working_directory, environment):

    def run(command_args, timeout):
        with Popen(command_args, env=environment, cwd=working_directory, stdout=PIPE, stderr=PIPE, encoding='utf8',
                   text=True) as proc:
            try:
                stdout, stderr = proc.communicate(timeout=timeout)
            except TimeoutExpired:
                proc.kill()
                stdout, stderr = proc.communicate()
        return ProcStatus(stdout, stderr, proc.returncode)

    return run


@pytest.fixture()
def working_directory():
    return os.path.dirname(os.path.abspath(__file__))


@pytest.fixture()
def environment():
    return os.environ.copy()
