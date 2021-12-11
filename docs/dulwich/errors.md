# Errors

> Auto-generated documentation for [dulwich.errors](blob/master/dulwich/errors.py) module.

Dulwich-related exception classes and utility functions.

- [Addons-update-tool](..\README.md#addons-update-tool) / [Modules](..\MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / Errors
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

[[find in source code]](blob/master/dulwich/errors.py#L107)

```python
class ApplyDeltaError(Exception):
    def __init__(*args, **kwargs):
```

Indicates that applying a delta failed.

## ChecksumMismatch

[[find in source code]](blob/master/dulwich/errors.py#L32)

```python
class ChecksumMismatch(Exception):
    def __init__(expected, got, extra=None):
```

A checksum didn't match the expected contents.

## CommitError

[[find in source code]](blob/master/dulwich/errors.py#L195)

```python
class CommitError(Exception):
```

An error occurred while performing a commit.

## FileFormatException

[[find in source code]](blob/master/dulwich/errors.py#L179)

```python
class FileFormatException(Exception):
```

Base class for exceptions relating to reading git file formats.

## GitProtocolError

[[find in source code]](blob/master/dulwich/errors.py#L121)

```python
class GitProtocolError(Exception):
    def __init__(*args, **kwargs):
```

Git protocol exception.

## HangupException

[[find in source code]](blob/master/dulwich/errors.py#L146)

```python
class HangupException(GitProtocolError):
    def __init__(stderr_lines=None):
```

Hangup exception.

#### See also

- [GitProtocolError](#gitprotocolerror)

## HookError

[[find in source code]](blob/master/dulwich/errors.py#L203)

```python
class HookError(Exception):
```

An error occurred while executing a hook.

## MissingCommitError

[[find in source code]](blob/master/dulwich/errors.py#L92)

```python
class MissingCommitError(Exception):
    def __init__(sha, *args, **kwargs):
```

Indicates that a commit was not found in the repository

## NoIndexPresent

[[find in source code]](blob/master/dulwich/errors.py#L191)

```python
class NoIndexPresent(Exception):
```

No index is present.

## NotBlobError

[[find in source code]](blob/master/dulwich/errors.py#L86)

```python
class NotBlobError(WrongObjectException):
```

Indicates that the sha requested does not point to a blob.

#### See also

- [WrongObjectException](#wrongobjectexception)

## NotCommitError

[[find in source code]](blob/master/dulwich/errors.py#L68)

```python
class NotCommitError(WrongObjectException):
```

Indicates that the sha requested does not point to a commit.

#### See also

- [WrongObjectException](#wrongobjectexception)

## NotGitRepository

[[find in source code]](blob/master/dulwich/errors.py#L114)

```python
class NotGitRepository(Exception):
    def __init__(*args, **kwargs):
```

Indicates that no Git repository was found.

## NotTagError

[[find in source code]](blob/master/dulwich/errors.py#L80)

```python
class NotTagError(WrongObjectException):
```

Indicates that the sha requested does not point to a tag.

#### See also

- [WrongObjectException](#wrongobjectexception)

## NotTreeError

[[find in source code]](blob/master/dulwich/errors.py#L74)

```python
class NotTreeError(WrongObjectException):
```

Indicates that the sha requested does not point to a tree.

#### See also

- [WrongObjectException](#wrongobjectexception)

## ObjectFormatException

[[find in source code]](blob/master/dulwich/errors.py#L187)

```python
class ObjectFormatException(FileFormatException):
```

Indicates an error parsing an object.

#### See also

- [FileFormatException](#fileformatexception)

## ObjectMissing

[[find in source code]](blob/master/dulwich/errors.py#L100)

```python
class ObjectMissing(Exception):
    def __init__(sha, *args, **kwargs):
```

Indicates that a requested object is missing.

## PackedRefsException

[[find in source code]](blob/master/dulwich/errors.py#L183)

```python
class PackedRefsException(FileFormatException):
```

Indicates an error parsing a packed-refs file.

#### See also

- [FileFormatException](#fileformatexception)

## RefFormatError

[[find in source code]](blob/master/dulwich/errors.py#L199)

```python
class RefFormatError(Exception):
```

Indicates an invalid ref name.

## SendPackError

[[find in source code]](blob/master/dulwich/errors.py#L131)

```python
class SendPackError(GitProtocolError):
```

An error occurred during send_pack.

#### See also

- [GitProtocolError](#gitprotocolerror)

## UnexpectedCommandError

[[find in source code]](blob/master/dulwich/errors.py#L166)

```python
class UnexpectedCommandError(GitProtocolError):
    def __init__(command):
```

Unexpected command received in a proto line.

#### See also

- [GitProtocolError](#gitprotocolerror)

## UpdateRefsError

[[find in source code]](blob/master/dulwich/errors.py#L138)

```python
class UpdateRefsError(GitProtocolError):
    def __init__(*args, **kwargs):
```

The server reported errors updating refs.

#### See also

- [GitProtocolError](#gitprotocolerror)

## WrongObjectException

[[find in source code]](blob/master/dulwich/errors.py#L55)

```python
class WrongObjectException(Exception):
    def __init__(sha, *args, **kwargs):
```

Baseclass for all the _ is not a _ exceptions on objects.

Do not instantiate directly.

Subclasses should define a type_name attribute that indicates what
was expected if they were raised.
