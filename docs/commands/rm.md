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

If a .fileset file exists in the current working directory, it will be applied,
unless `--set <fileset.yml>` is used.

To remove a subset of the set, specify one or more paths:

```console
fileset <store> rm [-s/--set <fileset.yml>] path/in/set ...
```

To remove a specific asset ID from the cache, within the set, specify one or more IDs:

```console
fileset <store> rm [-s/--set <fileset.yml>] ID ...
```

To remove a specific asset ID from the cache without a set-definition, use the `rm+` (rm plus command),
specify one or more IDs:

```console
fileset <store> rm+ ID ...
```
