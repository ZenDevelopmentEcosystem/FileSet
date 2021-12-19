Get Command
===========

Get files into the file-cache. The command is applied *on* a `store`.

Update index before get:

```console
fileset <store> get [--index-update] ...
```

Automatically apply the action without confirmation:

```console
fileset <store> get [-f/--force]
```

Use fileset (see [fileset](../fileset.md#sets) for more info):

```console
fileset <store> get [-s/--set <fileset.yml>] ...
```

If a `FileSet.yml` file exists in the current working directory, it will be applied,
unless `--set <fileset.yml>` is used.

To get a subset of the set, specify one or more paths:

```console
 fileset <store> get path/in/set ...
```

To get a specific asset ID, specify one or more IDs:

```console
fileset <store> get ID ...
```

To get a specific asset ID from the file-store without or outside current set-definition,
use the `get+` (get plus command), and specify one or more IDs:

```console
# ID from full index
fileset <store> get+ <ID>
```

Running `get+` without specifying an ID will get every asset in the store.

`get+` can't be combined with `--set`.
