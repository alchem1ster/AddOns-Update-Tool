# Objectspec

> Auto-generated documentation for [dulwich.objectspec](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/objectspec.py) module.

Object specification.

- [AddOns-Update-Tool](../README.md#addons-update-tool-index) / [Modules](../MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / Objectspec
    - [AmbiguousShortId](#ambiguousshortid)
    - [parse_commit](#parse_commit)
    - [parse_commit_range](#parse_commit_range)
    - [parse_object](#parse_object)
    - [parse_ref](#parse_ref)
    - [parse_refs](#parse_refs)
    - [parse_reftuple](#parse_reftuple)
    - [parse_reftuples](#parse_reftuples)
    - [parse_tree](#parse_tree)
    - [scan_for_short_id](#scan_for_short_id)
    - [to_bytes](#to_bytes)

## AmbiguousShortId

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/objectspec.py#L190)

```python
class AmbiguousShortId(Exception):
    def __init__(prefix, options):
```

The short id is ambiguous.

## parse_commit

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/objectspec.py#L213)

```python
def parse_commit(repo, committish):
```

Parse a string referring to a single commit.

#### Arguments

  - `repo` - A` Repo` object
  - `commitish` - A string referring to a single commit.
- `Returns` - A Commit object

#### Raises

- `KeyError` - When the reference commits can not be found
- `ValueError` - If the range can not be parsed

## parse_commit_range

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/objectspec.py#L174)

```python
def parse_commit_range(repo, committishs):
```

Parse a string referring to a range of commits.

#### Arguments

  - `repo` - A `Repo` object
  - `committishs` - A string referring to a range of commits.
- `Returns` - An iterator over `Commit` objects

#### Raises

- `KeyError` - When the reference commits can not be found
- `ValueError` - If the range can not be parsed

## parse_object

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/objectspec.py#L32)

```python
def parse_object(repo, objectish):
```

Parse a string referring to an object.

#### Arguments

  - `repo` - A `Repo` object
  - `objectish` - A string referring to an object
- `Returns` - A git object

#### Raises

- `KeyError` - If the object can not be found

## parse_ref

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/objectspec.py#L67)

```python
def parse_ref(container, refspec):
```

Parse a string referring to a reference.

#### Arguments

  - `container` - A RefsContainer object
  - `refspec` - A string referring to a ref
- `Returns` - A ref

#### Raises

- `KeyError` - If the ref can not be found

## parse_refs

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/objectspec.py#L155)

```python
def parse_refs(container, refspecs):
```

Parse a list of refspecs to a list of refs.

#### Arguments

  - `container` - A RefsContainer object
  - `refspecs` - A list of refspecs or a string
- `Returns` - A list of refs

#### Raises

- `KeyError` - If one of the refs can not be found

## parse_reftuple

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/objectspec.py#L92)

```python
def parse_reftuple(lh_container, rh_container, refspec, force=False):
```

Parse a reftuple spec.

#### Arguments

  - `lh_container` - A RefsContainer object
  - `hh_container` - A RefsContainer object
  - `refspec` - A string
- `Returns` - A tuple with left and right ref

#### Raises

- `KeyError` - If one of the refs can not be found

## parse_reftuples

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/objectspec.py#L127)

```python
def parse_reftuples(
    lh_container,
    rh_container,
    refspecs: Union[bytes, List[bytes], List[Tuple[bytes, bytes]]],
    force: bool = False,
):
```

Parse a list of reftuple specs to a list of reftuples.

#### Arguments

  - `lh_container` - A RefsContainer object
  - `hh_container` - A RefsContainer object
  - `refspecs` - A list of refspecs or a string
  - `force` - Force overwriting for all reftuples
- `Returns` - A list of refs

#### Raises

- `KeyError` - If one of the refs can not be found

## parse_tree

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/objectspec.py#L46)

```python
def parse_tree(repo, treeish):
```

Parse a string referring to a tree.

#### Arguments

  - `repo` - A `Repo` object
  - `treeish` - A string referring to a tree
- `Returns` - A git object

#### Raises

- `KeyError` - If the object can not be found

## scan_for_short_id

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/objectspec.py#L198)

```python
def scan_for_short_id(object_store, prefix):
```

Scan an object store for a short id.

## to_bytes

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/objectspec.py#L26)

```python
def to_bytes(text):
```
