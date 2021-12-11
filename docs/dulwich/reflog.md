# Reflog

> Auto-generated documentation for [dulwich.reflog](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/reflog.py) module.

Utilities for reading and generating reflogs.

- [Addons-update-tool](../README.md#addons-update-tool) / [Modules](../MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / Reflog
    - [drop_reflog_entry](#drop_reflog_entry)
    - [format_reflog_line](#format_reflog_line)
    - [parse_reflog_line](#parse_reflog_line)
    - [read_reflog](#read_reflog)

## drop_reflog_entry

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/reflog.py#L98)

```python
def drop_reflog_entry(f, index, rewrite=False):
```

Drop the specified reflog entry.

#### Arguments

- `f` - File-like object
- `index` - Reflog entry index (in Git reflog reverse 0-indexed order)
- `rewrite` - If a reflog entry's predecessor is removed, set its
    old SHA to the new SHA of the entry that now precedes it

## format_reflog_line

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/reflog.py#L38)

```python
def format_reflog_line(
    old_sha,
    new_sha,
    committer,
    timestamp,
    timezone,
    message,
):
```

Generate a single reflog line.

#### Arguments

- `old_sha` - Old Commit SHA
- `new_sha` - New Commit SHA
- `committer` - Committer name and e-mail
- `timestamp` - Timestamp
- `timezone` - Timezone
- `message` - Message

## parse_reflog_line

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/reflog.py#L66)

```python
def parse_reflog_line(line):
```

Parse a reflog line.

#### Arguments

  - `line` - Line to parse
- `Returns` - Tuple of (old_sha, new_sha, committer, timestamp, timezone,
    message)

## read_reflog

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/master/dulwich/reflog.py#L87)

```python
def read_reflog(f):
```

Read reflog.

#### Arguments

  - `f` - File-like object
- `Returns` - Iterator over Entry objects
