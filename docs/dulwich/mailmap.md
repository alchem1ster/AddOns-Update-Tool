# Mailmap

> Auto-generated documentation for [dulwich.mailmap](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/mailmap.py) module.

Mailmap file reader.

- [AddOns-Update-Tool](../README.md#addons-update-tool-index) / [Modules](../MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / Mailmap
    - [Mailmap](#mailmap)
        - [Mailmap().add_entry](#mailmapadd_entry)
        - [Mailmap.from_path](#mailmapfrom_path)
        - [Mailmap().lookup](#mailmaplookup)
    - [parse_identity](#parse_identity)
    - [read_mailmap](#read_mailmap)

## Mailmap

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/mailmap.py#L61)

```python
class Mailmap(object):
    def __init__(map=None):
```

Class for accessing a mailmap file.

### Mailmap().add_entry

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/mailmap.py#L70)

```python
def add_entry(canonical_identity, from_identity=None):
```

Add an entry to the mail mail.

Any of the fields can be None, but at least one of them needs to be
set.

#### Arguments

- `canonical_identity` - The canonical identity (tuple)
- `from_identity` - The from identity (tuple)

### Mailmap.from_path

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/mailmap.py#L111)

```python
@classmethod
def from_path(path):
```

### Mailmap().lookup

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/mailmap.py#L91)

```python
def lookup(identity):
```

Lookup an identity in this mailmail.

## parse_identity

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/mailmap.py#L24)

```python
def parse_identity(text):
```

## read_mailmap

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/mailmap.py#L37)

```python
def read_mailmap(f):
```

Read a mailmap.

#### Arguments

  - `f` - File-like object to read from
- `Returns` - Iterator over
    ((canonical_name, canonical_email), (from_name, from_email)) tuples
