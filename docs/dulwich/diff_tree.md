# Diff Tree

> Auto-generated documentation for [dulwich.diff_tree](blob/master/dulwich/diff_tree.py) module.

Utilities for diffing files and trees.

- [Addons-update-tool](..\README.md#addons-update-tool) / [Modules](..\MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / Diff Tree
    - [RenameDetector](#renamedetector)
        - [RenameDetector().changes_with_renames](#renamedetectorchanges_with_renames)
    - [TreeChange](#treechange)
        - [TreeChange.add](#treechangeadd)
        - [TreeChange.delete](#treechangedelete)
    - [tree_changes](#tree_changes)
    - [tree_changes_for_merge](#tree_changes_for_merge)
    - [walk_trees](#walk_trees)

#### Attributes

- `CHANGE_ADD` - TreeChange type constants.: `'add'`

## RenameDetector

[[find in source code]](blob/master/dulwich/diff_tree.py#L403)

```python
class RenameDetector(object):
    def __init__(
        store,
        rename_threshold=RENAME_THRESHOLD,
        max_files=MAX_FILES,
        rewrite_threshold=REWRITE_THRESHOLD,
        find_copies_harder=False,
    ):
```

Object for handling rename detection between two trees.

#### See also

- [MAX_FILES](#max_files)
- [RENAME_THRESHOLD](#rename_threshold)
- [REWRITE_THRESHOLD](#rewrite_threshold)

### RenameDetector().changes_with_renames

[[find in source code]](blob/master/dulwich/diff_tree.py#L620)

```python
def changes_with_renames(
    tree1_id,
    tree2_id,
    want_unchanged=False,
    include_trees=False,
):
```

Iterate TreeChanges between two tree SHAs, with rename detection.

## TreeChange

[[find in source code]](blob/master/dulwich/diff_tree.py#L56)

```python
class TreeChange(namedtuple('TreeChange', ['type', 'old', 'new'])):
```

Named tuple a single change between two trees.

### TreeChange.add

[[find in source code]](blob/master/dulwich/diff_tree.py#L59)

```python
@classmethod
def add(new):
```

### TreeChange.delete

[[find in source code]](blob/master/dulwich/diff_tree.py#L63)

```python
@classmethod
def delete(old):
```

## tree_changes

[[find in source code]](blob/master/dulwich/diff_tree.py#L166)

```python
def tree_changes(
    store,
    tree1_id,
    tree2_id,
    want_unchanged=False,
    rename_detector=None,
    include_trees=False,
    change_type_same=False,
):
```

Find the differences between the contents of two trees.

#### Arguments

- `store` - An ObjectStore for looking up objects.
- `tree1_id` - The SHA of the source tree.
- `tree2_id` - The SHA of the target tree.
- `want_unchanged` - If True, include TreeChanges for unmodified entries
  as well.
- `include_trees` - Whether to include trees
- `rename_detector` - RenameDetector object for detecting renames.
- `change_type_same` - Whether to report change types in the same
  entry or as delete+add.

#### Returns

Iterator over TreeChange instances for each change between the
  source and target tree.

## tree_changes_for_merge

[[find in source code]](blob/master/dulwich/diff_tree.py#L246)

```python
def tree_changes_for_merge(
    store,
    parent_tree_ids,
    tree_id,
    rename_detector=None,
):
```

Get the tree changes for a merge tree relative to all its parents.

#### Arguments

- `store` - An ObjectStore for looking up objects.
- `parent_tree_ids` - An iterable of the SHAs of the parent trees.
- `tree_id` - The SHA of the merge tree.
- `rename_detector` - RenameDetector object for detecting renames.

#### Returns

Iterator over lists of TreeChange objects, one per conflicted path
in the merge.

Each list contains one element per parent, with the TreeChange for that
path relative to that parent. An element may be None if it never
existed in one parent and was deleted in two others.

A path is only included in the output if it is a conflict, i.e. its SHA
in the merge tree is not found in any of the parents, or in the case of
deletes, if not all of the old SHAs match.

## walk_trees

[[find in source code]](blob/master/dulwich/diff_tree.py#L124)

```python
def walk_trees(store, tree1_id, tree2_id, prune_identical=False):
```

Recursively walk all the entries of two trees.

Iteration is depth-first pre-order, as in e.g. os.walk.

#### Arguments

- `store` - An ObjectStore for looking up objects.
- `tree1_id` - The SHA of the first Tree object to iterate, or None.
- `tree2_id` - The SHA of the second Tree object to iterate, or None.
- `param` *prune_identical* - If True, identical subtrees will not be walked.

#### Returns

Iterator over Pairs of TreeEntry objects for each pair of entries
  in the trees and their subtrees recursively. If an entry exists in one
  tree but not the other, the other entry will have all attributes set
  to None. If neither entry's path is None, they are guaranteed to
  match.
