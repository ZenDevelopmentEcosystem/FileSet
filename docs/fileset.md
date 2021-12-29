FileSet
=======

Commands:

* [config](commands/config.md)
* [stores](commands/stores.md)
* [`<store>` index](commands/index.md)
* [`<store>` get](commands/get.md)
* [`<store>` ls](commands/ls.md)
* [`<store>` rm](commands/rm.md)
* [`<store>` run](commands/run.md)
* [`<store>` fs](commands/fs.md)

File-Store Definitions
----------------------

File-stores are defined in `~/.fileset.yml` of the user. Or through environmental variable `FILESET_CONFIG=<fileset.yml>`.

The file-store is defined by:

source
: the file-source defined through a file-store engine.

cache
: Information about the file cache.

on-get
: Event to be triggered when an asset is retrieved from a source.

`source`-types:

* [csv](#csv-filesystem-file-store-engine)

`cache` definition:

path
: File-path to cache location. The variable `${store}` can be used for the store name.
  The path defaults to `~/.cache/fileset/${store}`. The path can be given as
  absolute path, or relative to the configuration file.

`on-get` event definition:

run
: command to run for `${file}`

Full Example:

```yaml
---
file-stores:
    <store-name>:
        source:
            <store-engine>
        cache:
            path: ~/.cache/fileset/${store}
        on-get:
            run: '<command> ${file}'
```

Sets
----

A set is a tree structure where the leaves are asset-IDs.

The example below categorizes music files in the sub-groups pop and rock.
The asset "song1" is categorized as both pop and rock.

Example:

```yaml
sets:
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
    index-file: /mnt/remote/my-file-store/index.csv
    id-column: id
    filename-column: filename
    filename-suffix: .txt
    root-path: /mnt/remote/my-file-store/data
```

`index-file` and `root-path` can be given as absolute paths or relative paths
to the config file.

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
