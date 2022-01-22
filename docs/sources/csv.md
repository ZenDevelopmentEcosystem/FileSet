CSV-Filesystem Source
=====================

The csv source-type is defined by the element `csv` and the following sub-elements:

index-file
: the CSV-file listing the index, absolute path or relative to the configuration file.

id-column
: the column in the CSV-file that has unique IDs

filename-column
: the column in the CSV-file that has the filename, including sub-path relative root-path.

filename-suffix
: a suffix that is appended to the filename to get the actual file as it appears on the filesystem

root-path
: the file-system root-directory where the data-store exists. Usually a mounted network filesystem such as NFS or CIFS.
  Absolute path or relative to the configuration file.

Configuration example (other sections excluded):

```yaml
file-stores:
    my-store:
        csv:
            index-file: /mnt/remote/my-file-store/index.csv
            id-column: id
            filename-column: filename
            filename-suffix: .txt
            root-path: /mnt/remote/my-file-store/data
        ...
```

`index-file` and `root-path` can be given as absolute paths or relative paths
to the config file.

Content of the `index.csv` in the example above:

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
