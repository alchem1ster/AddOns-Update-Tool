# Stash

> Auto-generated documentation for [dulwich.stash](../../dulwich/stash.py) module.

Stash handling.

- [AddOns-Update-Tool](../README.md#addons-update-tool-index) / [Modules](../MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / Stash
    - [Stash](#stash)
        - [Stash().drop](#stashdrop)
        - [Stash.from_repo](#stashfrom_repo)
        - [Stash().pop](#stashpop)
        - [Stash().push](#stashpush)
        - [Stash().stashes](#stashstashes)

## Stash

[[find in source code]](../../dulwich/stash.py#L38)

```python
class Stash(object):
    def __init__(repo, ref=DEFAULT_STASH_REF):
```

A Git stash.

Note that this doesn't currently update the working tree.

#### See also

- [DEFAULT_STASH_REF](#default_stash_ref)

### Stash().drop

[[find in source code]](../../dulwich/stash.py#L66)

```python
def drop(index):
```

Drop entry with specified index.

### Stash.from_repo

[[find in source code]](../../dulwich/stash.py#L61)

```python
@classmethod
def from_repo(repo):
```

Create a new stash from a Repo object.

### Stash().pop

[[find in source code]](../../dulwich/stash.py#L77)

```python
def pop(index):
```

### Stash().push

[[find in source code]](../../dulwich/stash.py#L80)

```python
def push(committer=None, author=None, message=None):
```

Create a new stash.

#### Arguments

- `committer` - Optional committer name to use
- `author` - Optional author name to use
- `message` - Optional commit message

### Stash().stashes

[[find in source code]](../../dulwich/stash.py#L54)

```python
def stashes():
```
