import os
import shlex
import sys

from pytest_bdd import given, parsers, then, when


@given('fileset', target_fixture='fileset_cmd')
def setup_fileset(fileset_path):
    python_path = sys.executable
    return [python_path, fileset_path]


@given(parsers.parse('Environment variable `{variable}={value}`'), target_fixture='environment')
def set_environment(environment, variable, value):
    result = environment.copy()
    result[variable] = value
    return result


@when(parsers.parse('fileset run with argument(s) `{args}`'), target_fixture='proc_status')
def fileset_run_with_argument(args, timeout, fileset_cmd, run_shell):
    fileset_cmd.extend(shlex.split(args))
    return run_shell(fileset_cmd, timeout)


@then(parsers.parse("content of YAML file '{yaml_file}' is in output"))
def check_yaml_file_content_in_output(yaml_file, working_directory, proc_status):
    yaml_file = os.path.join(working_directory, yaml_file)
    with open(yaml_file, 'r') as f:
        yaml_content = f.read().replace('---\n', '').strip()
    msg = f'Expected content of YAML file {yaml_file}:\n{yaml_content}\n to be in:\n{proc_status.output()}'
    assert yaml_content in proc_status.output(), msg
