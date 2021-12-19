Filesystem Command
==================

Create a filesystem replicating the structure of a file-set using the assets
in the cache.

The command is applied *on* a `store` and must have a valid set-definition.

Assets in the cache will not be fetched by default. If they are not in the cache,
a warning will be printed but otherwise ignored.

The destination directory must be on the same filesystem as the cache directory,
unless symbolic links are used.

The destination directory is specified as the principle positional argument:

```console
fileset <store> fs destdir
```

The destination directory defaults to the current working directory if left out.

To trigger an implicit `get` on any missing assets, run with:

```console
fileset <store> fs --get ...
```

Automatically apply the action without confirmation:

```console
fileset <store> fs [-f/--force] ...
```

Use fileset (see [fileset](../fileset.md#sets) for more info):

```console
fileset <store> fs [-s/--set <fileset.yml>] ...
```

If a `FileSet.yml` file exists in the current working directory, it will be applied,
unless `--set <fileset.yml>` is used.

To create symbolic links (instead of the default hard links):

```console
fileset <store> fs [--symbolic] ...
```

Symbolic links will automatically be used if assets are directories, since hard links
can't be created for directories. Symbolic must be used if the destination directory
is on a different filesystem than the store cache.

To create the link structure for a subset of the set, specify one or more paths after
the destination directory:

```console
fileset <store> fs destdir path/in/set ...
```
