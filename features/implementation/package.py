import os
import sys

from pytest_bdd import given, then, when


@given('wheel-package', target_fixture='package_path')
def wheel_package_path(wheel_package_path):
    return wheel_package_path


@given('sdist-package', target_fixture='package_path')
def sdist_package_path(sdist_package_path):
    return sdist_package_path


@given('venv', target_fixture='venv_dir')
def create_venv(tmpdir, run_shell):
    venv_dir = tmpdir.join('venv')
    python_path = sys.executable
    venv_cmd = [python_path, '-m', 'venv', str(venv_dir)]
    result = run_shell(venv_cmd, 10)
    assert result.exitcode == 0, result.output()
    return venv_dir


@when('install in venv', target_fixture='proc_status')
def install_in_venv(run_shell, venv_dir, timeout, package_path):
    pip = os.path.join(venv_dir, 'bin', 'pip')
    venv_cmd = [pip, 'install', package_path]
    return run_shell(venv_cmd, timeout)


@then('fileset entry-point exists')
def check_fileset_entrypoint(local, venv_dir):
    entrypoint = os.path.join(venv_dir, 'bin', 'fileset')
    local.file(entrypoint).exists
