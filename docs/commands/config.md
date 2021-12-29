Config Command
==============

Command to print and validate the applied configuration.

Defaults to `~/.fileset.yml`, but can be overridden by environmental variable
`FILESET_CONFIG`.

Validate and print the fully applied configuration:

```console
fileset config
```

Silence printing of the configuration, only validate:

```console
fileset config -q|--quite
```

Print only the the absolute path of the configuration file; can not be combined
with other options:

```console
fileset config --config-file
```

Use fileset (see [fileset](../fileset.md#sets) for more info):

```console
fileset config [-s/--set <fileset.yml>] ...
```

If a `FileSet.yml` file exists in the current working directory, it will be applied,
unless `--set <fileset.yml>` is used.

Print only the absolute path of the set-definition file; can not be combined
with other print options:

```console
fileset config --set-file
```

Print the set structure as paths:

```console
fileset config --set-paths
```

Print the set structure, assets only, as paths:

```console
fileset config --asset-paths
```
