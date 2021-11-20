Remove Command
==============

Remove files from the file-cache to save disk-space. The command is applied *on* a `store`.

Automatically apply the action without confirmation:

```console
fileset <store> rm [--force]
```

If a .fileset file exists in the current working directory, it will be applied, unless `--set <fileset.yml>` is used.

To remove a subset of the set, specify one or more paths:

```console
fileset <store> rm [-s/--set <fileset.yml>] path/in/set ...
```

To remove a specific asset ID from the cache, specify one or more IDs:

```console
fileset <store> rm [-s/--set <fileset.yml>] ID ...
```

To remove a specific assert ID from the cache without a set-definition, specify one or more IDs:

```console
fileset <store> rm+ ID ...
```
