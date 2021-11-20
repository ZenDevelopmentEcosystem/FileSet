import os
import re
import shlex
import sys
from subprocess import PIPE, Popen, TimeoutExpired

from pytest_bdd import given, parsers, then, when


class ProcStatus:

    def __init__(self, stdout, stderr, exitcode):
        self.stdout = stdout
        self.stderr = stderr
        self.exitcode = exitcode

    def output(self):
        return f'{self.stdout}{os.linesep}{self.stderr}'


@given('fileset', target_fixture='fileset_cmd')
def setup_fileset(fileset_path):
    python_path = sys.executable
    return [python_path, fileset_path]


@given(parsers.parse('timeout {timeout:d} seconds'), target_fixture='timeout')
def setup_timeout(timeout):
    return timeout


@when(parsers.parse('run with argument(s) `{args}`'), target_fixture='fileset_status')
def do_run_with_argument(args, timeout, fileset_cmd):
    fileset_cmd.extend(shlex.split(args))
    with Popen(fileset_cmd, stdout=PIPE, stderr=PIPE, encoding='utf8', text=True) as proc:
        try:
            stdout, stderr = proc.communicate(timeout=timeout)
        except TimeoutExpired:
            proc.kill()
            stdout, stderr = proc.communicate()
    return ProcStatus(stdout, stderr, proc.returncode)


@then(parsers.parse('exit code {exit_code:d}'))
def check_exit_code(exit_code, fileset_status):
    assert fileset_status.exitcode == exit_code, fileset_status.output()


@then(parsers.parse("output contains '{expression}'"))
def check_output(expression, fileset_status):
    assert re.match(expression, fileset_status.stdout), fileset_status.stdout
