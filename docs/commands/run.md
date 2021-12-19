Run Command
===========

Executes a command on the files scoped by the set. The command is applied *on* a `store`.

Files not in the cache will not be fetched by default. If they are not in the cache,
a warning will be printed but otherwise ignored.

To trigger an implicit `get` on any missing assets, run with:

```console
fileset <store> run --get ...
```

Automatically apply the action without confirmation:

```console
fileset <store> run [-f/--force] ...
```

Use fileset (see [fileset](../fileset.md#sets) for more info):

```console
fileset <store> run [-s/--set <fileset.yml>] ...
```

If a `FileSet.yml` file exists in the current working directory, it will be applied,
unless `--set <fileset.yml>` is used.

Pass extra arguments to the command:

```console
fileset <store> run -- args-to-cmd
```

To run the command `<cmd>` on a subset of the set, specify one or more paths:

```console
fileset <store> run <cmd> path/in/set ...
```

To run the command on a specific ID, specify one or more IDs:

```console
fileset <store> run ID ...
```

To run the command on a specific asset ID from the cache without or outside current set-definition,
use the `run+` (run plus command), and specify one or more IDs:

```console
fileset <store> run+ ID ...
```

Command Definition
------------------

Commands are defined in `~/.fileset.yml` of the user. Or through environmental variable `FILESET_CONFIG=<fileset.yml>`.

Commands can also be specified in `FileSet.yml` files together with sets.

If multiple commands are named the same, the last one in `FileSet.yml` will be used.

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

If max-arg-length is often exceeded, use smaller sets or invoke the command
once for each file.
