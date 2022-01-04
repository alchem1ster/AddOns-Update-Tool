# Graph

> Auto-generated documentation for [dulwich.graph](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/graph.py) module.

Implementation of merge-base following the approach of git

- [AddOns-Update-Tool](../README.md#addons-update-tool-index) / [Modules](../MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / Graph
    - [can_fast_forward](#can_fast_forward)
    - [find_merge_base](#find_merge_base)
    - [find_octopus_base](#find_octopus_base)

## can_fast_forward

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/graph.py#L132)

```python
def can_fast_forward(repo, c1, c2):
```

Is it possible to fast-forward from c1 to c2?

#### Arguments

- `repo` - Repository to retrieve objects from
- `c1` - Commit id for first commit
- `c2` - Commit id for second commit

## find_merge_base

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/graph.py#L85)

```python
def find_merge_base(repo, commit_ids):
```

Find lowest common ancestors of commit_ids[0] and *any* of commits_ids[1:]

#### Arguments

- `repo` - Repository object
- `commit_ids` - list of commit ids

#### Returns

list of lowest common ancestor commit_ids

## find_octopus_base

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/graph.py#L106)

```python
def find_octopus_base(repo, commit_ids):
```

Find lowest common ancestors of *all* provided commit_ids

#### Arguments

- `repo` - Repository
- `commit_ids` - list of commit ids

#### Returns

list of lowest common ancestor commit_ids
