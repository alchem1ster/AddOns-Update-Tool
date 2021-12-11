# Clone

> Auto-generated documentation for [dulwich.clone](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/clone.py) module.

Repository clone handling.

- [Addons-update-tool](../README.md#addons-update-tool) / [Modules](../MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / Clone
    - [do_clone](#do_clone)

## do_clone

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/clone.py#L38)

```python
def do_clone(
    source_path,
    target_path,
    clone_refs: Callable[['Repo', bytes], Tuple[bytes, bytes]] = None,
    mkdir=True,
    bare=False,
    origin=b'origin',
    checkout=None,
    errstream=None,
    branch=None,
):
```

Clone a repository.

#### Arguments

  - `source_path` - Source repository path
  - `target_path` - Target repository path
  - `clone_refs` - Callback to handle setting up cloned remote refs in
    the target repo
  - `mkdir` - Create the target directory
  - `bare` - Whether to create a bare repository
  - `checkout` - Whether or not to check-out HEAD after cloning
  - `origin` - Base name for refs in target repository
    cloned from this repository
  - `branch` - Optional branch or tag to be used as HEAD in the new repository
    instead of the source repository's HEAD.
- `Returns` - Created repository as `Repo`
