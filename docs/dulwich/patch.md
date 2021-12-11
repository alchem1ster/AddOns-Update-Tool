# Patch

> Auto-generated documentation for [dulwich.patch](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/patch.py) module.

Classes for dealing with git am-style patches.

- [Addons-update-tool](../README.md#addons-update-tool) / [Modules](../MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / Patch
    - [gen_diff_header](#gen_diff_header)
    - [get_summary](#get_summary)
    - [git_am_patch_split](#git_am_patch_split)
    - [is_binary](#is_binary)
    - [parse_patch_message](#parse_patch_message)
    - [patch_filename](#patch_filename)
    - [shortid](#shortid)
    - [unified_diff](#unified_diff)
    - [write_blob_diff](#write_blob_diff)
    - [write_commit_patch](#write_commit_patch)
    - [write_object_diff](#write_object_diff)
    - [write_tree_diff](#write_tree_diff)

These patches are basically unified diffs with some extra metadata tacked
on.

## gen_diff_header

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/patch.py#L252)

```python
def gen_diff_header(paths, modes, shas):
```

Write a blob diff header.

#### Arguments

- `paths` - Tuple with old and new path
- `modes` - Tuple with old and new modes
- `shas` - Tuple with old and new shas

## get_summary

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/patch.py#L93)

```python
def get_summary(commit):
```

Determine the summary line for use in a filename.

#### Arguments

  - `commit` - Commit
- `Returns` - Summary string

## git_am_patch_split

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/patch.py#L341)

```python
def git_am_patch_split(f, encoding=None):
```

Parse a git-am-style patch and split it up into bits.

#### Arguments

  - `f` - File-like object to parse
  - `encoding` - Encoding to use when creating Git objects
- `Returns` - Tuple with commit object, diff contents and git version

## is_binary

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/patch.py#L171)

```python
def is_binary(content):
```

See if the first few bytes contain any null characters.

#### Arguments

- `content` - Bytestring to check for binary content

## parse_patch_message

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/patch.py#L361)

```python
def parse_patch_message(msg, encoding=None):
```

Extract a Commit object and patch from an e-mail message.

#### Arguments

  - `msg` - An email message (email.message.Message)
  - `encoding` - Encoding to use to encode Git commits
- `Returns` - Tuple with commit object, diff contents and git version

## patch_filename

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/patch.py#L187)

```python
def patch_filename(p, root):
```

## shortid

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/patch.py#L180)

```python
def shortid(hexsha):
```

## unified_diff

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/patch.py#L117)

```python
def unified_diff(
    a,
    b,
    fromfile='',
    tofile='',
    fromfiledate='',
    tofiledate='',
    n=3,
    lineterm='\n',
    tree_encoding='utf-8',
    output_encoding='utf-8',
):
```

difflib.unified_diff that can detect "No newline at end of file" as
original "git diff" does.

Based on the same function in Python2.7 difflib.py

## write_blob_diff

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/patch.py#L285)

```python
def write_blob_diff(f, old_file, new_file):
```

Write blob diff.

#### Arguments

- `f` - File-like object to write to
- `old_file` - (path, mode, hexsha) tuple (None if nonexisting)
- `new_file` - (path, mode, hexsha) tuple (None if nonexisting)

- `Note` - The use of write_object_diff is recommended over this function.

## write_commit_patch

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/patch.py#L40)

```python
def write_commit_patch(
    f,
    commit,
    contents,
    progress,
    version=None,
    encoding=None,
):
```

Write a individual file patch.

#### Arguments

- `commit` - Commit object
- `progress` - Tuple with current patch number and total.

#### Returns

tuple with filename and contents

## write_object_diff

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/patch.py#L194)

```python
def write_object_diff(f, store, old_file, new_file, diff_binary=False):
```

Write the diff for an object.

#### Arguments

- `f` - File-like object to write to
- `store` - Store to retrieve objects from, if necessary
- `old_file` - (path, mode, hexsha) tuple
- `new_file` - (path, mode, hexsha) tuple
- `diff_binary` - Whether to diff files even if they
  are considered binary files by is_binary().

- `Note` - the tuple elements should be None for nonexistant files

## write_tree_diff

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/patch.py#L320)

```python
def write_tree_diff(f, store, old_tree, new_tree, diff_binary=False):
```

Write tree diff.

#### Arguments

- `f` - File-like object to write to.
- `old_tree` - Old tree id
- `new_tree` - New tree id
- `diff_binary` - Whether to diff files even if they
  are considered binary files by is_binary().
