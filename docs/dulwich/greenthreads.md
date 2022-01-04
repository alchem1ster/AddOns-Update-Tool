# Greenthreads

> Auto-generated documentation for [dulwich.greenthreads](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/greenthreads.py) module.

Utility module for querying an ObjectStore with gevent.

- [AddOns-Update-Tool](../README.md#addons-update-tool-index) / [Modules](../MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / Greenthreads
    - [GreenThreadsMissingObjectFinder](#greenthreadsmissingobjectfinder)
    - [GreenThreadsObjectStoreIterator](#greenthreadsobjectstoreiterator)
        - [GreenThreadsObjectStoreIterator().retrieve](#greenthreadsobjectstoreiteratorretrieve)

## GreenThreadsMissingObjectFinder

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/greenthreads.py#L68)

```python
class GreenThreadsMissingObjectFinder(MissingObjectFinder):
    def __init__(
        object_store,
        haves,
        wants,
        progress=None,
        get_tagged=None,
        concurrency=1,
        get_parents=None,
    ):
```

Find the objects missing from another object store.

Same implementation as object_store.MissingObjectFinder
except we use gevent to parallelize object retrieval.

#### See also

- [MissingObjectFinder](object_store.md#missingobjectfinder)

## GreenThreadsObjectStoreIterator

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/greenthreads.py#L119)

```python
class GreenThreadsObjectStoreIterator(ObjectStoreIterator):
    def __init__(store, shas, finder, concurrency=1):
```

ObjectIterator that works on top of an ObjectStore.

Same implementation as object_store.ObjectStoreIterator
except we use gevent to parallelize object retrieval.

#### See also

- [ObjectStoreIterator](object_store.md#objectstoreiterator)

### GreenThreadsObjectStoreIterator().retrieve

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/greenthreads.py#L131)

```python
def retrieve(args):
```
