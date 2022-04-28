# Index

> Auto-generated documentation for [dulwich.index](../../dulwich/index.py) module.

Parser for the git index file format.

- [AddOns-Update-Tool](../README.md#addons-update-tool-index) / [Modules](../MODULES.md#addons-update-tool-modules) / [Dulwich](#dulwich) / Index
    - [Index](#index)
        - [Index().\_\_getitem\_\_](#index__getitem__)
        - [Index().\_\_iter\_\_](#index__iter__)
        - [Index().\_\_len\_\_](#index__len__)
        - [Index().changes_from_tree](#indexchanges_from_tree)
        - [Index().clear](#indexclear)
        - [Index().commit](#indexcommit)
        - [Index().get_mode](#indexget_mode)
        - [Index().get_sha1](#indexget_sha1)
        - [Index().items](#indexitems)
        - [Index().iteritems](#indexiteritems)
        - [Index().iterobjects](#indexiterobjects)
        - [Index().path](#indexpath)
        - [Index().read](#indexread)
        - [Index().update](#indexupdate)
        - [Index().write](#indexwrite)
    - [locked_index](#locked_index)
    - [blob_from_path_and_mode](#blob_from_path_and_mode)
    - [blob_from_path_and_stat](#blob_from_path_and_stat)
    - [build_file_from_blob](#build_file_from_blob)
    - [build_index_from_tree](#build_index_from_tree)
    - [changes_from_tree](#changes_from_tree)
    - [cleanup_mode](#cleanup_mode)
    - [commit_index](#commit_index)
    - [commit_tree](#commit_tree)
    - [get_unstaged_changes](#get_unstaged_changes)
    - [index_entry_from_directory](#index_entry_from_directory)
    - [index_entry_from_path](#index_entry_from_path)
    - [index_entry_from_stat](#index_entry_from_stat)
    - [iter_fresh_entries](#iter_fresh_entries)
    - [iter_fresh_objects](#iter_fresh_objects)
    - [pathjoin](#pathjoin)
    - [pathsplit](#pathsplit)
    - [read_cache_entry](#read_cache_entry)
    - [read_cache_time](#read_cache_time)
    - [read_index](#read_index)
    - [read_index_dict](#read_index_dict)
    - [read_submodule_head](#read_submodule_head)
    - [refresh_index](#refresh_index)
    - [validate_path](#validate_path)
    - [validate_path_element_default](#validate_path_element_default)
    - [validate_path_element_ntfs](#validate_path_element_ntfs)
    - [write_cache_entry](#write_cache_entry)
    - [write_cache_time](#write_cache_time)
    - [write_index](#write_index)
    - [write_index_dict](#write_index_dict)

#### Attributes

- `FLAG_STAGEMASK` - 2-bit stage (during merge): `12288`
- `FLAG_VALID` - assume-valid: `32768`
- `FLAG_EXTENDED` - extended flag (must be zero in version 2): `16384`
- `EXTENDED_FLAG_SKIP_WORKTREE` - used by sparse checkout: `16384`
- `EXTENDED_FLAG_INTEND_TO_ADD` - used by "git add -N": `8192`

## Index

[[find in source code]](../../dulwich/index.py#L310)

```python
class Index(object):
    def __init__(filename):
```

A Git Index file.

### Index().\_\_getitem\_\_

[[find in source code]](../../dulwich/index.py#L360)

```python
def __getitem__(name: bytes) -> IndexEntry:
```

Retrieve entry by relative path.

Returns: tuple with (ctime, mtime, dev, ino, mode, uid, gid, size, sha,
    flags)

#### See also

- [IndexEntry](#indexentry)

### Index().\_\_iter\_\_

[[find in source code]](../../dulwich/index.py#L368)

```python
def __iter__() -> Iterator[bytes]:
```

Iterate over the paths in this index.

### Index().\_\_len\_\_

[[find in source code]](../../dulwich/index.py#L356)

```python
def __len__() -> int:
```

Number of entries in this index file.

### Index().changes_from_tree

[[find in source code]](../../dulwich/index.py#L410)

```python
def changes_from_tree(object_store, tree, want_unchanged=False):
```

Find the differences between the contents of this index and a tree.

#### Arguments

  - `object_store` - Object store to use for retrieving tree contents
  - `tree` - SHA1 of the root tree
  - `want_unchanged` - Whether unchanged files should be reported
- `Returns` - Iterator over tuples with (oldpath, newpath), (oldmode,
    newmode), (oldsha, newsha)

### Index().clear

[[find in source code]](../../dulwich/index.py#L386)

```python
def clear():
```

Remove all contents from this index.

### Index().commit

[[find in source code]](../../dulwich/index.py#L434)

```python
def commit(object_store):
```

Create a new tree from an index.

#### Arguments

- `object_store` - Object store to save the tree in

#### Returns

Root tree SHA

### Index().get_mode

[[find in source code]](../../dulwich/index.py#L376)

```python
def get_mode(path: bytes) -> int:
```

Return the POSIX file mode for the object at a path.

### Index().get_sha1

[[find in source code]](../../dulwich/index.py#L372)

```python
def get_sha1(path: bytes) -> bytes:
```

Return the (git object) SHA1 for the object at a path.

### Index().items

[[find in source code]](../../dulwich/index.py#L403)

```python
def items():
```

### Index().iteritems

[[find in source code]](../../dulwich/index.py#L400)

```python
def iteritems():
```

### Index().iterobjects

[[find in source code]](../../dulwich/index.py#L380)

```python
def iterobjects() -> Iterable[Tuple[bytes, bytes, int]]:
```

Iterate over path, sha, mode tuples for use with commit_tree.

### Index().path

[[find in source code]](../../dulwich/index.py#L325)

```python
@property
def path():
```

### Index().read

[[find in source code]](../../dulwich/index.py#L341)

```python
def read():
```

Read current contents of index from disk.

### Index().update

[[find in source code]](../../dulwich/index.py#L406)

```python
def update(entries):
```

### Index().write

[[find in source code]](../../dulwich/index.py#L332)

```python
def write() -> None:
```

Write current contents of index to disk.

## locked_index

[[find in source code]](../../dulwich/index.py#L974)

```python
class locked_index(object):
    def __init__(path):
```

Lock the index while making modifications.

Works as a context manager.

## blob_from_path_and_mode

[[find in source code]](../../dulwich/index.py#L723)

```python
def blob_from_path_and_mode(fs_path, mode, tree_encoding='utf-8'):
```

Create a blob from a path and a stat object.

#### Arguments

  - `fs_path` - Full file system path to file
  - `mode` - File mode
- `Returns` - A `Blob` object

## blob_from_path_and_stat

[[find in source code]](../../dulwich/index.py#L746)

```python
def blob_from_path_and_stat(fs_path, st, tree_encoding='utf-8'):
```

Create a blob from a path and a stat object.

#### Arguments

  - `fs_path` - Full file system path to file
  - `st` - A stat object
- `Returns` - A `Blob` object

## build_file_from_blob

[[find in source code]](../../dulwich/index.py#L583)

```python
def build_file_from_blob(
    blob,
    mode,
    target_path,
    honor_filemode=True,
    tree_encoding='utf-8',
):
```

Build a file or symlink on disk based on a Git object.

#### Arguments

  - `blob` - The git object
  - `mode` - File mode
  - `target_path` - Path to write to
  - `honor_filemode` - An optional flag to honor core.filemode setting in
    config file, default is core.filemode=True, change executable bit
- `Returns` - stat object for the file

## build_index_from_tree

[[find in source code]](../../dulwich/index.py#L652)

```python
def build_index_from_tree(
    root_path,
    index_path,
    object_store,
    tree_id,
    honor_filemode=True,
    validate_path_element=validate_path_element_default,
):
```

Generate and materialize index from a tree

#### Arguments

- `tree_id` - Tree to materialize
- `root_path` - Target dir for materialized index files
- `index_path` - Target path for generated index
- `object_store` - Non-empty object store holding tree contents
- `honor_filemode` - An optional flag to honor core.filemode setting in
  config file, default is core.filemode=True, change executable bit
- `validate_path_element` - Function to validate path elements to check
  out; default just refuses .git and .. directories.

- `Note` - existing index is wiped and contents are not merged
    in a working dir. Suitable only for fresh clones.

#### See also

- [validate_path_element_default](#validate_path_element_default)

## changes_from_tree

[[find in source code]](../../dulwich/index.py#L501)

```python
def changes_from_tree(
    names: Iterable[bytes],
    lookup_entry: Callable[[bytes], Tuple[bytes, int]],
    object_store: 'BaseObjectStore',
    tree: Optional[bytes],
    want_unchanged=False,
) -> Iterable[Tuple[
    Tuple[
        Optional[bytes],
        Optional[bytes],
    ],
    Tuple[
        Optional[int],
        Optional[int],
    ],
    Tuple[
        Optional[bytes],
        Optional[bytes],
    ],
]]:
```

Find the differences between the contents of a tree and
a working copy.

#### Arguments

  - `names` - Iterable of names in the working copy
  - `lookup_entry` - Function to lookup an entry in the working copy
  - `object_store` - Object store to use for retrieving tree contents
  - `tree` - SHA1 of the root tree, or None for an empty tree
  - `want_unchanged` - Whether unchanged files should be reported
- `Returns` - Iterator over tuples with (oldpath, newpath), (oldmode, newmode),
    (oldsha, newsha)

## cleanup_mode

[[find in source code]](../../dulwich/index.py#L288)

```python
def cleanup_mode(mode: int) -> int:
```

Cleanup a mode value.

This will return a mode that can be stored in a tree object.

#### Arguments

- `mode` - Mode to clean up.

#### Returns

mode

## commit_index

[[find in source code]](../../dulwich/index.py#L489)

```python
def commit_index(object_store: 'BaseObjectStore', index: Index) -> bytes:
```

Create a new tree from an index.

#### Arguments

  - `object_store` - Object store to save the tree in
  - `index` - Index file
- `Note` - This function is deprecated, use index.commit() instead.
- `Returns` - Root tree sha.

#### See also

- [Index](#index)

## commit_tree

[[find in source code]](../../dulwich/index.py#L445)

```python
def commit_tree(
    object_store: 'BaseObjectStore',
    blobs: Iterable[Tuple[bytes, bytes, int]],
) -> bytes:
```

Commit a new tree.

#### Arguments

- `object_store` - Object store to add trees to
- `blobs` - Iterable over blob path, sha, mode entries

#### Returns

SHA1 of the created tree.

## get_unstaged_changes

[[find in source code]](../../dulwich/index.py#L806)

```python
def get_unstaged_changes(index: Index, root_path, filter_blob_callback=None):
```

Walk through an index and check for differences against working tree.

#### Arguments

  - `index` - index to check
  - `root_path` - path in which to find files
- `Returns` - iterator over paths with unstaged changes

#### See also

- [Index](#index)

## index_entry_from_directory

[[find in source code]](../../dulwich/index.py#L882)

```python
def index_entry_from_directory(st, path):
```

## index_entry_from_path

[[find in source code]](../../dulwich/index.py#L891)

```python
def index_entry_from_path(path, object_store=None):
```

Create an index from a filesystem path.

This returns an index value for files, symlinks
and tree references. for directories and
non-existant files it returns None

#### Arguments

  - `path` - Path to create an index entry for
  - `object_store` - Optional object store to
    save new blobs in
- `Returns` - An index entry; None for directories

## index_entry_from_stat

[[find in source code]](../../dulwich/index.py#L551)

```python
def index_entry_from_stat(
    stat_val,
    hex_sha: bytes,
    flags: int,
    mode: Optional[int] = None,
    extended_flags: Optional[int] = None,
):
```

Create a new index entry from a stat value.

#### Arguments

- `stat_val` - POSIX stat_result instance
- `hex_sha` - Hex sha of the object
- `flags` - Index flags

## iter_fresh_entries

[[find in source code]](../../dulwich/index.py#L918)

```python
def iter_fresh_entries(
    paths,
    root_path,
    object_store: Optional['BaseObjectStore'] = None,
):
```

Iterate over current versions of index entries on disk.

#### Arguments

  - `paths` - Paths to iterate over
  - `root_path` - Root path to access from
  - `object_store` - Optional store to save new blobs in
- `Returns` - Iterator over path, index_entry

## iter_fresh_objects

[[find in source code]](../../dulwich/index.py#L938)

```python
def iter_fresh_objects(
    paths,
    root_path,
    include_deleted=False,
    object_store=None,
):
```

Iterate over versions of objecs on disk referenced by index.

#### Arguments

  - `root_path` - Root path to access from
  - `include_deleted` - Include deleted entries with sha and
    mode set to None
  - `object_store` - Optional object store to report new items to
- `Returns` - Iterator over path, sha, mode

## pathjoin

[[find in source code]](../../dulwich/index.py#L114)

```python
def pathjoin(*args):
```

Join a /-delimited path.

## pathsplit

[[find in source code]](../../dulwich/index.py#L98)

```python
def pathsplit(path):
```

Split a /-delimited path into a directory part and a basename.

#### Arguments

- `path` - The path to split.

#### Returns

Tuple with directory name and basename

## read_cache_entry

[[find in source code]](../../dulwich/index.py#L147)

```python
def read_cache_entry(f, version: int) -> Tuple[str, IndexEntry]:
```

Read an entry from a cache file.

#### Arguments

- `f` - File-like object to read from

#### Returns

- `tuple` *with* - name, IndexEntry

#### See also

- [IndexEntry](#indexentry)

## read_cache_time

[[find in source code]](../../dulwich/index.py#L119)

```python
def read_cache_time(f):
```

Read a cache time.

#### Arguments

- `f` - File-like object to read from

#### Returns

Tuple with seconds and nanoseconds

## read_index

[[find in source code]](../../dulwich/index.py#L233)

```python
def read_index(f: BinaryIO):
```

Read an index file, yielding the individual entries.

## read_index_dict

[[find in source code]](../../dulwich/index.py#L244)

```python
def read_index_dict(f):
```

Read an index file and return it as a dictionary.

#### Arguments

- `f` - File object to read from

## read_submodule_head

[[find in source code]](../../dulwich/index.py#L757)

```python
def read_submodule_head(path):
```

Read the head commit of a submodule.

#### Arguments

  - `path` - path to the submodule
- `Returns` - HEAD sha, None if not a valid head/repository

## refresh_index

[[find in source code]](../../dulwich/index.py#L961)

```python
def refresh_index(index, root_path):
```

Refresh the contents of an index.

This is the equivalent to running 'git commit -a'.

#### Arguments

- `index` - Index to update
- `root_path` - Root filesystem path

## validate_path

[[find in source code]](../../dulwich/index.py#L642)

```python
def validate_path(path, element_validator=validate_path_element_default):
```

Default path validator that just checks for .git/.

#### See also

- [validate_path_element_default](#validate_path_element_default)

## validate_path_element_default

[[find in source code]](../../dulwich/index.py#L629)

```python
def validate_path_element_default(element):
```

## validate_path_element_ntfs

[[find in source code]](../../dulwich/index.py#L633)

```python
def validate_path_element_ntfs(element):
```

## write_cache_entry

[[find in source code]](../../dulwich/index.py#L197)

```python
def write_cache_entry(f, name, entry, version):
```

Write an index entry to a file.

#### Arguments

- `f` - File object
- `entry` - IndexEntry to write, tuple with:

## write_cache_time

[[find in source code]](../../dulwich/index.py#L130)

```python
def write_cache_time(f, t):
```

Write a cache time.

#### Arguments

- `f` - File-like object to write to
- `t` - Time to write (as int, float or tuple with secs and nsecs)

## write_index

[[find in source code]](../../dulwich/index.py#L256)

```python
def write_index(
    f: BinaryIO,
    entries: List[Tuple[bytes, IndexEntry]],
    version: Optional[int] = None,
):
```

Write an index file.

#### Arguments

- `f` - File-like object to write to
- `version` - Version number to write
- `entries` - Iterable over the entries to write

## write_index_dict

[[find in source code]](../../dulwich/index.py#L276)

```python
def write_index_dict(
    f: BinaryIO,
    entries: Dict[bytes, IndexEntry],
    version: Optional[int] = None,
) -> None:
```

Write an index file based on the contents of a dictionary.

#### See also

- [IndexEntry](#indexentry)
