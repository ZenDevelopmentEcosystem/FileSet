Feature: Version

Scenario: Print version
    Given fileset
    And timeout 5 seconds
    When fileset run with argument(s) `--version`
    Then exit code 0
    And output contains 'fileset, version [\d.\d.\d]'
