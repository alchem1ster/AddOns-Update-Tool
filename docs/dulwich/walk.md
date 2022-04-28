# Walk

> Auto-generated documentation for [dulwich.walk](../../dulwich/walk.py) module.

General implementation of walking commits and their contents.

- [AddOns-Update-Tool](../README.md#addons-update-tool-index) / [Modules](../MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / Walk
    - [WalkEntry](#walkentry)
        - [WalkEntry().changes](#walkentrychanges)
    - [Walker](#walker)

## WalkEntry

[[find in source code]](../../dulwich/walk.py#L50)

```python
class WalkEntry(object):
    def __init__(walker, commit):
```

Object encapsulating a single result from a walk.

### WalkEntry().changes

[[find in source code]](../../dulwich/walk.py#L60)

```python
def changes(path_prefix=None):
```

Get the tree changes for this entry.

#### Arguments

  - `path_prefix` - Portion of the path in the repository to
    use to filter changes. Must be a directory name. Must be
    a full, valid, path reference (no partial names or wildcards).
- `Returns` - For commits with up to one parent, a list of TreeChange
    objects; if the commit has no parents, these will be relative to
    the empty tree. For merge commits, a list of lists of TreeChange
    objects; see dulwich.diff.tree_changes_for_merge.

## Walker

[[find in source code]](../../dulwich/walk.py#L239)

```python
class Walker(object):
    def __init__(
        store,
        include,
        exclude=None,
        order=ORDER_DATE,
        reverse=False,
        max_entries=None,
        paths=None,
        rename_detector=None,
        follow=False,
        since=None,
        until=None,
        get_parents=lambda commit: commit.parents,
        queue_cls=_CommitTimeQueue,
    ):
```

Object for performing a walk of commits in a store.

Walker objects are initialized with a store and other options and can then
be treated as iterators of Commit objects.

#### See also

- [ORDER_DATE](#order_date)
