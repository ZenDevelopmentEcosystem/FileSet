List Command
============

List the assets in a set. Only cached assets will be listed.
If an asset is requested using ID, and the asset isn't cached,
it will not be shown.

```console
fileset <store> ls
```

Use fileset (see [fileset](../fileset.md#sets) for more info):

```console
fileset <store> ls [-s/--set <fileset.yml>] ...
```

If a `FileSet.yml` file exists in the current working directory, it will be applied,
unless `--set <fileset.yml>` is used.

To show uncached (missing) assets, run:

```console
fileset <store> ls --missing
```

To list a subset of the set, specify one or more paths:

```console
fileset <store> ls path/in/set ...
```

To list a specific asset ID from the cache, within the set, specify one or more IDs:

```console
fileset <store> ls ID ...
```

To list a specific asset ID from the cache without or outside current set-definition,
use the `ls+` (ls plus command), and specify one or more IDs:

```console
fileset <store> ls+ ID ...
```

Running `ls+` without specifying an ID will list all assets in the cache.

`ls+` can't be combined with `--missing` or `--set`.
