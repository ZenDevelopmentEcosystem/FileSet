Feature: Config Command

Scenario: Validate config
    Given fileset
    And timeout 5 seconds
    And Environment variable `FILESET_CONFIG=./test_data/.fileset.yml`
    When fileset run with argument(s) `config --quiet --set ./test_data/FileSet.yml`
    Then exit code 0
    And no output

Scenario: Print applied config, no valid set-file
    Given fileset
    And timeout 5 seconds
    And Environment variable `FILESET_CONFIG=./test_data/.fileset.yml`
    When fileset run with argument(s) `config`
    Then exit code 0
    And content of YAML file './test_data/.fileset.yml' is in output

Scenario: Print applied config, with valid set-file
    Given fileset
    And timeout 5 seconds
    And Environment variable `FILESET_CONFIG=./test_data/.fileset.yml`
    When fileset run with argument(s) `config --set ./test_data/FileSet.yml`
    Then exit code 0
    And content of YAML file './test_data/.fileset.yml' is in output

Scenario: Print set file, default
    Given fileset
    And timeout 5 seconds
    And Environment variable `FILESET_CONFIG=./test_data/.fileset.yml`
    When fileset run with argument(s) `config --set-file`
    Then exit code 0
    And output contains 'FileSet.yml'
    And output does not contain 'test_data'

Scenario: Print set file, with set file specified
    Given fileset
    And timeout 5 seconds
    And Environment variable `FILESET_CONFIG=./test_data/.fileset.yml`
    When fileset run with argument(s) `config --set-file --set ./test_data/FileSet.yml`
    Then exit code 0
    And output contains '/test_data/FileSet.yml'

Scenario: Print config file, default
    Given fileset
    And timeout 5 seconds
    When fileset run with argument(s) `config --config-file`
    Then exit code 0
    And output contains '/home/.*/.fileset.yml'

Scenario: Print config file, set via environment variable
    Given fileset
    And timeout 5 seconds
    And Environment variable `FILESET_CONFIG=./test_data/.fileset.yml`
    When fileset run with argument(s) `config --config-file`
    Then exit code 0
    And output contains '/test_data/.fileset.yml'

Scenario: Print sets as paths
    Given fileset
    And timeout 5 seconds
    And Environment variable `FILESET_CONFIG=./test_data/.fileset.yml`
    When fileset run with argument(s) `config --set-paths --set ./test_data/FileSet.yml`
    Then exit code 0
    And output contains '^all/a/1$'

Scenario: Print assets as paths
    Given fileset
    And timeout 5 seconds
    And Environment variable `FILESET_CONFIG=./test_data/.fileset.yml`
    When fileset run with argument(s) `config --asset-paths --set ./test_data/FileSet.yml`
    Then exit code 0
    And output contains '^all/a/1$'
    And output does not contain '^all/a$'
