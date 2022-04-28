# Object Store

> Auto-generated documentation for [dulwich.object_store](../../dulwich/object_store.py) module.

Git object store interfaces and implementation.

- [AddOns-Update-Tool](../README.md#addons-update-tool-index) / [Modules](../MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / Object Store
    - [BaseObjectStore](#baseobjectstore)
        - [BaseObjectStore().\_\_contains\_\_](#baseobjectstore__contains__)
        - [BaseObjectStore().\_\_getitem\_\_](#baseobjectstore__getitem__)
        - [BaseObjectStore().\_\_iter\_\_](#baseobjectstore__iter__)
        - [BaseObjectStore().add_object](#baseobjectstoreadd_object)
        - [BaseObjectStore().add_objects](#baseobjectstoreadd_objects)
        - [BaseObjectStore().add_pack_data](#baseobjectstoreadd_pack_data)
        - [BaseObjectStore().close](#baseobjectstoreclose)
        - [BaseObjectStore().contains_loose](#baseobjectstorecontains_loose)
        - [BaseObjectStore().contains_packed](#baseobjectstorecontains_packed)
        - [BaseObjectStore().determine_wants_all](#baseobjectstoredetermine_wants_all)
        - [BaseObjectStore().find_common_revisions](#baseobjectstorefind_common_revisions)
        - [BaseObjectStore().find_missing_objects](#baseobjectstorefind_missing_objects)
        - [BaseObjectStore().generate_pack_contents](#baseobjectstoregenerate_pack_contents)
        - [BaseObjectStore().generate_pack_data](#baseobjectstoregenerate_pack_data)
        - [BaseObjectStore().get_raw](#baseobjectstoreget_raw)
        - [BaseObjectStore().iter_shas](#baseobjectstoreiter_shas)
        - [BaseObjectStore().iter_tree_contents](#baseobjectstoreiter_tree_contents)
        - [BaseObjectStore().packs](#baseobjectstorepacks)
        - [BaseObjectStore().peel_sha](#baseobjectstorepeel_sha)
        - [BaseObjectStore().tree_changes](#baseobjectstoretree_changes)
    - [BucketBasedObjectStore](#bucketbasedobjectstore)
        - [BucketBasedObjectStore().add_pack](#bucketbasedobjectstoreadd_pack)
    - [DiskObjectStore](#diskobjectstore)
        - [DiskObjectStore().add_alternate_path](#diskobjectstoreadd_alternate_path)
        - [DiskObjectStore().add_object](#diskobjectstoreadd_object)
        - [DiskObjectStore().add_pack](#diskobjectstoreadd_pack)
        - [DiskObjectStore().add_thin_pack](#diskobjectstoreadd_thin_pack)
        - [DiskObjectStore().alternates](#diskobjectstorealternates)
        - [DiskObjectStore.from_config](#diskobjectstorefrom_config)
        - [DiskObjectStore.init](#diskobjectstoreinit)
        - [DiskObjectStore().move_in_pack](#diskobjectstoremove_in_pack)
    - [MemoryObjectStore](#memoryobjectstore)
        - [MemoryObjectStore().\_\_delitem\_\_](#memoryobjectstore__delitem__)
        - [MemoryObjectStore().\_\_iter\_\_](#memoryobjectstore__iter__)
        - [MemoryObjectStore().add_object](#memoryobjectstoreadd_object)
        - [MemoryObjectStore().add_objects](#memoryobjectstoreadd_objects)
        - [MemoryObjectStore().add_pack](#memoryobjectstoreadd_pack)
        - [MemoryObjectStore().add_thin_pack](#memoryobjectstoreadd_thin_pack)
        - [MemoryObjectStore().contains_loose](#memoryobjectstorecontains_loose)
        - [MemoryObjectStore().contains_packed](#memoryobjectstorecontains_packed)
        - [MemoryObjectStore().get_raw](#memoryobjectstoreget_raw)
        - [MemoryObjectStore().packs](#memoryobjectstorepacks)
    - [MissingObjectFinder](#missingobjectfinder)
        - [MissingObjectFinder().add_todo](#missingobjectfinderadd_todo)
        - [MissingObjectFinder().next](#missingobjectfindernext)
    - [ObjectIterator](#objectiterator)
        - [ObjectIterator().iterobjects](#objectiteratoriterobjects)
    - [ObjectStoreGraphWalker](#objectstoregraphwalker)
        - [ObjectStoreGraphWalker().ack](#objectstoregraphwalkerack)
        - [ObjectStoreGraphWalker().next](#objectstoregraphwalkernext)
    - [ObjectStoreIterator](#objectstoreiterator)
        - [ObjectStoreIterator().\_\_bool\_\_](#objectstoreiterator__bool__)
        - [ObjectStoreIterator().\_\_contains\_\_](#objectstoreiterator__contains__)
        - [ObjectStoreIterator().\_\_getitem\_\_](#objectstoreiterator__getitem__)
        - [ObjectStoreIterator().\_\_iter\_\_](#objectstoreiterator__iter__)
        - [ObjectStoreIterator().\_\_len\_\_](#objectstoreiterator__len__)
        - [ObjectStoreIterator().empty](#objectstoreiteratorempty)
        - [ObjectStoreIterator().iterobjects](#objectstoreiteratoriterobjects)
        - [ObjectStoreIterator().itershas](#objectstoreiteratoritershas)
    - [OverlayObjectStore](#overlayobjectstore)
        - [OverlayObjectStore().add_object](#overlayobjectstoreadd_object)
        - [OverlayObjectStore().add_objects](#overlayobjectstoreadd_objects)
        - [OverlayObjectStore().contains_loose](#overlayobjectstorecontains_loose)
        - [OverlayObjectStore().contains_packed](#overlayobjectstorecontains_packed)
        - [OverlayObjectStore().get_raw](#overlayobjectstoreget_raw)
        - [OverlayObjectStore().packs](#overlayobjectstorepacks)
    - [PackBasedObjectStore](#packbasedobjectstore)
        - [PackBasedObjectStore().\_\_contains\_\_](#packbasedobjectstore__contains__)
        - [PackBasedObjectStore().\_\_iter\_\_](#packbasedobjectstore__iter__)
        - [PackBasedObjectStore().add_objects](#packbasedobjectstoreadd_objects)
        - [PackBasedObjectStore().alternates](#packbasedobjectstorealternates)
        - [PackBasedObjectStore().close](#packbasedobjectstoreclose)
        - [PackBasedObjectStore().contains_loose](#packbasedobjectstorecontains_loose)
        - [PackBasedObjectStore().contains_packed](#packbasedobjectstorecontains_packed)
        - [PackBasedObjectStore().get_raw](#packbasedobjectstoreget_raw)
        - [PackBasedObjectStore().pack_loose_objects](#packbasedobjectstorepack_loose_objects)
        - [PackBasedObjectStore().packs](#packbasedobjectstorepacks)
        - [PackBasedObjectStore().repack](#packbasedobjectstorerepack)
    - [commit_tree_changes](#commit_tree_changes)
    - [read_packs_file](#read_packs_file)
    - [tree_lookup_path](#tree_lookup_path)

#### Attributes

- `PACK_MODE` - use permissions consistent with Git; just readable by everyone
  would requite some rather significant adjustments to the test suite: `292 if sys.platform != 'win32' else 420`

## BaseObjectStore

[[find in source code]](../../dulwich/object_store.py#L79)

```python
class BaseObjectStore(object):
```

Object store interface.

### BaseObjectStore().\_\_contains\_\_

[[find in source code]](../../dulwich/object_store.py#L115)

```python
def __contains__(sha):
```

Check if a particular object is present by SHA1.

This method makes no distinction between loose and packed objects.

### BaseObjectStore().\_\_getitem\_\_

[[find in source code]](../../dulwich/object_store.py#L136)

```python
def __getitem__(sha):
```

Obtain an object by SHA1.

### BaseObjectStore().\_\_iter\_\_

[[find in source code]](../../dulwich/object_store.py#L141)

```python
def __iter__():
```

Iterate over the SHAs that are present in this store.

### BaseObjectStore().add_object

[[find in source code]](../../dulwich/object_store.py#L145)

```python
def add_object(obj):
```

Add a single object to this object store.

### BaseObjectStore().add_objects

[[find in source code]](../../dulwich/object_store.py#L149)

```python
def add_objects(objects, progress=None):
```

Add a set of objects to this object store.

#### Arguments

- `objects` - Iterable over a list of (object, path) tuples

### BaseObjectStore().add_pack_data

[[find in source code]](../../dulwich/object_store.py#L157)

```python
def add_pack_data(count, pack_data, progress=None):
```

Add pack data to this object store.

#### Arguments

- `count` - Number of items to add
- `pack_data` - Iterator over pack data tuples

### BaseObjectStore().close

[[find in source code]](../../dulwich/object_store.py#L399)

```python
def close():
```

Close any files opened by this object store.

### BaseObjectStore().contains_loose

[[find in source code]](../../dulwich/object_store.py#L107)

```python
def contains_loose(sha):
```

Check if a particular object is present by SHA1 and is loose.

### BaseObjectStore().contains_packed

[[find in source code]](../../dulwich/object_store.py#L111)

```python
def contains_packed(sha):
```

Check if a particular object is present by SHA1 and is packed.

### BaseObjectStore().determine_wants_all

[[find in source code]](../../dulwich/object_store.py#L82)

```python
def determine_wants_all(refs, depth=None):
```

### BaseObjectStore().find_common_revisions

[[find in source code]](../../dulwich/object_store.py#L270)

```python
def find_common_revisions(graphwalker):
```

Find which revisions this store has in common using graphwalker.

#### Arguments

  - `graphwalker` - A graphwalker object.
- `Returns` - List of SHAs that are in common

### BaseObjectStore().find_missing_objects

[[find in source code]](../../dulwich/object_store.py#L235)

```python
def find_missing_objects(
    haves,
    wants,
    shallow=None,
    progress=None,
    get_tagged=None,
    get_parents=lambda commit: commit.parents,
    depth=None,
):
```

Find the missing objects required for a set of revisions.

#### Arguments

  - `haves` - Iterable over SHAs already in common.
  - `wants` - Iterable over SHAs of objects to fetch.
  - `shallow` - Set of shallow commit SHA1s to skip
  - `progress` - Simple progress function that will be called with
    updated progress strings.
  - `get_tagged` - Function that returns a dict of pointed-to sha ->
    tag sha for including tags.
  - `get_parents` - Optional function for getting the parents of a
    commit.
- `Returns` - Iterator over (sha, path) pairs.

### BaseObjectStore().generate_pack_contents

[[find in source code]](../../dulwich/object_store.py#L286)

```python
def generate_pack_contents(have, want, shallow=None, progress=None):
```

Iterate over the contents of a pack file.

#### Arguments

- `have` - List of SHA1s of objects that should not be sent
- `want` - List of SHA1s of objects that should be sent
- `shallow` - Set of shallow commit SHA1s to skip
- `progress` - Optional progress reporting method

### BaseObjectStore().generate_pack_data

[[find in source code]](../../dulwich/object_store.py#L298)

```python
def generate_pack_data(
    have,
    want,
    shallow=None,
    progress=None,
    ofs_delta=True,
):
```

Generate pack data objects for a set of wants/haves.

#### Arguments

- `have` - List of SHA1s of objects that should not be sent
- `want` - List of SHA1s of objects that should be sent
- `shallow` - Set of shallow commit SHA1s to skip
- `ofs_delta` - Whether OFS deltas can be included
- `progress` - Optional progress reporting method

### BaseObjectStore().get_raw

[[find in source code]](../../dulwich/object_store.py#L127)

```python
def get_raw(name):
```

Obtain the raw text for an object.

#### Arguments

  - `name` - sha for the object.
- `Returns` - tuple with numeric type and object contents.

### BaseObjectStore().iter_shas

[[find in source code]](../../dulwich/object_store.py#L98)

```python
def iter_shas(shas):
```

Iterate over the objects for the specified shas.

#### Arguments

  - `shas` - Iterable object with SHAs
- `Returns` - Object iterator

### BaseObjectStore().iter_tree_contents

[[find in source code]](../../dulwich/object_store.py#L218)

```python
def iter_tree_contents(tree_id, include_trees=False):
```

Iterate the contents of a tree and all subtrees.

Iteration is depth-first pre-order, as in e.g. os.walk.

#### Arguments

  - `tree_id` - SHA1 of the tree.
  - `include_trees` - If True, include tree objects in the iteration.
- `Returns` - Iterator over TreeEntry namedtuples for all the objects in a
    tree.

### BaseObjectStore().packs

[[find in source code]](../../dulwich/object_store.py#L122)

```python
@property
def packs():
```

Iterable of pack objects.

### BaseObjectStore().peel_sha

[[find in source code]](../../dulwich/object_store.py#L315)

```python
def peel_sha(sha):
```

Peel all tags from a SHA.

#### Arguments

  - `sha` - The object SHA to peel.
- `Returns` - The fully-peeled SHA1 of a tag object, after peeling all
    intermediate tags; if the original ref does not point to a tag,
    this will equal the original SHA1.

### BaseObjectStore().tree_changes

[[find in source code]](../../dulwich/object_store.py#L182)

```python
def tree_changes(
    source,
    target,
    want_unchanged=False,
    include_trees=False,
    change_type_same=False,
    rename_detector=None,
):
```

Find the differences between the contents of two trees

#### Arguments

  - `source` - SHA1 of the source tree
  - `target` - SHA1 of the target tree
  - `want_unchanged` - Whether unchanged files should be reported
  - `include_trees` - Whether to include trees
  - `change_type_same` - Whether to report files changing
    type in the same entry.
- `Returns` - Iterator over tuples with
    (oldpath, newpath), (oldmode, newmode), (oldsha, newsha)

## BucketBasedObjectStore

[[find in source code]](../../dulwich/object_store.py#L1549)

```python
class BucketBasedObjectStore(PackBasedObjectStore):
```

Object store implementation that uses a bucket store like S3 as backend.

#### See also

- [PackBasedObjectStore](#packbasedobjectstore)

### BucketBasedObjectStore().add_pack

[[find in source code]](../../dulwich/object_store.py#L1590)

```python
def add_pack():
```

Add a new pack to this object store.

Returns: Fileobject to write to, a commit function to
    call when the pack is finished and an abort
    function.

## DiskObjectStore

[[find in source code]](../../dulwich/object_store.py#L604)

```python
class DiskObjectStore(PackBasedObjectStore):
    def __init__(path, loose_compression_level=-1, pack_compression_level=-1):
```

Git-style object store that exists on disk.

#### See also

- [PackBasedObjectStore](#packbasedobjectstore)

### DiskObjectStore().add_alternate_path

[[find in source code]](../../dulwich/object_store.py#L677)

```python
def add_alternate_path(path):
```

Add an alternate path to this object store.

### DiskObjectStore().add_object

[[find in source code]](../../dulwich/object_store.py#L925)

```python
def add_object(obj):
```

Add a single object to this object store.

#### Arguments

- `obj` - Object to add

### DiskObjectStore().add_pack

[[find in source code]](../../dulwich/object_store.py#L896)

```python
def add_pack():
```

Add a new pack to this object store.

Returns: Fileobject to write to, a commit function to
    call when the pack is finished and an abort
    function.

### DiskObjectStore().add_thin_pack

[[find in source code]](../../dulwich/object_store.py#L837)

```python
def add_thin_pack(read_all, read_some):
```

Add a new thin pack to this object store.

Thin packs are packs that contain deltas with parents that exist
outside the pack. They should never be placed in the object store
directly, and always indexed and completed as they are copied.

#### Arguments

  - `read_all` - Read function that blocks until the number of
    requested bytes are read.
  - `read_some` - Read function that returns at least one byte, but may
    not return the number of bytes requested.
- `Returns` - A Pack object pointing at the now-completed thin pack in the
    objects/pack directory.

### DiskObjectStore().alternates

[[find in source code]](../../dulwich/object_store.py#L651)

```python
@property
def alternates():
```

### DiskObjectStore.from_config

[[find in source code]](../../dulwich/object_store.py#L629)

```python
@classmethod
def from_config(path, config):
```

### DiskObjectStore.init

[[find in source code]](../../dulwich/object_store.py#L946)

```python
@classmethod
def init(path):
```

### DiskObjectStore().move_in_pack

[[find in source code]](../../dulwich/object_store.py#L864)

```python
def move_in_pack(path):
```

Move a specific file containing a pack into the pack directory.

Note: The file should be on the same file system as the
    packs directory.

#### Arguments

- `path` - Path to the pack file.

## MemoryObjectStore

[[find in source code]](../../dulwich/object_store.py#L957)

```python
class MemoryObjectStore(BaseObjectStore):
    def __init__():
```

Object store that keeps all objects in memory.

#### See also

- [BaseObjectStore](#baseobjectstore)

### MemoryObjectStore().\_\_delitem\_\_

[[find in source code]](../../dulwich/object_store.py#L1003)

```python
def __delitem__(name):
```

Delete an object from this store, for testing only.

### MemoryObjectStore().\_\_iter\_\_

[[find in source code]](../../dulwich/object_store.py#L981)

```python
def __iter__():
```

Iterate over the SHAs that are present in this store.

### MemoryObjectStore().add_object

[[find in source code]](../../dulwich/object_store.py#L1007)

```python
def add_object(obj):
```

Add a single object to this object store.

### MemoryObjectStore().add_objects

[[find in source code]](../../dulwich/object_store.py#L1011)

```python
def add_objects(objects, progress=None):
```

Add a set of objects to this object store.

#### Arguments

- `objects` - Iterable over a list of (object, path) tuples

### MemoryObjectStore().add_pack

[[find in source code]](../../dulwich/object_store.py#L1020)

```python
def add_pack():
```

Add a new pack to this object store.

Because this object store doesn't support packs, we extract and add the
individual objects.

Returns: Fileobject to write to and a commit function to
    call when the pack is finished.

### MemoryObjectStore().add_thin_pack

[[find in source code]](../../dulwich/object_store.py#L1066)

```python
def add_thin_pack(read_all, read_some):
```

Add a new thin pack to this object store.

Thin packs are packs that contain deltas with parents that exist
outside the pack. Because this object store doesn't support packs, we
extract and add the individual objects.

#### Arguments

- `read_all` - Read function that blocks until the number of
  requested bytes are read.
- `read_some` - Read function that returns at least one byte, but may
  not return the number of bytes requested.

### MemoryObjectStore().contains_loose

[[find in source code]](../../dulwich/object_store.py#L973)

```python
def contains_loose(sha):
```

Check if a particular object is present by SHA1 and is loose.

### MemoryObjectStore().contains_packed

[[find in source code]](../../dulwich/object_store.py#L977)

```python
def contains_packed(sha):
```

Check if a particular object is present by SHA1 and is packed.

### MemoryObjectStore().get_raw

[[find in source code]](../../dulwich/object_store.py#L990)

```python
def get_raw(name):
```

Obtain the raw text for an object.

#### Arguments

  - `name` - sha for the object.
- `Returns` - tuple with numeric type and object contents.

### MemoryObjectStore().packs

[[find in source code]](../../dulwich/object_store.py#L985)

```python
@property
def packs():
```

List with pack objects.

## MissingObjectFinder

[[find in source code]](../../dulwich/object_store.py#L1252)

```python
class MissingObjectFinder(object):
    def __init__(
        object_store,
        haves,
        wants,
        shallow=None,
        progress=None,
        get_tagged=None,
        get_parents=lambda commit: commit.parents,
    ):
```

Find the objects missing from another object store.

#### Arguments

- `object_store` - Object store containing at least all objects to be
  sent
- `haves` - SHA1s of commits not to send (already present in target)
- `wants` - SHA1s of commits to send
- `progress` - Optional function to report progress to.
- `get_tagged` - Function that returns a dict of pointed-to sha -> tag
  sha for including tags.
- `get_parents` - Optional function for getting the parents of a commit.
- `tagged` - dict of pointed-to sha -> tag sha for including tags

### MissingObjectFinder().add_todo

[[find in source code]](../../dulwich/object_store.py#L1334)

```python
def add_todo(entries):
```

### MissingObjectFinder().next

[[find in source code]](../../dulwich/object_store.py#L1339)

```python
def next():
```

## ObjectIterator

[[find in source code]](../../dulwich/object_store.py#L1094)

```python
class ObjectIterator(object):
```

Interface for iterating over objects.

### ObjectIterator().iterobjects

[[find in source code]](../../dulwich/object_store.py#L1097)

```python
def iterobjects():
```

## ObjectStoreGraphWalker

[[find in source code]](../../dulwich/object_store.py#L1371)

```python
class ObjectStoreGraphWalker(object):
    def __init__(local_heads, get_parents, shallow=None):
```

Graph walker that finds what commits are missing from an object store.

#### Attributes

- `heads` - Revisions without descendants in the local repo
- `get_parents` - Function to retrieve parents in the local repo

### ObjectStoreGraphWalker().ack

[[find in source code]](../../dulwich/object_store.py#L1393)

```python
def ack(sha):
```

Ack that a revision and its ancestors are present in the source.

### ObjectStoreGraphWalker().next

[[find in source code]](../../dulwich/object_store.py#L1419)

```python
def next():
```

Iterate over ancestors of heads in the target.

## ObjectStoreIterator

[[find in source code]](../../dulwich/object_store.py#L1101)

```python
class ObjectStoreIterator(ObjectIterator):
    def __init__(store, sha_iter):
```

ObjectIterator that works on top of an ObjectStore.

#### See also

- [ObjectIterator](#objectiterator)

### ObjectStoreIterator().\_\_bool\_\_

[[find in source code]](../../dulwich/object_store.py#L1175)

```python
def __bool__():
```

Indicate whether this object has contents.

### ObjectStoreIterator().\_\_contains\_\_

[[find in source code]](../../dulwich/object_store.py#L1133)

```python
def __contains__(needle):
```

Check if an object is present.

Note: This checks if the object is present in
    the underlying object store, not if it would
    be yielded by the iterator.

#### Arguments

- `needle` - SHA1 of the object to check for

### ObjectStoreIterator().\_\_getitem\_\_

[[find in source code]](../../dulwich/object_store.py#L1147)

```python
def __getitem__(key):
```

Find an object by SHA1.

Note: This retrieves the object from the underlying
    object store. It will also succeed if the object would
    not be returned by the iterator.

### ObjectStoreIterator().\_\_iter\_\_

[[find in source code]](../../dulwich/object_store.py#L1115)

```python
def __iter__():
```

Yield tuple with next object and path.

### ObjectStoreIterator().\_\_len\_\_

[[find in source code]](../../dulwich/object_store.py#L1156)

```python
def __len__():
```

Return the number of objects.

### ObjectStoreIterator().empty

[[find in source code]](../../dulwich/object_store.py#L1160)

```python
def empty():
```

### ObjectStoreIterator().iterobjects

[[find in source code]](../../dulwich/object_store.py#L1120)

```python
def iterobjects():
```

Iterate over just the objects.

### ObjectStoreIterator().itershas

[[find in source code]](../../dulwich/object_store.py#L1125)

```python
def itershas():
```

Iterate over the SHAs.

## OverlayObjectStore

[[find in source code]](../../dulwich/object_store.py#L1485)

```python
class OverlayObjectStore(BaseObjectStore):
    def __init__(bases, add_store=None):
```

Object store that can overlay multiple object stores.

#### See also

- [BaseObjectStore](#baseobjectstore)

### OverlayObjectStore().add_object

[[find in source code]](../../dulwich/object_store.py#L1492)

```python
def add_object(object):
```

### OverlayObjectStore().add_objects

[[find in source code]](../../dulwich/object_store.py#L1497)

```python
def add_objects(objects, progress=None):
```

### OverlayObjectStore().contains_loose

[[find in source code]](../../dulwich/object_store.py#L1531)

```python
def contains_loose(sha):
```

### OverlayObjectStore().contains_packed

[[find in source code]](../../dulwich/object_store.py#L1525)

```python
def contains_packed(sha):
```

### OverlayObjectStore().get_raw

[[find in source code]](../../dulwich/object_store.py#L1517)

```python
def get_raw(sha_id):
```

### OverlayObjectStore().packs

[[find in source code]](../../dulwich/object_store.py#L1502)

```python
@property
def packs():
```

## PackBasedObjectStore

[[find in source code]](../../dulwich/object_store.py#L404)

```python
class PackBasedObjectStore(BaseObjectStore):
    def __init__(pack_compression_level=-1):
```

#### See also

- [BaseObjectStore](#baseobjectstore)

### PackBasedObjectStore().\_\_contains\_\_

[[find in source code]](../../dulwich/object_store.py#L426)

```python
def __contains__(sha):
```

Check if a particular object is present by SHA1.

This method makes no distinction between loose and packed objects.

### PackBasedObjectStore().\_\_iter\_\_

[[find in source code]](../../dulwich/object_store.py#L529)

```python
def __iter__():
```

Iterate over the SHAs that are present in this store.

### PackBasedObjectStore().add_objects

[[find in source code]](../../dulwich/object_store.py#L591)

```python
def add_objects(objects, progress=None):
```

Add a set of objects to this object store.

#### Arguments

  - `objects` - Iterable over (object, path) tuples, should support
    __len__.
- `Returns` - Pack object of the objects written.

### PackBasedObjectStore().alternates

[[find in source code]](../../dulwich/object_store.py#L409)

```python
@property
def alternates():
```

### PackBasedObjectStore().close

[[find in source code]](../../dulwich/object_store.py#L459)

```python
def close():
```

### PackBasedObjectStore().contains_loose

[[find in source code]](../../dulwich/object_store.py#L543)

```python
def contains_loose(sha):
```

Check if a particular object is present by SHA1 and is loose.

This does not check alternates.

### PackBasedObjectStore().contains_packed

[[find in source code]](../../dulwich/object_store.py#L413)

```python
def contains_packed(sha):
```

Check if a particular object is present by SHA1 and is packed.

This does not check alternates.

### PackBasedObjectStore().get_raw

[[find in source code]](../../dulwich/object_store.py#L550)

```python
def get_raw(name):
```

Obtain the raw fulltext for an object.

#### Arguments

  - `name` - sha for the object.
- `Returns` - tuple with numeric type and object contents.

### PackBasedObjectStore().pack_loose_objects

[[find in source code]](../../dulwich/object_store.py#L488)

```python
def pack_loose_objects():
```

Pack loose objects.

Returns: Number of objects packed

### PackBasedObjectStore().packs

[[find in source code]](../../dulwich/object_store.py#L462)

```python
@property
def packs():
```

List with pack objects.

### PackBasedObjectStore().repack

[[find in source code]](../../dulwich/object_store.py#L501)

```python
def repack():
```

Repack the packs in this repository.

Note that this implementation is fairly naive and currently keeps all
objects in memory while it repacks.

## commit_tree_changes

[[find in source code]](../../dulwich/object_store.py#L1435)

```python
def commit_tree_changes(object_store, tree, changes):
```

Commit a specified set of changes to a tree structure.

This will apply a set of changes on top of an existing tree, storing new
objects in object_store.

changes are a list of tuples with (path, mode, object_sha).
Paths can be both blobs and trees. See the mode and
object sha to None deletes the path.

This method works especially well if there are only a small
number of changes to a big tree. For a large number of changes
to a large tree, use e.g. commit_tree.

#### Arguments

  - `object_store` - Object store to store new objects in
    and retrieve old ones from.
  - `tree` - Original tree root
  - `changes` - changes to apply
- `Returns` - New tree root object

## read_packs_file

[[find in source code]](../../dulwich/object_store.py#L1538)

```python
def read_packs_file(f):
```

Yield the packs listed in a packs file.

## tree_lookup_path

[[find in source code]](../../dulwich/object_store.py#L1180)

```python
def tree_lookup_path(lookup_obj, root_sha, path):
```

Look up an object in a Git tree.

#### Arguments

  - `lookup_obj` - Callback for retrieving object by SHA1
  - `root_sha` - SHA1 of the root tree
  - `path` - Path to lookup
- `Returns` - A tuple of (mode, SHA) of the resulting path.
