Run Command
===========

Executes a command on the files scoped by the set.

Example:

```console
fileset <store> run <cmd> path/in/set ... -- args-to-cmd
```

The command is defined in a FileSet.yml config as:

```yaml
runs:
    <run-name>:
        command: command to invoke ${files}
        for-each-file: -f ${file}
```

Defaults
: If `${files}` is not part of the `command`, the files are appended at the end.
: If `${file}` is not part of `for-each-file` it is appended at the end.
: If `for-each-file` is not specified, it defaults to `${file}` which expands
  to a list of space-separated files.
