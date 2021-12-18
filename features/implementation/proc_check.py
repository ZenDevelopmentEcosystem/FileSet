import re

from pytest_bdd import parsers, then


@then(parsers.parse('exit code {exit_code:d}'))
def check_exit_code(exit_code, proc_status):
    assert proc_status.exitcode == exit_code, proc_status.output()


@then(parsers.parse("output contains '{expression}'"))
def check_output(expression, proc_status):
    assert re.search(expression, proc_status.stdout), proc_status.stdout
