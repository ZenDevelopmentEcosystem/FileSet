Get Command
===========

Get files into the file-cache. The command is applied *on* a `store`.

update index before get:

```console
fileset <store> get [--index-update] ...
```

Automatically apply the action without confirmation:

```console
fileset <store> get [--force]
```

Print the filenames from the cache (useful for command-line scripting):

```console
fileset <store> get [--print]
```

Use fileset (see [fileset](../fileset.md#sets) for more info):

```console
fileset <store> get [-s/--set <fileset.yml>] ...
```

If a `FileSet.yml` file exists in the current working directory, it will be applied,
unless `--set <fileset.yml>` is used.

To get a subset of the set, specify one or more paths:

```console
 fileset <store> get [-s/--set <fileset.yml>] path/in/set ...
```

To get a specific asset ID, specify one or more IDs:

```console
fileset <store> get [-s/--set <fileset.yml>] ID ...
```

To get a specific asset ID from the file-store without a set-definition, use the `get+` (get plus command),
specify one or more IDs:

```console
# ID from full index
fileset <store> get+ <ID>
```
