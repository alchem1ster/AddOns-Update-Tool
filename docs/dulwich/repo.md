# Repo

> Auto-generated documentation for [dulwich.repo](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py) module.

Repository access.

- [Addons-update-tool](../README.md#addons-update-tool) / [Modules](../MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / Repo
    - [BaseRepo](#baserepo)
        - [BaseRepo().\_\_contains\_\_](#baserepo__contains__)
        - [BaseRepo().\_\_delitem\_\_](#baserepo__delitem__)
        - [BaseRepo().\_\_getitem\_\_](#baserepo__getitem__)
        - [BaseRepo().\_\_setitem\_\_](#baserepo__setitem__)
        - [BaseRepo().do_commit](#baserepodo_commit)
        - [BaseRepo().fetch](#baserepofetch)
        - [BaseRepo().fetch_objects](#baserepofetch_objects)
        - [BaseRepo().fetch_pack_data](#baserepofetch_pack_data)
        - [BaseRepo().generate_pack_data](#baserepogenerate_pack_data)
        - [BaseRepo().get_config](#baserepoget_config)
        - [BaseRepo().get_config_stack](#baserepoget_config_stack)
        - [BaseRepo().get_description](#baserepoget_description)
        - [BaseRepo().get_graph_walker](#baserepoget_graph_walker)
        - [BaseRepo().get_named_file](#baserepoget_named_file)
        - [BaseRepo().get_object](#baserepoget_object)
        - [BaseRepo().get_parents](#baserepoget_parents)
        - [BaseRepo().get_peeled](#baserepoget_peeled)
        - [BaseRepo().get_refs](#baserepoget_refs)
        - [BaseRepo().get_shallow](#baserepoget_shallow)
        - [BaseRepo().get_walker](#baserepoget_walker)
        - [BaseRepo().head](#baserepohead)
        - [BaseRepo().open_index](#baserepoopen_index)
        - [BaseRepo().parents_provider](#baserepoparents_provider)
        - [BaseRepo().set_description](#basereposet_description)
        - [BaseRepo().update_shallow](#baserepoupdate_shallow)
    - [InvalidUserIdentity](#invaliduseridentity)
    - [MemoryRepo](#memoryrepo)
        - [MemoryRepo().get_config](#memoryrepoget_config)
        - [MemoryRepo().get_description](#memoryrepoget_description)
        - [MemoryRepo().get_named_file](#memoryrepoget_named_file)
        - [MemoryRepo.init_bare](#memoryrepoinit_bare)
        - [MemoryRepo().open_index](#memoryrepoopen_index)
        - [MemoryRepo().set_description](#memoryreposet_description)
    - [ParentsProvider](#parentsprovider)
        - [ParentsProvider().get_parents](#parentsproviderget_parents)
    - [Repo](#repo)
        - [Repo().clone](#repoclone)
        - [Repo().close](#repoclose)
        - [Repo().commondir](#repocommondir)
        - [Repo().controldir](#repocontroldir)
        - [Repo.discover](#repodiscover)
        - [Repo().get_blob_normalizer](#repoget_blob_normalizer)
        - [Repo().get_config](#repoget_config)
        - [Repo().get_description](#repoget_description)
        - [Repo().get_named_file](#repoget_named_file)
        - [Repo().has_index](#repohas_index)
        - [Repo().index_path](#repoindex_path)
        - [Repo.init](#repoinit)
        - [Repo.init_bare](#repoinit_bare)
        - [Repo().open_index](#repoopen_index)
        - [Repo().reset_index](#reporeset_index)
        - [Repo().set_description](#reposet_description)
        - [Repo().stage](#repostage)
        - [Repo().unstage](#repounstage)
    - [UnsupportedVersion](#unsupportedversion)
    - [check_user_identity](#check_user_identity)
    - [get_user_identity](#get_user_identity)
    - [parse_graftpoints](#parse_graftpoints)
    - [read_gitfile](#read_gitfile)
    - [serialize_graftpoints](#serialize_graftpoints)

This module contains the base class for git repositories
(BaseRepo) and an implementation which uses a repository on
local disk (Repo).

## BaseRepo

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L324)

```python
class BaseRepo(object):
    def __init__(object_store: BaseObjectStore, refs: RefsContainer):
```

Base class for a git repository.

:ivar object_store: Dictionary-like object for accessing
    the objects
:ivar refs: Dictionary-like object with the refs in this
    repository

#### See also

- [BaseObjectStore](object_store.md#baseobjectstore)
- [RefsContainer](refs.md#refscontainer)

### BaseRepo().\_\_contains\_\_

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L785)

```python
def __contains__(name: bytes) -> bool:
```

Check if a specific Git object or ref is present.

#### Arguments

- `name` - Git object SHA1 or ref name

### BaseRepo().\_\_delitem\_\_

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L813)

```python
def __delitem__(name: bytes):
```

Remove a ref.

#### Arguments

- `name` - Name of the ref to remove

### BaseRepo().\_\_getitem\_\_

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L762)

```python
def __getitem__(name):
```

Retrieve a Git object by SHA1 or ref.

#### Arguments

  - `name` - A Git object SHA1 or a ref name
- `Returns` - A `ShaFile` object, such as a Commit or Blob

#### Raises

- `KeyError` - when the specified ref or object does not exist

### BaseRepo().\_\_setitem\_\_

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L796)

```python
def __setitem__(name: bytes, value: Union[ShaFile, bytes]):
```

Set a ref.

#### Arguments

- `name` - ref name
- `value` - Ref value - either a ShaFile object, or a hex sha

### BaseRepo().do_commit

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L859)

```python
def do_commit(
    message=None,
    committer=None,
    author=None,
    commit_timestamp=None,
    commit_timezone=None,
    author_timestamp=None,
    author_timezone=None,
    tree=None,
    encoding=None,
    ref=b'HEAD',
    merge_heads=None,
    no_verify=False,
):
```

Create a new commit.

If not specified, `committer` and `author` default to
get_user_identity(..., 'COMMITTER')
and get_user_identity(..., 'AUTHOR') respectively.

#### Arguments

- `message` - Commit message
- `committer` - Committer fullname
- `author` - Author fullname
- `commit_timestamp` - Commit timestamp (defaults to now)
- `commit_timezone` - Commit timestamp timezone (defaults to GMT)
- `author_timestamp` - Author timestamp (defaults to commit
  timestamp)
- `author_timezone` - Author timestamp timezone
  (defaults to commit timestamp timezone)
- `tree` - SHA1 of the tree root to use (if not specified the
  current index will be committed).
- `encoding` - Encoding
- `ref` - Optional ref to commit to (defaults to current branch)
- `merge_heads` - Merge heads (defaults to .git/MERGE_HEAD)
- `no_verify` - Skip pre-commit and commit-msg hooks

#### Returns

New commit SHA1

### BaseRepo().fetch

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L410)

```python
def fetch(target, determine_wants=None, progress=None, depth=None):
```

Fetch objects into another repository.

#### Arguments

  - `target` - The target repository
  - `determine_wants` - Optional function to determine what refs to
    fetch.
  - `progress` - Optional progress function
  - `depth` - Optional shallow fetch depth
- `Returns` - The local refs

### BaseRepo().fetch_objects

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L461)

```python
def fetch_objects(
    determine_wants,
    graph_walker,
    progress,
    get_tagged=None,
    depth=None,
):
```

Fetch the missing objects required for a set of revisions.

#### Arguments

  - `determine_wants` - Function that takes a dictionary with heads
    and returns the list of heads to fetch.
  - `graph_walker` - Object that can iterate over the list of revisions
    to fetch and has an "ack" method that will be called to acknowledge
    that a revision is present.
  - `progress` - Simple progress function that will be called with
    updated progress strings.
  - `get_tagged` - Function that returns a dict of pointed-to sha ->
    tag sha for including tags.
  - `depth` - Shallow fetch depth
- `Returns` - iterator over objects, with __len__ implemented

### BaseRepo().fetch_pack_data

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L432)

```python
def fetch_pack_data(
    determine_wants,
    graph_walker,
    progress,
    get_tagged=None,
    depth=None,
):
```

Fetch the pack data required for a set of revisions.

#### Arguments

  - `determine_wants` - Function that takes a dictionary with heads
    and returns the list of heads to fetch.
  - `graph_walker` - Object that can iterate over the list of revisions
    to fetch and has an "ack" method that will be called to acknowledge
    that a revision is present.
  - `progress` - Simple progress function that will be called with
    updated progress strings.
  - `get_tagged` - Function that returns a dict of pointed-to sha ->
    tag sha for including tags.
  - `depth` - Shallow fetch depth
- `Returns` - count and iterator over pack data

### BaseRepo().generate_pack_data

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L548)

```python
def generate_pack_data(have, want, progress=None, ofs_delta=None):
```

Generate pack data objects for a set of wants/haves.

#### Arguments

- `have` - List of SHA1s of objects that should not be sent
- `want` - List of SHA1s of objects that should be sent
- `ofs_delta` - Whether OFS deltas can be included
- `progress` - Optional progress reporting method

### BaseRepo().get_config

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L646)

```python
def get_config():
```

Retrieve the config object.

Returns: `ConfigFile` object for the ``.git/config`` file.

### BaseRepo().get_config_stack

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L669)

```python
def get_config_stack() -> 'StackedConfig':
```

Return a config stack for this repository.

This stack accesses the configuration for both this repository
itself (.git/config) and the global configuration, which usually
lives in ~/.gitconfig.

Returns: `Config` instance for this repository

### BaseRepo().get_description

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L653)

```python
def get_description():
```

Retrieve the description for this repository.

Returns: String with the description of the repository
    as set by the user.

### BaseRepo().get_graph_walker

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L565)

```python
def get_graph_walker(heads=None):
```

Retrieve a graph walker.

A graph walker is used by a remote repository (or proxy)
to find out which objects are present in this repository.

#### Arguments

  - `heads` - Repository heads to use (optional)
- `Returns` - A graph walker object

### BaseRepo().get_named_file

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L375)

```python
def get_named_file(path):
```

Get a file from the control dir with a specific name.

Although the filename should be interpreted as a filename relative to
the control dir in a disk-based Repo, the object returned need not be
pointing to a file in that location.

#### Arguments

  - `path` - The path to the file, relative to the control dir.
- `Returns` - An open file object, or None if the file does not exist.

### BaseRepo().get_object

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L615)

```python
def get_object(sha: bytes) -> ShaFile:
```

Retrieve the object with the specified SHA.

#### Arguments

  - `sha` - SHA to retrieve
- `Returns` - A ShaFile object

#### Raises

- `KeyError` - when the object can not be found

#### See also

- [ShaFile](objects.md#shafile)

### BaseRepo().get_parents

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L633)

```python
def get_parents(sha: bytes, commit: Commit = None) -> List[bytes]:
```

Retrieve the parents of a specific commit.

If the specific commit is a graftpoint, the graft parents
will be returned instead.

#### Arguments

  - `sha` - SHA of the commit for which to retrieve the parents
  - `commit` - Optional commit matching the sha
- `Returns` - List of parents

#### See also

- [Commit](objects.md#commit)

### BaseRepo().get_peeled

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L711)

```python
def get_peeled(ref):
```

Get the peeled value of a ref.

#### Arguments

  - `ref` - The refname to peel.
- `Returns` - The fully-peeled SHA1 of a tag object, after peeling all
    intermediate tags; if the original ref does not point to a tag,
    this will equal the original SHA1.

### BaseRepo().get_refs

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L586)

```python
def get_refs() -> Dict[bytes, bytes]:
```

Get dictionary with all refs.

Returns: A ``dict`` mapping ref names to SHA1s

### BaseRepo().get_shallow

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L683)

```python
def get_shallow():
```

Get the set of shallow commits.

Returns: Set of shallow commits.

### BaseRepo().get_walker

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L725)

```python
def get_walker(include=None, *args, **kwargs):
```

Obtain a walker for this repository.

#### Arguments

  - `include` - Iterable of SHAs of commits to include along with their
    ancestors. Defaults to [HEAD]
  - `exclude` - Iterable of SHAs of commits to exclude along with their
    ancestors, overriding includes.
  - `order` - ORDER_* constant specifying the order of results.
    Anything other than ORDER_DATE may result in O(n) memory usage.
  - `reverse` - If True, reverse the order of output, requiring O(n)
    memory.
  - `max_entries` - The maximum number of entries to yield, or None for
    no limit.
  - `paths` - Iterable of file or subtree paths to show entries for.
  - `rename_detector` - diff.RenameDetector object for detecting
    renames.
  - `follow` - If True, follow path across renames/copies. Forces a
    default rename_detector.
  - `since` - Timestamp to list commits after.
  - `until` - Timestamp to list commits before.
  - `queue_cls` - A class to use for a queue of commits, supporting the
    iterator protocol. The constructor takes a single argument, the
    Walker.
- `Returns` - A `Walker` object

### BaseRepo().head

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L593)

```python
def head() -> bytes:
```

Return the SHA1 pointed at by HEAD.

### BaseRepo().open_index

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L401)

```python
def open_index():
```

Open the index for this repository.

#### Raises

  - `NoIndexPresent` - If no index is present
- `Returns` - The matching `Index`

### BaseRepo().parents_provider

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L626)

```python
def parents_provider():
```

### BaseRepo().set_description

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L661)

```python
def set_description(description):
```

Set the description for this repository.

#### Arguments

- `description` - Text to set as description for this repository.

### BaseRepo().update_shallow

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L694)

```python
def update_shallow(new_shallow, new_unshallow):
```

Update the list of shallow objects.

#### Arguments

- `new_shallow` - Newly shallow objects
- `new_unshallow` - Newly no longer shallow objects

## InvalidUserIdentity

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L132)

```python
class InvalidUserIdentity(Exception):
    def __init__(identity):
```

User identity is not of the format 'user <email>'

## MemoryRepo

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L1602)

```python
class MemoryRepo(BaseRepo):
    def __init__():
```

Repo that stores refs, objects, and named files in memory.

MemoryRepos are always bare: they have no working tree and no index, since
those have a stronger dependency on the filesystem.

#### See also

- [BaseRepo](#baserepo)

### MemoryRepo().get_config

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L1675)

```python
def get_config():
```

Retrieve the config object.

Returns: `ConfigFile` object.

### MemoryRepo().get_description

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L1626)

```python
def get_description():
```

### MemoryRepo().get_named_file

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L1651)

```python
def get_named_file(path, basedir=None):
```

Get a file from the control dir with a specific name.

Although the filename should be interpreted as a filename relative to
the control dir in a disk-baked Repo, the object returned need not be
pointing to a file in that location.

#### Arguments

  - `path` - The path to the file, relative to the control dir.
- `Returns` - An open file object, or None if the file does not exist.

### MemoryRepo.init_bare

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L1682)

```python
@classmethod
def init_bare(objects, refs):
```

Create a new bare repository in memory.

#### Arguments

- `objects` - Objects for the new repository,
  as iterable
- `refs` - Refs as dictionary, mapping names
  to object SHA1s

### MemoryRepo().open_index

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L1667)

```python
def open_index():
```

Fail to open index for this repo, since it is bare.

#### Raises

- `NoIndexPresent` - Raised when no index is present

### MemoryRepo().set_description

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L1623)

```python
def set_description(description):
```

## ParentsProvider

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L306)

```python
class ParentsProvider(object):
    def __init__(store, grafts={}, shallows=[]):
```

### ParentsProvider().get_parents

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L312)

```python
def get_parents(commit_id, commit=None):
```

## Repo

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L1035)

```python
class Repo(BaseRepo):
    def __init__(root, object_store=None, bare=None):
```

A git repository backed by local disk.

To open an existing repository, call the contructor with
the path of the repository.

To create a new repository, use the Repo.init class method.

#### See also

- [BaseRepo](#baserepo)

### Repo().clone

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L1369)

```python
def clone(
    target_path,
    mkdir=True,
    bare=False,
    origin=b'origin',
    checkout=None,
    branch=None,
):
```

Clone this repository.

#### Arguments

  - `target_path` - Target path
  - `mkdir` - Create the target directory
  - `bare` - Whether to create a bare repository
  - `checkout` - Whether or not to check-out HEAD after cloning
  - `origin` - Base name for refs in target repository
    cloned from this repository
  - `branch` - Optional branch or tag to be used as HEAD in the new repository
    instead of this repository's HEAD.
- `Returns` - Created repository as [Repo](#repo)

### Repo().close

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L1575)

```python
def close():
```

Close any files opened by this repository.

### Repo().commondir

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L1161)

```python
def commondir():
```

Return the path of the common directory.

For a main working tree, it is identical to controldir().

For a linked working tree, it is the control directory of the
main working tree.

### Repo().controldir

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L1157)

```python
def controldir():
```

Return the path of the control directory.

### Repo.discover

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L1138)

```python
@classmethod
def discover(start='.'):
```

Iterate parent directories to discover a repository

Return a Repo object for the first parent directory that looks like a
Git repository.

#### Arguments

- `start` - The directory to start discovery from (defaults to '.')

### Repo().get_blob_normalizer

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L1585)

```python
def get_blob_normalizer():
```

Return a BlobNormalizer object

### Repo().get_config

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L1455)

```python
def get_config() -> 'ConfigFile':
```

Retrieve the config object.

Returns: `ConfigFile` object for the ``.git/config`` file.

### Repo().get_description

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L1470)

```python
def get_description():
```

Retrieve the description of this repository.

Returns: A string describing the repository or None.

### Repo().get_named_file

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L1211)

```python
def get_named_file(path, basedir=None):
```

Get a file from the control dir with a specific name.

Although the filename should be interpreted as a filename relative to
the control dir in a disk-based Repo, the object returned need not be
pointing to a file in that location.

#### Arguments

  - `path` - The path to the file, relative to the control dir.
  - `basedir` - Optional argument that specifies an alternative to the
    control dir.
- `Returns` - An open file object, or None if the file does not exist.

### Repo().has_index

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L1251)

```python
def has_index():
```

Check if an index is present.

### Repo().index_path

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L1234)

```python
def index_path():
```

Return path to the index file.

### Repo.init

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L1505)

```python
@classmethod
def init(path, mkdir=False):
```

Create a new repository.

#### Arguments

  - `path` - Path in which to create the repository
  - `mkdir` - Whether to create the directory
- `Returns` - [Repo](#repo) instance

### Repo.init_bare

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L1559)

```python
@classmethod
def init_bare(path, mkdir=False, object_store=None):
```

Create a new bare repository.

``path`` should already exist and be an empty directory.

#### Arguments

  - `path` - Path to create bare repository in
- `Returns` - a [Repo](#repo) instance

### Repo().open_index

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L1238)

```python
def open_index() -> 'Index':
```

Open the index for this repository.

#### Raises

  - `NoIndexPresent` - If no index is present
- `Returns` - The matching `Index`

### Repo().reset_index

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L1422)

```python
def reset_index(tree=None):
```

Reset the index back to a specific tree.

#### Arguments

- `tree` - Tree SHA to reset to, None for current HEAD tree.

### Repo().set_description

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L1485)

```python
def set_description(description):
```

Set the description for this repository.

#### Arguments

- `description` - Text to set as description for this repository.

### Repo().stage

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L1257)

```python
def stage(fs_paths):
```

Stage a set of paths.

#### Arguments

- `fs_paths` - List of paths, relative to the repository path

### Repo().unstage

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L1309)

```python
def unstage(fs_paths: List[str]):
```

unstage specific file in the index

#### Arguments

- `fs_paths` - a list of files to unstage,
  relative to the repository path

## UnsupportedVersion

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L1028)

```python
class UnsupportedVersion(Exception):
    def __init__(version):
```

Unsupported repository version.

## check_user_identity

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L213)

```python
def check_user_identity(identity):
```

Verify that a user identity is formatted correctly.

#### Arguments

- `identity` - User identity bytestring

#### Raises

- `InvalidUserIdentity` - Raised when identity is invalid

## get_user_identity

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L163)

```python
def get_user_identity(
    config: 'StackedConfig',
    kind: Optional[str] = None,
) -> bytes:
```

Determine the identity to use for new commits.

If kind is set, this first checks
GIT_${KIND}_NAME and GIT_${KIND}_EMAIL.

If those variables are not set, then it will fall back
to reading the user.name and user.email settings from
the specified configuration.

If that also fails, then it will fall back to using
the current users' identity as obtained from the host
system (e.g. the gecos field, $EMAIL, $USER@$(hostname -f).

#### Arguments

- `kind` - Optional kind to return identity for,
  usually either "AUTHOR" or "COMMITTER".

#### Returns

A user identity

## parse_graftpoints

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L229)

```python
def parse_graftpoints(
    graftpoints: Iterable[bytes],
) -> Dict[bytes, List[bytes]]:
```

Convert a list of graftpoints into a dict

#### Arguments

- `graftpoints` - Iterator of graftpoint lines

Each line is formatted as:
    <commit sha1> <parent sha1> [<parent sha1>]*

Resulting dictionary is:
    - `<commit` *sha1>* - [<parent sha1>*]

https://git.wiki.kernel.org/index.php/GraftPoint

## read_gitfile

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L1013)

```python
def read_gitfile(f):
```

Read a ``.git`` file.

The first line of the file should start with "gitdir: "

#### Arguments

  - `f` - File-like object to read from
- `Returns` - A path

## serialize_graftpoints

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/repo.py#L262)

```python
def serialize_graftpoints(graftpoints: Dict[bytes, List[bytes]]) -> bytes:
```

Convert a dictionary of grafts into string

The graft dictionary is:
    <commit sha1>: [<parent sha1>*]

Each line is formatted as:
    <commit sha1> <parent sha1> [<parent sha1>]*

https://git.wiki.kernel.org/index.php/GraftPoint
