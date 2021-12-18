Run Command
===========

Executes a command on the files scoped by the set.

Example:

```console
fileset <store> run <cmd> path/in/set ... -- args-to-cmd
```

Commands are defined in `~/.fileset.yml` of the user. Or through environmental variable `FILESET_CONFIG=<fileset.yml>`.

```yaml
runs:
    <command-name>:
        command: command-to-invoke ${files}
        for-each-file: -f ${file}
        max-arg-length:
```

command
: The command to be invoked.
: The token `${files}` expands to the expression defined by `for-each-file` as a
  space separated list for all files.
: The token `${file}` will instead force the command to be invoked once for every file.
: If both or neither of the tokens `${files}` or `${file}`, is part of the command,
  an error will be thrown.

for-each-file
: The token `${file}` together with any extra arguments, to define the expression
  to be used for each file when building the token `${files}`.
: If `for-each-file` is not specified, it defaults to `${file}`.
: `for-each-file` has no meaning when the command is invoked for each file in the set.

max-arg-length
: Specifies the number of bytes the total command-line is allowed to be.
  If the length is exceeded, the command will not be run.
: If max-arg-length is not specified, it defaults to the value of `getconf ARG_MAX`.
