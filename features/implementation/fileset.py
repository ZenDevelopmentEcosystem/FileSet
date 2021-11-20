from pytest_bdd import given, parsers, then, when


@given('fileset')
def prepare_fileset():
    pass


@when(parsers.parse('run with argument(s) {args}'))
def do_run_with_argument(args):
    pass


@then(parsers.parse('exit code {exit_code}'))
def check_exit_code(exit_code):
    pass


@then(parsers.parse('output contains {expression}'))
def check_output(expression):
    pass
