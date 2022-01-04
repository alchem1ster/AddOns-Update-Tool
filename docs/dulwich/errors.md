# Errors

> Auto-generated documentation for [dulwich.errors](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/errors.py) module.

Dulwich-related exception classes and utility functions.

- [AddOns-Update-Tool](../README.md#addons-update-tool-index) / [Modules](../MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / Errors
    - [ApplyDeltaError](#applydeltaerror)
    - [ChecksumMismatch](#checksummismatch)
    - [CommitError](#commiterror)
    - [FileFormatException](#fileformatexception)
    - [GitProtocolError](#gitprotocolerror)
    - [HangupException](#hangupexception)
    - [HookError](#hookerror)
    - [MissingCommitError](#missingcommiterror)
    - [NoIndexPresent](#noindexpresent)
    - [NotBlobError](#notbloberror)
    - [NotCommitError](#notcommiterror)
    - [NotGitRepository](#notgitrepository)
    - [NotTagError](#nottagerror)
    - [NotTreeError](#nottreeerror)
    - [ObjectFormatException](#objectformatexception)
    - [ObjectMissing](#objectmissing)
    - [PackedRefsException](#packedrefsexception)
    - [RefFormatError](#refformaterror)
    - [SendPackError](#sendpackerror)
    - [UnexpectedCommandError](#unexpectedcommanderror)
    - [UpdateRefsError](#updaterefserror)
    - [WrongObjectException](#wrongobjectexception)

## ApplyDeltaError

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/errors.py#L108)

```python
class ApplyDeltaError(Exception):
    def __init__(*args, **kwargs):
```

Indicates that applying a delta failed.

## ChecksumMismatch

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/errors.py#L32)

```python
class ChecksumMismatch(Exception):
    def __init__(expected, got, extra=None):
```

A checksum didn't match the expected contents.

## CommitError

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/errors.py#L202)

```python
class CommitError(Exception):
```

An error occurred while performing a commit.

## FileFormatException

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/errors.py#L186)

```python
class FileFormatException(Exception):
```

Base class for exceptions relating to reading git file formats.

## GitProtocolError

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/errors.py#L122)

```python
class GitProtocolError(Exception):
    def __init__(*args, **kwargs):
```

Git protocol exception.

## HangupException

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/errors.py#L147)

```python
class HangupException(GitProtocolError):
    def __init__(stderr_lines=None):
```

Hangup exception.

#### See also

- [GitProtocolError](#gitprotocolerror)

## HookError

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/errors.py#L210)

```python
class HookError(Exception):
```

An error occurred while executing a hook.

## MissingCommitError

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/errors.py#L93)

```python
class MissingCommitError(Exception):
    def __init__(sha, *args, **kwargs):
```

Indicates that a commit was not found in the repository

## NoIndexPresent

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/errors.py#L198)

```python
class NoIndexPresent(Exception):
```

No index is present.

## NotBlobError

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/errors.py#L87)

```python
class NotBlobError(WrongObjectException):
```

Indicates that the sha requested does not point to a blob.

#### See also

- [WrongObjectException](#wrongobjectexception)

## NotCommitError

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/errors.py#L69)

```python
class NotCommitError(WrongObjectException):
```

Indicates that the sha requested does not point to a commit.

#### See also

- [WrongObjectException](#wrongobjectexception)

## NotGitRepository

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/errors.py#L115)

```python
class NotGitRepository(Exception):
    def __init__(*args, **kwargs):
```

Indicates that no Git repository was found.

## NotTagError

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/errors.py#L81)

```python
class NotTagError(WrongObjectException):
```

Indicates that the sha requested does not point to a tag.

#### See also

- [WrongObjectException](#wrongobjectexception)

## NotTreeError

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/errors.py#L75)

```python
class NotTreeError(WrongObjectException):
```

Indicates that the sha requested does not point to a tree.

#### See also

- [WrongObjectException](#wrongobjectexception)

## ObjectFormatException

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/errors.py#L194)

```python
class ObjectFormatException(FileFormatException):
```

Indicates an error parsing an object.

#### See also

- [FileFormatException](#fileformatexception)

## ObjectMissing

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/errors.py#L101)

```python
class ObjectMissing(Exception):
    def __init__(sha, *args, **kwargs):
```

Indicates that a requested object is missing.

## PackedRefsException

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/errors.py#L190)

```python
class PackedRefsException(FileFormatException):
```

Indicates an error parsing a packed-refs file.

#### See also

- [FileFormatException](#fileformatexception)

## RefFormatError

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/errors.py#L206)

```python
class RefFormatError(Exception):
```

Indicates an invalid ref name.

## SendPackError

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/errors.py#L132)

```python
class SendPackError(GitProtocolError):
```

An error occurred during send_pack.

#### See also

- [GitProtocolError](#gitprotocolerror)

## UnexpectedCommandError

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/errors.py#L173)

```python
class UnexpectedCommandError(GitProtocolError):
    def __init__(command):
```

Unexpected command received in a proto line.

#### See also

- [GitProtocolError](#gitprotocolerror)

## UpdateRefsError

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/errors.py#L139)

```python
class UpdateRefsError(GitProtocolError):
    def __init__(*args, **kwargs):
```

The server reported errors updating refs.

#### See also

- [GitProtocolError](#gitprotocolerror)

## WrongObjectException

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/errors.py#L56)

```python
class WrongObjectException(Exception):
    def __init__(sha, *args, **kwargs):
```

Baseclass for all the _ is not a _ exceptions on objects.

Do not instantiate directly.

Subclasses should define a type_name attribute that indicates what
was expected if they were raised.
