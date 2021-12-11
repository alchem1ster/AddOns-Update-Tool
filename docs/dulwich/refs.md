# Refs

> Auto-generated documentation for [dulwich.refs](blob/master/dulwich/refs.py) module.

Ref handling.

- [Addons-update-tool](..\README.md#addons-update-tool) / [Modules](..\MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / Refs
    - [DictRefsContainer](#dictrefscontainer)
        - [DictRefsContainer().add_if_new](#dictrefscontaineradd_if_new)
        - [DictRefsContainer().allkeys](#dictrefscontainerallkeys)
        - [DictRefsContainer().get_packed_refs](#dictrefscontainerget_packed_refs)
        - [DictRefsContainer().get_peeled](#dictrefscontainerget_peeled)
        - [DictRefsContainer().read_loose_ref](#dictrefscontainerread_loose_ref)
        - [DictRefsContainer().remove_if_equals](#dictrefscontainerremove_if_equals)
        - [DictRefsContainer().set_if_equals](#dictrefscontainerset_if_equals)
        - [DictRefsContainer().set_symbolic_ref](#dictrefscontainerset_symbolic_ref)
        - [DictRefsContainer().watch](#dictrefscontainerwatch)
    - [DiskRefsContainer](#diskrefscontainer)
        - [DiskRefsContainer().add_if_new](#diskrefscontaineradd_if_new)
        - [DiskRefsContainer().allkeys](#diskrefscontainerallkeys)
        - [DiskRefsContainer().get_packed_refs](#diskrefscontainerget_packed_refs)
        - [DiskRefsContainer().get_peeled](#diskrefscontainerget_peeled)
        - [DiskRefsContainer().read_loose_ref](#diskrefscontainerread_loose_ref)
        - [DiskRefsContainer().refpath](#diskrefscontainerrefpath)
        - [DiskRefsContainer().remove_if_equals](#diskrefscontainerremove_if_equals)
        - [DiskRefsContainer().set_if_equals](#diskrefscontainerset_if_equals)
        - [DiskRefsContainer().set_symbolic_ref](#diskrefscontainerset_symbolic_ref)
        - [DiskRefsContainer().subkeys](#diskrefscontainersubkeys)
        - [DiskRefsContainer().watch](#diskrefscontainerwatch)
    - [InfoRefsContainer](#inforefscontainer)
        - [InfoRefsContainer().allkeys](#inforefscontainerallkeys)
        - [InfoRefsContainer().get_packed_refs](#inforefscontainerget_packed_refs)
        - [InfoRefsContainer().get_peeled](#inforefscontainerget_peeled)
        - [InfoRefsContainer().read_loose_ref](#inforefscontainerread_loose_ref)
    - [RefsContainer](#refscontainer)
        - [RefsContainer().\_\_delitem\_\_](#refscontainer__delitem__)
        - [RefsContainer().\_\_getitem\_\_](#refscontainer__getitem__)
        - [RefsContainer().\_\_setitem\_\_](#refscontainer__setitem__)
        - [RefsContainer().add_if_new](#refscontaineradd_if_new)
        - [RefsContainer().allkeys](#refscontainerallkeys)
        - [RefsContainer().as_dict](#refscontaineras_dict)
        - [RefsContainer().follow](#refscontainerfollow)
        - [RefsContainer().get_packed_refs](#refscontainerget_packed_refs)
        - [RefsContainer().get_peeled](#refscontainerget_peeled)
        - [RefsContainer().get_symrefs](#refscontainerget_symrefs)
        - [RefsContainer().import_refs](#refscontainerimport_refs)
        - [RefsContainer().keys](#refscontainerkeys)
        - [RefsContainer().read_loose_ref](#refscontainerread_loose_ref)
        - [RefsContainer().read_ref](#refscontainerread_ref)
        - [RefsContainer().remove_if_equals](#refscontainerremove_if_equals)
        - [RefsContainer().set_if_equals](#refscontainerset_if_equals)
        - [RefsContainer().set_symbolic_ref](#refscontainerset_symbolic_ref)
        - [RefsContainer().subkeys](#refscontainersubkeys)
        - [RefsContainer().watch](#refscontainerwatch)
    - [check_ref_format](#check_ref_format)
    - [is_local_branch](#is_local_branch)
    - [parse_symref_value](#parse_symref_value)
    - [read_info_refs](#read_info_refs)
    - [read_packed_refs](#read_packed_refs)
    - [read_packed_refs_with_peeled](#read_packed_refs_with_peeled)
    - [strip_peeled_refs](#strip_peeled_refs)
    - [write_info_refs](#write_info_refs)
    - [write_packed_refs](#write_packed_refs)

## DictRefsContainer

[[find in source code]](blob/master/dulwich/refs.py#L460)

```python
class DictRefsContainer(RefsContainer):
    def __init__(refs, logger=None):
```

RefsContainer backed by a simple dict.

This container does not support symbolic or packed references and is not
threadsafe.

#### See also

- [RefsContainer](#refscontainer)

### DictRefsContainer().add_if_new

[[find in source code]](blob/master/dulwich/refs.py#L541)

```python
def add_if_new(
    name,
    ref,
    committer=None,
    timestamp=None,
    timezone=None,
    message=None,
):
```

### DictRefsContainer().allkeys

[[find in source code]](blob/master/dulwich/refs.py#L473)

```python
def allkeys():
```

### DictRefsContainer().get_packed_refs

[[find in source code]](blob/master/dulwich/refs.py#L479)

```python
def get_packed_refs():
```

### DictRefsContainer().get_peeled

[[find in source code]](blob/master/dulwich/refs.py#L593)

```python
def get_peeled(name):
```

### DictRefsContainer().read_loose_ref

[[find in source code]](blob/master/dulwich/refs.py#L476)

```python
def read_loose_ref(name):
```

### DictRefsContainer().remove_if_equals

[[find in source code]](blob/master/dulwich/refs.py#L565)

```python
def remove_if_equals(
    name,
    old_ref,
    committer=None,
    timestamp=None,
    timezone=None,
    message=None,
):
```

### DictRefsContainer().set_if_equals

[[find in source code]](blob/master/dulwich/refs.py#L512)

```python
def set_if_equals(
    name,
    old_ref,
    new_ref,
    committer=None,
    timestamp=None,
    timezone=None,
    message=None,
):
```

### DictRefsContainer().set_symbolic_ref

[[find in source code]](blob/master/dulwich/refs.py#L489)

```python
def set_symbolic_ref(
    name,
    other,
    committer=None,
    timestamp=None,
    timezone=None,
    message=None,
):
```

### DictRefsContainer().watch

[[find in source code]](blob/master/dulwich/refs.py#L486)

```python
def watch():
```

## DiskRefsContainer

[[find in source code]](blob/master/dulwich/refs.py#L686)

```python
class DiskRefsContainer(RefsContainer):
    def __init__(path, worktree_path=None, logger=None):
```

Refs container that reads refs from disk.

#### See also

- [RefsContainer](#refscontainer)

### DiskRefsContainer().add_if_new

[[find in source code]](blob/master/dulwich/refs.py#L957)

```python
def add_if_new(
    name,
    ref,
    committer=None,
    timestamp=None,
    timezone=None,
    message=None,
):
```

Add a new reference only if it does not already exist.

This method follows symrefs, and only ensures that the last ref in the
chain does not exist.

#### Arguments

  - `name` - The refname to set.
  - `ref` - The new sha the refname will refer to.
  - `message` - Optional message for reflog
- `Returns` - True if the add was successful, False otherwise.

### DiskRefsContainer().allkeys

[[find in source code]](blob/master/dulwich/refs.py#L724)

```python
def allkeys():
```

### DiskRefsContainer().get_packed_refs

[[find in source code]](blob/master/dulwich/refs.py#L752)

```python
def get_packed_refs():
```

Get contents of the packed-refs file.

Returns: Dictionary mapping ref names to SHA1s

Note: Will return an empty dictionary when no packed-refs file is
    present.

### DiskRefsContainer().get_peeled

[[find in source code]](blob/master/dulwich/refs.py#L784)

```python
def get_peeled(name):
```

Return the cached peeled value of a ref, if available.

#### Arguments

  - `name` - Name of the ref to peel
- `Returns` - The peeled value of the ref. If the ref is known not point to
    a tag, this will be the SHA the ref refers to. If the ref may point
    to a tag, but no cached information is available, None is returned.

### DiskRefsContainer().read_loose_ref

[[find in source code]](blob/master/dulwich/refs.py#L803)

```python
def read_loose_ref(name):
```

Read a reference file and return its contents.

If the reference file a symbolic reference, only read the first line of
the file. Otherwise, only read the first 40 bytes.

#### Arguments

  - `name` - the refname to read, relative to refpath
- `Returns` - The contents of the ref file, or None if the file does not
    exist.

#### Raises

- `IOError` - if any other error occurs

### DiskRefsContainer().refpath

[[find in source code]](blob/master/dulwich/refs.py#L741)

```python
def refpath(name):
```

Return the disk path of a ref.

### DiskRefsContainer().remove_if_equals

[[find in source code]](blob/master/dulwich/refs.py#L1008)

```python
def remove_if_equals(
    name,
    old_ref,
    committer=None,
    timestamp=None,
    timezone=None,
    message=None,
):
```

Remove a refname only if it currently equals old_ref.

This method does not follow symbolic references. It can be used to
perform an atomic compare-and-delete operation.

#### Arguments

  - `name` - The refname to delete.
  - `old_ref` - The old sha the refname must refer to, or None to
    delete unconditionally.
  - `message` - Optional message
- `Returns` - True if the delete was successful, False otherwise.

### DiskRefsContainer().set_if_equals

[[find in source code]](blob/master/dulwich/refs.py#L888)

```python
def set_if_equals(
    name,
    old_ref,
    new_ref,
    committer=None,
    timestamp=None,
    timezone=None,
    message=None,
):
```

Set a refname to new_ref only if it currently equals old_ref.

This method follows all symbolic references, and can be used to perform
an atomic compare-and-swap operation.

#### Arguments

  - `name` - The refname to set.
  - `old_ref` - The old sha the refname must refer to, or None to set
    unconditionally.
  - `new_ref` - The new sha the refname will refer to.
  - `message` - Set message for reflog
- `Returns` - True if the set was successful, False otherwise.

### DiskRefsContainer().set_symbolic_ref

[[find in source code]](blob/master/dulwich/refs.py#L850)

```python
def set_symbolic_ref(
    name,
    other,
    committer=None,
    timestamp=None,
    timezone=None,
    message=None,
):
```

Make a ref point at another ref.

#### Arguments

- `name` - Name of the ref to set
- `other` - Name of the ref to point at
- `message` - Optional message to describe the change

### DiskRefsContainer().subkeys

[[find in source code]](blob/master/dulwich/refs.py#L705)

```python
def subkeys(base):
```

### DiskRefsContainer().watch

[[find in source code]](blob/master/dulwich/refs.py#L1085)

```python
def watch():
```

## InfoRefsContainer

[[find in source code]](blob/master/dulwich/refs.py#L608)

```python
class InfoRefsContainer(RefsContainer):
    def __init__(f):
```

Refs container that reads refs from a info/refs file.

#### See also

- [RefsContainer](#refscontainer)

### InfoRefsContainer().allkeys

[[find in source code]](blob/master/dulwich/refs.py#L626)

```python
def allkeys():
```

### InfoRefsContainer().get_packed_refs

[[find in source code]](blob/master/dulwich/refs.py#L632)

```python
def get_packed_refs():
```

### InfoRefsContainer().get_peeled

[[find in source code]](blob/master/dulwich/refs.py#L635)

```python
def get_peeled(name):
```

### InfoRefsContainer().read_loose_ref

[[find in source code]](blob/master/dulwich/refs.py#L629)

```python
def read_loose_ref(name):
```

## RefsContainer

[[find in source code]](blob/master/dulwich/refs.py#L95)

```python
class RefsContainer(object):
    def __init__(logger=None):
```

A container for refs.

### RefsContainer().\_\_delitem\_\_

[[find in source code]](blob/master/dulwich/refs.py#L400)

```python
def __delitem__(name):
```

Remove a refname.

This method does not follow symbolic references, even if applicable for
the subclass.

Note: This method unconditionally deletes the contents of a reference.
    To delete atomically only if the reference has not changed, use
    remove_if_equals().

#### Arguments

- `name` - The refname to delete.

### RefsContainer().\_\_getitem\_\_

[[find in source code]](blob/master/dulwich/refs.py#L314)

```python
def __getitem__(name):
```

Get the SHA1 for a reference name.

This method follows all symbolic references.

### RefsContainer().\_\_setitem\_\_

[[find in source code]](blob/master/dulwich/refs.py#L360)

```python
def __setitem__(name, ref):
```

Set a reference name to point to the given SHA1.

This method follows all symbolic references if applicable for the
subclass.

Note: This method unconditionally overwrites the contents of a
    reference. To update atomically only if the reference has not
    changed, use set_if_equals().

#### Arguments

- `name` - The refname to set.
- `ref` - The new sha the refname will refer to.

### RefsContainer().add_if_new

[[find in source code]](blob/master/dulwich/refs.py#L350)

```python
def add_if_new(name, ref):
```

Add a new reference only if it does not already exist.

#### Arguments

- `name` - Ref name
- `ref` - Ref value
- `message` - Message for reflog

### RefsContainer().allkeys

[[find in source code]](blob/master/dulwich/refs.py#L185)

```python
def allkeys():
```

All refs present in this container.

### RefsContainer().as_dict

[[find in source code]](blob/master/dulwich/refs.py#L220)

```python
def as_dict(base=None):
```

Return the contents of this container as a dictionary.

### RefsContainer().follow

[[find in source code]](blob/master/dulwich/refs.py#L277)

```python
def follow(name):
```

Follow a reference name.

Returns: a tuple of (refnames, sha), wheres refnames are the names of
    references in the chain

### RefsContainer().get_packed_refs

[[find in source code]](blob/master/dulwich/refs.py#L135)

```python
def get_packed_refs():
```

Get contents of the packed-refs file.

Returns: Dictionary mapping ref names to SHA1s

Note: Will return an empty dictionary when no packed-refs file is
    present.

### RefsContainer().get_peeled

[[find in source code]](blob/master/dulwich/refs.py#L145)

```python
def get_peeled(name):
```

Return the cached peeled value of a ref, if available.

#### Arguments

  - `name` - Name of the ref to peel
- `Returns` - The peeled value of the ref. If the ref is known not point to
    a tag, this will be the SHA the ref refers to. If the ref may point
    to a tag, but no cached information is available, None is returned.

### RefsContainer().get_symrefs

[[find in source code]](blob/master/dulwich/refs.py#L415)

```python
def get_symrefs():
```

Get a dict with all symrefs in this container.

Returns: Dictionary mapping source ref to target ref

### RefsContainer().import_refs

[[find in source code]](blob/master/dulwich/refs.py#L156)

```python
def import_refs(
    base,
    other,
    committer=None,
    timestamp=None,
    timezone=None,
    message=None,
    prune=False,
):
```

### RefsContainer().keys

[[find in source code]](blob/master/dulwich/refs.py#L192)

```python
def keys(base=None):
```

Refs present in this container.

#### Arguments

  - `base` - An optional base to return refs under.
- `Returns` - An unsorted set of valid refs in this container, including
    packed refs.

### RefsContainer().read_loose_ref

[[find in source code]](blob/master/dulwich/refs.py#L267)

```python
def read_loose_ref(name):
```

Read a loose reference and return its contents.

#### Arguments

  - `name` - the refname to read
- `Returns` - The contents of the ref file, or None if it does
    not exist.

### RefsContainer().read_ref

[[find in source code]](blob/master/dulwich/refs.py#L254)

```python
def read_ref(refname):
```

Read a reference without following any references.

#### Arguments

  - `refname` - The name of the reference
- `Returns` - The contents of the ref file, or None if it does
    not exist.

### RefsContainer().remove_if_equals

[[find in source code]](blob/master/dulwich/refs.py#L376)

```python
def remove_if_equals(
    name,
    old_ref,
    committer=None,
    timestamp=None,
    timezone=None,
    message=None,
):
```

Remove a refname only if it currently equals old_ref.

This method does not follow symbolic references, even if applicable for
the subclass. It can be used to perform an atomic compare-and-delete
operation.

#### Arguments

  - `name` - The refname to delete.
  - `old_ref` - The old sha the refname must refer to, or None to
    delete unconditionally.
  - `message` - Message for reflog
- `Returns` - True if the delete was successful, False otherwise.

### RefsContainer().set_if_equals

[[find in source code]](blob/master/dulwich/refs.py#L324)

```python
def set_if_equals(
    name,
    old_ref,
    new_ref,
    committer=None,
    timestamp=None,
    timezone=None,
    message=None,
):
```

Set a refname to new_ref only if it currently equals old_ref.

This method follows all symbolic references if applicable for the
subclass, and can be used to perform an atomic compare-and-swap
operation.

#### Arguments

  - `name` - The refname to set.
  - `old_ref` - The old sha the refname must refer to, or None to set
    unconditionally.
  - `new_ref` - The new sha the refname will refer to.
  - `message` - Message for reflog
- `Returns` - True if the set was successful, False otherwise.

### RefsContainer().set_symbolic_ref

[[find in source code]](blob/master/dulwich/refs.py#L117)

```python
def set_symbolic_ref(
    name,
    other,
    committer=None,
    timestamp=None,
    timezone=None,
    message=None,
):
```

Make a ref point at another ref.

#### Arguments

- `name` - Name of the ref to set
- `other` - Name of the ref to point at
- `message` - Optional message

### RefsContainer().subkeys

[[find in source code]](blob/master/dulwich/refs.py#L205)

```python
def subkeys(base):
```

Refs present in this container under a base.

#### Arguments

  - `base` - The base to return refs under.
- `Returns` - A set of valid refs in this container under the base; the base
    prefix is stripped from the ref names returned.

### RefsContainer().watch

[[find in source code]](blob/master/dulwich/refs.py#L430)

```python
def watch():
```

Watch for changes to the refs in this container.

Returns a context manager that yields tuples with (refname, new_sha)

## check_ref_format

[[find in source code]](blob/master/dulwich/refs.py#L61)

```python
def check_ref_format(refname):
```

Check if a refname is correctly formatted.

Implements all the same rules as git-check-ref-format[1].

[1]
http://www.kernel.org/pub/software/scm/git/docs/git-check-ref-format.html

#### Arguments

  - `refname` - The refname to check
- `Returns` - True if refname is valid, False otherwise

## is_local_branch

[[find in source code]](blob/master/dulwich/refs.py#L1195)

```python
def is_local_branch(x):
```

## parse_symref_value

[[find in source code]](blob/master/dulwich/refs.py#L49)

```python
def parse_symref_value(contents):
```

Parse a symref value.

#### Arguments

  - `contents` - Contents to parse
- `Returns` - Destination

## read_info_refs

[[find in source code]](blob/master/dulwich/refs.py#L1170)

```python
def read_info_refs(f):
```

## read_packed_refs

[[find in source code]](blob/master/dulwich/refs.py#L1104)

```python
def read_packed_refs(f):
```

Read a packed refs file.

#### Arguments

  - `f` - file-like object to read from
- `Returns` - Iterator over tuples with SHA1s and ref names.

## read_packed_refs_with_peeled

[[find in source code]](blob/master/dulwich/refs.py#L1120)

```python
def read_packed_refs_with_peeled(f):
```

Read a packed refs file including peeled refs.

Assumes the "# pack-refs with: peeled" line was already read. Yields tuples
with ref names, SHA1s, and peeled SHA1s (or None).

#### Arguments

- `f` - file-like object to read from, seek'ed to the second line

## strip_peeled_refs

[[find in source code]](blob/master/dulwich/refs.py#L1199)

```python
def strip_peeled_refs(refs):
```

Remove all peeled refs

## write_info_refs

[[find in source code]](blob/master/dulwich/refs.py#L1178)

```python
def write_info_refs(refs, store):
```

Generate info refs.

## write_packed_refs

[[find in source code]](blob/master/dulwich/refs.py#L1152)

```python
def write_packed_refs(f, packed_refs, peeled_refs=None):
```

Write a packed refs file.

#### Arguments

- `f` - empty file-like object to write to
- `packed_refs` - dict of refname to sha of packed refs to write
- `peeled_refs` - dict of refname to peeled value of sha
