# Ignore

> Auto-generated documentation for [dulwich.ignore](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/ignore.py) module.

Parsing of gitignore files.

- [AddOns-Update-Tool](../README.md#addons-update-tool-index) / [Modules](../MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / Ignore
    - [IgnoreFilter](#ignorefilter)
        - [IgnoreFilter().append_pattern](#ignorefilterappend_pattern)
        - [IgnoreFilter().find_matching](#ignorefilterfind_matching)
        - [IgnoreFilter.from_path](#ignorefilterfrom_path)
        - [IgnoreFilter().is_ignored](#ignorefilteris_ignored)
    - [IgnoreFilterManager](#ignorefiltermanager)
        - [IgnoreFilterManager().find_matching](#ignorefiltermanagerfind_matching)
        - [IgnoreFilterManager.from_repo](#ignorefiltermanagerfrom_repo)
        - [IgnoreFilterManager().is_ignored](#ignorefiltermanageris_ignored)
    - [IgnoreFilterStack](#ignorefilterstack)
        - [IgnoreFilterStack().is_ignored](#ignorefilterstackis_ignored)
    - [Pattern](#pattern)
        - [Pattern().match](#patternmatch)
    - [default_user_ignore_filter_path](#default_user_ignore_filter_path)
    - [match_pattern](#match_pattern)
    - [read_ignore_patterns](#read_ignore_patterns)
    - [translate](#translate)

For details for the matching rules, see https://git-scm.com/docs/gitignore

## IgnoreFilter

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/ignore.py#L206)

```python
class IgnoreFilter(object):
    def __init__(
        patterns: Iterable[bytes],
        ignorecase: bool = False,
        path=None,
    ):
```

### IgnoreFilter().append_pattern

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/ignore.py#L216)

```python
def append_pattern(pattern: bytes) -> None:
```

Add a pattern to the set.

### IgnoreFilter().find_matching

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/ignore.py#L220)

```python
def find_matching(path: Union[bytes, str]) -> Iterable[Pattern]:
```

Yield all matching patterns for path.

#### Arguments

- `path` - Path to match

#### Returns

Iterator over iterators

### IgnoreFilter.from_path

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/ignore.py#L247)

```python
@classmethod
def from_path(path, ignorecase: bool = False) -> 'IgnoreFilter':
```

### IgnoreFilter().is_ignored

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/ignore.py#L234)

```python
def is_ignored(path: bytes) -> Optional[bool]:
```

Check whether a path is ignored.

For directories, include a trailing slash.

Returns: status is None if file is not mentioned, True if it is
    included, False if it is explicitly excluded.

## IgnoreFilterManager

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/ignore.py#L299)

```python
class IgnoreFilterManager(object):
    def __init__(
        top_path: str,
        global_filters: List[IgnoreFilter],
        ignorecase: bool,
    ):
```

Ignore file manager.

### IgnoreFilterManager().find_matching

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/ignore.py#L336)

```python
def find_matching(path: str) -> Iterable[Pattern]:
```

Find matching patterns for path.

#### Arguments

- `path` - Path to check

#### Returns

Iterator over Pattern instances

### IgnoreFilterManager.from_repo

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/ignore.py#L379)

```python
@classmethod
def from_repo(repo: 'Repo') -> 'IgnoreFilterManager':
```

Create a IgnoreFilterManager from a repository.

#### Arguments

- `repo` - Repository object

#### Returns

A [IgnoreFilterManager](#ignorefiltermanager) object

### IgnoreFilterManager().is_ignored

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/ignore.py#L365)

```python
def is_ignored(path: str) -> Optional[bool]:
```

Check whether a path is explicitly included or excluded in ignores.

#### Arguments

- `path` - Path to check

#### Returns

None if the file is not mentioned, True if it is included,
False if it is explicitly excluded.

## IgnoreFilterStack

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/ignore.py#L260)

```python
class IgnoreFilterStack(object):
    def __init__(filters):
```

Check for ignore status in multiple filters.

### IgnoreFilterStack().is_ignored

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/ignore.py#L266)

```python
def is_ignored(path: str) -> Optional[bool]:
```

Check whether a path is explicitly included or excluded in ignores.

#### Arguments

- `path` - Path to check

#### Returns

None if the file is not mentioned, True if it is included,
False if it is explicitly excluded.

## Pattern

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/ignore.py#L158)

```python
class Pattern(object):
    def __init__(pattern: bytes, ignorecase: bool = False):
```

A single ignore pattern.

### Pattern().match

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/ignore.py#L196)

```python
def match(path: bytes) -> bool:
```

Try to match a path against this ignore pattern.

#### Arguments

  - `path` - Path to match (relative to ignore location)
- `Returns` - boolean

## default_user_ignore_filter_path

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/ignore.py#L283)

```python
def default_user_ignore_filter_path(config: Config) -> str:
```

Return default user ignore filter path.

#### Arguments

- `config` - A Config object

#### Returns

Path to a global ignore file

#### See also

- [Config](config.md#config)

## match_pattern

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/ignore.py#L143)

```python
def match_pattern(
    path: bytes,
    pattern: bytes,
    ignorecase: bool = False,
) -> bool:
```

Match a gitignore-style pattern against a path.

#### Arguments

- `path` - Path to match
- `pattern` - Pattern to match
- `ignorecase` - Whether to do case-sensitive matching

#### Returns

bool indicating whether the pattern matched

## read_ignore_patterns

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/ignore.py#L116)

```python
def read_ignore_patterns(f: BinaryIO) -> Iterable[bytes]:
```

Read a git ignore file.

#### Arguments

  - `f` - File-like object to read from
- `Returns` - List of patterns

## translate

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/ignore.py#L78)

```python
def translate(pat: bytes) -> bytes:
```

Translate a shell PATTERN to a regular expression.

There is no way to quote meta-characters.

Originally copied from fnmatch in Python 2.7, but modified for Dulwich
to cope with features in Git ignore patterns.
