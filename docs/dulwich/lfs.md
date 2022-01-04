# Lfs

> Auto-generated documentation for [dulwich.lfs](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/lfs.py) module.

- [AddOns-Update-Tool](../README.md#addons-update-tool-index) / [Modules](../MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / Lfs
    - [LFSStore](#lfsstore)
        - [LFSStore.create](#lfsstorecreate)
        - [LFSStore.from_repo](#lfsstorefrom_repo)
        - [LFSStore().open_object](#lfsstoreopen_object)
        - [LFSStore().write_object](#lfsstorewrite_object)

## LFSStore

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/lfs.py#L26)

```python
class LFSStore(object):
    def __init__(path):
```

Stores objects on disk, indexed by SHA256.

### LFSStore.create

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/lfs.py#L32)

```python
@classmethod
def create(lfs_dir):
```

### LFSStore.from_repo

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/lfs.py#L40)

```python
@classmethod
def from_repo(repo, create=False):
```

### LFSStore().open_object

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/lfs.py#L50)

```python
def open_object(sha):
```

Open an object by sha.

### LFSStore().write_object

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/lfs.py#L57)

```python
def write_object(chunks):
```

Write an object.

Returns: object SHA
