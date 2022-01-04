# File

> Auto-generated documentation for [dulwich.file](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/file.py) module.

Safe access to git files.

- [AddOns-Update-Tool](../README.md#addons-update-tool-index) / [Modules](../MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / File
    - [FileLocked](#filelocked)
    - [GitFile](#gitfile)
    - [ensure_dir_exists](#ensure_dir_exists)

## FileLocked

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/file.py#L97)

```python
class FileLocked(Exception):
    def __init__(filename, lockfilename):
```

File is already locked.

## GitFile

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/file.py#L69)

```python
def GitFile(filename, mode='rb', bufsize=-1, mask=420):
```

Create a file object that obeys the git file locking protocol.

Returns: a builtin file object or a _GitFile object

Note: See _GitFile for a description of the file locking protocol.

Only read-only and write-only (binary) modes are supported; r+, w+, and a
are not.  To read and write from the same file, you can take advantage of
the fact that opening a file for write does not actually open the file you
request.

The default file mask makes any created files user-writable and
world-readable.

## ensure_dir_exists

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/file.py#L28)

```python
def ensure_dir_exists(dirname):
```

Ensure a directory exists, creating if necessary.
