# Archive

> Auto-generated documentation for [dulwich.archive](../../dulwich/archive.py) module.

Generates tarballs for Git trees.

- [AddOns-Update-Tool](../README.md#addons-update-tool-index) / [Modules](../MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / Archive
    - [ChunkedBytesIO](#chunkedbytesio)
        - [ChunkedBytesIO().read](#chunkedbytesioread)
    - [tar_stream](#tar_stream)

## ChunkedBytesIO

[[find in source code]](../../dulwich/archive.py#L35)

```python
class ChunkedBytesIO(object):
    def __init__(contents):
```

Turn a list of bytestrings into a file-like object.

This is similar to creating a `BytesIO` from a concatenation of the
bytestring list, but saves memory by NOT creating one giant bytestring
first

```python
BytesIO(b''.join(list_of_bytestrings)) =~= ChunkedBytesIO(
    list_of_bytestrings)
```

### ChunkedBytesIO().read

[[find in source code]](../../dulwich/archive.py#L50)

```python
def read(maxbytes=None):
```

## tar_stream

[[find in source code]](../../dulwich/archive.py#L72)

```python
def tar_stream(store, tree, mtime, prefix=b'', format=''):
```

Generate a tar stream for the contents of a Git tree.

Returns a generator that lazily assembles a .tar.gz archive, yielding it in
pieces (bytestrings). To obtain the complete .tar.gz binary file, simply
concatenate these chunks.

#### Arguments

- `store` - Object store to retrieve objects from
- `tree` - Tree object for the tree root
- `mtime` - UNIX timestamp that is assigned as the modification time for
  all files, and the gzip header modification time if format='gz'
- `format` - Optional compression format for tarball

#### Returns

Bytestrings
