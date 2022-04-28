# Log Utils

> Auto-generated documentation for [dulwich.log_utils](../../dulwich/log_utils.py) module.

Logging utilities for Dulwich.

- [AddOns-Update-Tool](../README.md#addons-update-tool-index) / [Modules](../MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / Log Utils
    - [default_logging_config](#default_logging_config)
    - [remove_null_handler](#remove_null_handler)

Any module that uses logging needs to do compile-time initialization to set up
the logging environment. Since Dulwich is also used as a library, clients may
not want to see any logging output. In that case, we need to use a special
handler to suppress spurious warnings like "No handlers could be found for
logger dulwich.foo".

For details on the _NullHandler approach, see:
http://docs.python.org/library/logging.html#configuring-logging-for-a-library

For many modules, the only function from the logging module they need is
getLogger; this module exports that function for convenience. If a calling
module needs something else, it can import the standard logging module
directly.

## default_logging_config

[[find in source code]](../../dulwich/log_utils.py#L56)

```python
def default_logging_config():
```

Set up the default Dulwich loggers.

## remove_null_handler

[[find in source code]](../../dulwich/log_utils.py#L66)

```python
def remove_null_handler():
```

Remove the null handler from the Dulwich loggers.

If a caller wants to set up logging using something other than
default_logging_config, calling this function first is a minor optimization
to avoid the overhead of using the _NullHandler.
