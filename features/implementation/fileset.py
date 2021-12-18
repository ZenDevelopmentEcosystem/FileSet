import shlex
import sys

from pytest_bdd import given, parsers, when


@given('fileset', target_fixture='fileset_cmd')
def setup_fileset(fileset_path):
    python_path = sys.executable
    return [python_path, fileset_path]


@when(parsers.parse('fileset run with argument(s) `{args}`'), target_fixture='proc_status')
def fileset_run_with_argument(args, timeout, fileset_cmd, run_shell):
    fileset_cmd.extend(shlex.split(args))
    return run_shell(fileset_cmd, timeout)
