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

* [csv](sources/csv.md)

`cache` definition:

path
: File-path to cache location. The variable `{store}` can be used for the store name, and `{id}` for the asset ID.
  The path defaults to `~/.cache/fileset/${store}/{id}`. The path can be given as
  absolute path, or relative to the configuration file.

`on-get` event definition:

run
: command to run for `{file}`

Full Example:

```yaml
---
file-stores:
    <store-name>:
        source:
            <store-engine>
        cache:
            path: ~/.cache/fileset/{store}/{id}
        on-get:
            run: '<command> {file}'
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
