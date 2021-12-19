Remove Command
==============

Remove files from the file-cache to save disk-space. The command is applied *on* a `store`.

Note that sets are only a virtual representation of the assets in a given store.
Hence, removing an asset from the store, regardless of set being used to interface the store,
the asset will be removed for all sets for that store.

Automatically apply the action without confirmation:

```console
fileset <store> rm [--force]
```

Use fileset (see [fileset](../fileset.md#sets) for more info):

```console
fileset <store> rm [-s/--set <fileset.yml>] ...
```

If a `FileSet.yml` file exists in the current working directory, it will be applied,
unless `--set <fileset.yml>` is used.

To remove a subset of the set, specify one or more paths:

```console
fileset <store> rm path/in/set ...
```

To remove a specific asset ID from the cache, within the set, specify one or more IDs:

```console
fileset <store> rm ID ...
```

To remove a specific asset ID from the cache without or outside current set-definition,
use the `rm+` (rm plus command), and specify one or more IDs:

```console
fileset <store> rm+ ID ...
```

Running `rm+` without specifying an ID will remove every asset in the cache.

`rm+` can't be combined with `--set`.
