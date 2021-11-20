Feature: fileset

fileset is a command-line utility and python library for working with file-sets.

Scenario: Listing top help (long)
    Given fileset
    When run with argument(s) `--help`
    Then exit code 0
#    And output contains 'Usage'

# Scenario: Listing top help (short)
#     Given fileset
#     When run with argument `--help`
#     Then exit code 0
#     And output contains 'Usage'
