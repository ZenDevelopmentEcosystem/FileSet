Feature: fileset

fileset is a command-line utility and python library for working with file-sets.

Scenario: Print top help (long)
    Given fileset
    And timeout 5 seconds
    When fileset run with argument(s) `--help`
    Then exit code 0
    And output contains 'Usage'

Scenario: Print top help (short)
    Given fileset
    And timeout 5 seconds
    When fileset run with argument(s) `-h`
    Then exit code 0
    And output contains 'Usage'

Scenario: Print version
    Given fileset
    And timeout 5 seconds
    When fileset run with argument(s) `--version`
    Then exit code 0
    And output contains 'fileset, version [\d.\d.\d]'
