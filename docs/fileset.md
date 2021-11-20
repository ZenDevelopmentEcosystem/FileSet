FileSet
=======

Commands:

* stores
* `<store>` index
* `<store>` get
* `<store>` ls
* `<store>` rm
* `<store>` run


Stores Command
--------------

See also [File-Store Definition](#file-store-definitions).

`stores` subcommands:

ls
: list stores

Example:

```console
fileset stores ls
```

Index Command
-------------

Manage a store's index. The command is applied *on* a `store`.

Index sub-commands:

update
: update the current index
ls
: list items in the current index

Examples:

```console
fileset <store> index update
fileset <store> index ls [--format '%1\t%2']
```

Get Command
-----------

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

Use fileset (see [fileset](#fileset) for more info):

```console
fileset <store> get [-s/--set <fileset.yml>] ...
```

If a `FileSet.yml` file exists in the current working directory, it will be applied, unless `--set <fileset.yml>` is used.

To get a subset of the set, specify one or more paths:

```console
 fileset <store> get [-s/--set <fileset.yml>] path/in/set ...
```

To get a specific asset ID, specify one or more IDs:

```console
fileset <store> get [-s/--set <fileset.yml>] ID ...
```

To get a specific asset ID from the file-store, specify one or more IDs:

```console
# ID from full index
fileset <store> get+ <ID>
```

List Command
------------

List the assets in set.

```console
fileset <store> ls [path/in/set ...]
```

Remove Command
--------------

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

Run Command
-----------

Executes a command on the files scoped by the set.

Example:

```console
fileset <store> run <cmd> path/in/set ... -- args-to-cmd
```

The command is defined in a FileSet.yml config as:

```yaml
runs:
    <run-name>:
        command: command to invoke ${files}
        for-each-file: -f ${file}
```

Defaults
: If `${files}` is not part of the `command`, the files are appended at the end.
: If `${file}` is not part of `for-each-file` it is appended at the end.
: If `for-each-file` is not specified, it defaults to `${file}` which expands
  to a list of space-separated files.

File-Store Definitions
----------------------

File-stores are defined in `~/.fileset.yml` of the user. Or through environmental variable `FILESET_CONFIG=<fileset.yml>`.

The file-store is defined by:

source
: the file-source defined through a file-store engine.

cache
: Information about the file cache.

on-get
: Event to be triggered when a file is retrieved from a source.

on-rm
: Event to be triggered when a file is deleted from the cache.

`source`-types:

* [csv](#csv-filesystem-file-store-engine)

`cache` definition:

path
: File-path to cache location. The variable `${source}` can be used for the source name.
  The path defaults to `~/.cache/fileset/${source}`.

`on-get`, `on-rm` event definitions:

run
: command to run for `${file}`

log
: if the event should be logged and to what destinations (comma separated list).
  Valid options: `console`

Full Example:

```yaml
---
file-stores:
    <store-name>:
        source:
            <store-engine>
        cache:
            path: ~/.cache/fileset/${source}
        on-get:
            run: '<command> ${file}'
            log: console
        on-rm:
            run: '<command> ${file}'
            log: console
```

Sets
----

A set is a tree structure where the leaves are asset-IDs.

The example below categorizes music files in the sub-groups pop and rock.
The asset "song1" is categorized as both pop and rock.

Example:

```yaml
set:
    music:
        pop:
            - song1
            - song2
        rock:
            - song1
            - song3
```

CSV-Filesystem File-store Engine
--------------------------------

Is defined by the element `csv` and the following sub-elements:

file
: the CSV-file listing the index

id-column
: the column in the CSV-file that has unique IDs

filename-column
: the column in the CSV-file that has the filename, including sub-path relative root-path.

filename-suffix
: a suffix that is appended to the filename to get the actual file as it appears on the filesystem

root-path
: the file-system root-directory where the data-store exists. Usually a mounted network filesystem such as NFS or CIFS.

Configuration example (relative to `file-stores > {store-name} > source`: ):

```yaml
csv:
    file: /mnt/remote/my-file-store/index.csv
    id-column: id
    filename-column: filename
    filename-suffix: .txt
    root-path: /mnt/remote/my-file-store/data
```

`index.csv` in the example above:

```csv
id;filename
1;relative/path/to/file-1
2;relative/path/to/file-2
```

Actual filesystem for the example above:

```console
/mnt/remote/my-file-store/data/relative/path/to/file-1.txt
/mnt/remote/my-file-store/data/relative/path/to/file-2.txt
```
