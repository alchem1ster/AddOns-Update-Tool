# LRUCache

> Auto-generated documentation for [dulwich.lru_cache](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/lru_cache.py) module.

A simple least-recently-used (LRU) cache.

- [Addons-update-tool](../README.md#addons-update-tool) / [Modules](../MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / LRUCache
    - [LRUCache](#lrucache)
        - [LRUCache().\_\_setitem\_\_](#lrucache__setitem__)
        - [LRUCache().add](#lrucacheadd)
        - [LRUCache().cache_size](#lrucachecache_size)
        - [LRUCache().cleanup](#lrucachecleanup)
        - [LRUCache().clear](#lrucacheclear)
        - [LRUCache().get](#lrucacheget)
        - [LRUCache().items](#lrucacheitems)
        - [LRUCache().keys](#lrucachekeys)
        - [LRUCache().resize](#lrucacheresize)
    - [LRUSizeCache](#lrusizecache)
        - [LRUSizeCache().add](#lrusizecacheadd)
        - [LRUSizeCache().cleanup](#lrusizecachecleanup)
        - [LRUSizeCache().resize](#lrusizecacheresize)

## LRUCache

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/lru_cache.py#L62)

```python
class LRUCache(object):
    def __init__(max_cache=100, after_cleanup_count=None):
```

A class which manages a cache of entries, removing unused ones.

### LRUCache().\_\_setitem\_\_

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/lru_cache.py#L211)

```python
def __setitem__(key, value):
```

Add a value to the cache, there will be no cleanup function.

### LRUCache().add

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/lru_cache.py#L147)

```python
def add(key, value, cleanup=None):
```

Add a new value to the cache.

Also, if the entry is ever removed from the cache, call
cleanup(key, value).

#### Arguments

- `key` - The key to store it under
- `value` - The object to store
- `cleanup` - None or a function taking (key, value) to indicate
              'value' should be cleaned up.

### LRUCache().cache_size

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/lru_cache.py#L175)

```python
def cache_size():
```

Get the number of entries we will cache.

### LRUCache().cleanup

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/lru_cache.py#L201)

```python
def cleanup():
```

Clear the cache until it shrinks to the requested size.

This does not completely wipe the cache, just makes sure it is under
the after_cleanup_count.

### LRUCache().clear

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/lru_cache.py#L267)

```python
def clear():
```

Clear out all of the cache.

### LRUCache().get

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/lru_cache.py#L179)

```python
def get(key, default=None):
```

### LRUCache().items

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/lru_cache.py#L197)

```python
def items():
```

Get the key:value pairs as a dict.

### LRUCache().keys

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/lru_cache.py#L186)

```python
def keys():
```

Get the list of keys currently cached.

Note that values returned here may not be available by the time you
request them later. This is simply meant as a peak into the current
state.

Returns: An unordered list of keys that are currently cached.

### LRUCache().resize

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/lru_cache.py#L273)

```python
def resize(max_cache, after_cleanup_count=None):
```

Change the number of entries that will be cached.

## LRUSizeCache

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/lru_cache.py#L286)

```python
class LRUSizeCache(LRUCache):
    def __init__(
        max_size=1024 * 1024,
        after_cleanup_size=None,
        compute_size=None,
    ):
```

An LRUCache that removes things based on the size of the values.

This differs in that it doesn't care how many actual items there are,
it just restricts the cache to be cleaned up after so much data is stored.

The size of items added will be computed using compute_size(value), which
defaults to len() if not supplied.

#### See also

- [LRUCache](#lrucache)

### LRUSizeCache().add

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/lru_cache.py#L320)

```python
def add(key, value, cleanup=None):
```

Add a new value to the cache.

Also, if the entry is ever removed from the cache, call
cleanup(key, value).

#### Arguments

- `key` - The key to store it under
- `value` - The object to store
- `cleanup` - None or a function taking (key, value) to indicate
              'value' should be cleaned up.

### LRUSizeCache().cleanup

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/lru_cache.py#L358)

```python
def cleanup():
```

Clear the cache until it shrinks to the requested size.

This does not completely wipe the cache, just makes sure it is under
the after_cleanup_size.

### LRUSizeCache().resize

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/lru_cache.py#L372)

```python
def resize(max_size, after_cleanup_size=None):
```

Change the number of bytes that will be cached.
