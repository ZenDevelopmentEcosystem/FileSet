import re

from pytest_bdd import parsers, then


@then(parsers.parse('exit code {exit_code:d}'))
def check_exit_code(exit_code, proc_status):
    assert proc_status.exitcode == exit_code, proc_status.output()


@then('no output')
def check_no_output(proc_status):
    assert proc_status.output() == '', proc_status.output()


@then(parsers.parse("output contains '{expression}'"))
def check_output(expression, proc_status):
    msg = f"Searched for expression '{expression}' in:\n {proc_status.stdout}"
    assert re.search(expression, proc_status.stdout, re.MULTILINE), msg


# output does not contain 'test_data'
@then(parsers.parse("output does not contain '{expression}'"))
def check_not_in_output(expression, proc_status):
    msg = f"Searched for expression '{expression}' to ensure not in:\n {proc_status.stdout}"
    assert not re.search(expression, proc_status.stdout, re.MULTILINE), msg
