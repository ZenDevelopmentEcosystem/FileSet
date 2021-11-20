from os import environ

from pytest_bdd import scenarios

scenarios(environ.get('FEATURES', './scenarios'))
