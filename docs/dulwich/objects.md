# Objects

> Auto-generated documentation for [dulwich.objects](../../dulwich/objects.py) module.

Access to base git objects.

- [AddOns-Update-Tool](../README.md#addons-update-tool-index) / [Modules](../MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / Objects
    - [Blob](#blob)
        - [Blob().check](#blobcheck)
        - [Blob.from_path](#blobfrom_path)
        - [Blob().splitlines](#blobsplitlines)
    - [Commit](#commit)
        - [Commit().check](#commitcheck)
        - [Commit.from_path](#commitfrom_path)
    - [EmptyFileException](#emptyfileexception)
    - [FixedSha](#fixedsha)
        - [FixedSha().digest](#fixedshadigest)
        - [FixedSha().hexdigest](#fixedshahexdigest)
    - [ShaFile](#shafile)
        - [ShaFile().\_\_bytes\_\_](#shafile__bytes__)
        - [ShaFile().\_\_cmp\_\_](#shafile__cmp__)
        - [ShaFile().\_\_eq\_\_](#shafile__eq__)
        - [ShaFile().\_\_hash\_\_](#shafile__hash__)
        - [ShaFile().\_\_le\_\_](#shafile__le__)
        - [ShaFile().\_\_lt\_\_](#shafile__lt__)
        - [ShaFile().\_\_ne\_\_](#shafile__ne__)
        - [ShaFile().as_legacy_object](#shafileas_legacy_object)
        - [ShaFile().as_legacy_object_chunks](#shafileas_legacy_object_chunks)
        - [ShaFile().as_pretty_string](#shafileas_pretty_string)
        - [ShaFile().as_raw_chunks](#shafileas_raw_chunks)
        - [ShaFile().as_raw_string](#shafileas_raw_string)
        - [ShaFile().check](#shafilecheck)
        - [ShaFile().copy](#shafilecopy)
        - [ShaFile.from_file](#shafilefrom_file)
        - [ShaFile.from_path](#shafilefrom_path)
        - [ShaFile.from_raw_chunks](#shafilefrom_raw_chunks)
        - [ShaFile.from_raw_string](#shafilefrom_raw_string)
        - [ShaFile.from_string](#shafilefrom_string)
        - [ShaFile().get_type](#shafileget_type)
        - [ShaFile().id](#shafileid)
        - [ShaFile().raw_length](#shafileraw_length)
        - [ShaFile().set_raw_chunks](#shafileset_raw_chunks)
        - [ShaFile().set_raw_string](#shafileset_raw_string)
        - [ShaFile().set_type](#shafileset_type)
        - [ShaFile().sha](#shafilesha)
    - [SubmoduleEncountered](#submoduleencountered)
    - [Tag](#tag)
        - [Tag().check](#tagcheck)
        - [Tag.from_path](#tagfrom_path)
        - [Tag().sign](#tagsign)
        - [Tag().verify](#tagverify)
    - [Tree](#tree)
        - [Tree().\_\_setitem\_\_](#tree__setitem__)
        - [Tree().add](#treeadd)
        - [Tree().as_pretty_string](#treeas_pretty_string)
        - [Tree().check](#treecheck)
        - [Tree.from_path](#treefrom_path)
        - [Tree().items](#treeitems)
        - [Tree().iteritems](#treeiteritems)
        - [Tree().lookup_path](#treelookup_path)
    - [TreeEntry](#treeentry)
        - [TreeEntry().in_path](#treeentryin_path)
    - [S_ISGITLINK](#s_isgitlink)
    - [check_hexsha](#check_hexsha)
    - [check_identity](#check_identity)
    - [check_time](#check_time)
    - [filename_to_hex](#filename_to_hex)
    - [format_timezone](#format_timezone)
    - [git_line](#git_line)
    - [hex_to_filename](#hex_to_filename)
    - [hex_to_sha](#hex_to_sha)
    - [key_entry](#key_entry)
    - [key_entry_name_order](#key_entry_name_order)
    - [object_class](#object_class)
    - [object_header](#object_header)
    - [parse_commit](#parse_commit)
    - [parse_time_entry](#parse_time_entry)
    - [parse_timezone](#parse_timezone)
    - [parse_tree](#parse_tree)
    - [pretty_format_tree_entry](#pretty_format_tree_entry)
    - [serializable_property](#serializable_property)
    - [serialize_tree](#serialize_tree)
    - [sha_to_hex](#sha_to_hex)
    - [sorted_tree_items](#sorted_tree_items)
    - [valid_hexsha](#valid_hexsha)

## Blob

[[find in source code]](../../dulwich/objects.py#L583)

```python
class Blob(ShaFile):
    def __init__():
```

A Git Blob object.

#### See also

- [ShaFile](#shafile)

### Blob().check

[[find in source code]](../../dulwich/objects.py#L631)

```python
def check():
```

Check this object for internal consistency.

#### Raises

- `ObjectFormatException` - if the object is malformed in some way

### Blob.from_path

[[find in source code]](../../dulwich/objects.py#L624)

```python
@classmethod
def from_path(path):
```

### Blob().splitlines

[[find in source code]](../../dulwich/objects.py#L639)

```python
def splitlines():
```

Return list of lines in this blob.

This preserves the original line endings.

## Commit

[[find in source code]](../../dulwich/objects.py#L1347)

```python
class Commit(ShaFile):
    def __init__():
```

A git commit object

#### See also

- [ShaFile](#shafile)

### Commit().check

[[find in source code]](../../dulwich/objects.py#L1411)

```python
def check():
```

Check this object for internal consistency.

#### Raises

- `ObjectFormatException` - if the object is malformed in some way

### Commit.from_path

[[find in source code]](../../dulwich/objects.py#L1381)

```python
@classmethod
def from_path(path):
```

## EmptyFileException

[[find in source code]](../../dulwich/objects.py#L79)

```python
class EmptyFileException(FileFormatException):
```

An unexpectedly empty file was encountered.

#### See also

- [FileFormatException](errors.md#fileformatexception)

## FixedSha

[[find in source code]](../../dulwich/objects.py#L245)

```python
class FixedSha(object):
    def __init__(hexsha):
```

SHA object that behaves like hashlib's but is given a fixed value.

### FixedSha().digest

[[find in source code]](../../dulwich/objects.py#L258)

```python
def digest():
```

Return the raw SHA digest.

### FixedSha().hexdigest

[[find in source code]](../../dulwich/objects.py#L262)

```python
def hexdigest():
```

Return the hex SHA digest.

## ShaFile

[[find in source code]](../../dulwich/objects.py#L267)

```python
class ShaFile(object):
    def __init__():
```

A git SHA file.

#### Attributes

- `type` - DEPRECATED: use type_num or type_name as needed.: `property(get_type, set_type)`

### ShaFile().\_\_bytes\_\_

[[find in source code]](../../dulwich/objects.py#L343)

```python
def __bytes__():
```

Return raw string serialization of this object.

### ShaFile().\_\_cmp\_\_

[[find in source code]](../../dulwich/objects.py#L576)

```python
def __cmp__(other):
```

Compare the SHA of this object with that of the other object.

### ShaFile().\_\_eq\_\_

[[find in source code]](../../dulwich/objects.py#L560)

```python
def __eq__(other):
```

Return True if the SHAs of the two objects match.

### ShaFile().\_\_hash\_\_

[[find in source code]](../../dulwich/objects.py#L347)

```python
def __hash__():
```

Return unique hash for this object.

### ShaFile().\_\_le\_\_

[[find in source code]](../../dulwich/objects.py#L570)

```python
def __le__(other):
```

Check whether SHA of this object is less than or equal to the other.

### ShaFile().\_\_lt\_\_

[[find in source code]](../../dulwich/objects.py#L564)

```python
def __lt__(other):
```

Return whether SHA of this object is less than the other.

### ShaFile().\_\_ne\_\_

[[find in source code]](../../dulwich/objects.py#L556)

```python
def __ne__(other):
```

Check whether this object does not match the other.

### ShaFile().as_legacy_object

[[find in source code]](../../dulwich/objects.py#L319)

```python
def as_legacy_object(compression_level=-1):
```

Return string representing the object in the experimental format.

### ShaFile().as_legacy_object_chunks

[[find in source code]](../../dulwich/objects.py#L308)

```python
def as_legacy_object_chunks(compression_level=-1):
```

Return chunks representing the object in the experimental format.

Returns: List of strings

### ShaFile().as_pretty_string

[[find in source code]](../../dulwich/objects.py#L351)

```python
def as_pretty_string():
```

Return a string representing this object, fit for display.

### ShaFile().as_raw_chunks

[[find in source code]](../../dulwich/objects.py#L325)

```python
def as_raw_chunks():
```

Return chunks with serialization of the object.

Returns: List of strings, not necessarily one per line

### ShaFile().as_raw_string

[[find in source code]](../../dulwich/objects.py#L336)

```python
def as_raw_string():
```

Return raw string with serialization of the object.

Returns: String object

### ShaFile().check

[[find in source code]](../../dulwich/objects.py#L487)

```python
def check():
```

Check this object for internal consistency.

#### Raises

- `ObjectFormatException` - if the object is malformed in some way
- `ChecksumMismatch` - if the object was created with a SHA that does
  not match its contents

### ShaFile().copy

[[find in source code]](../../dulwich/objects.py#L530)

```python
def copy():
```

Create a new copy of this SHA1 object from its raw string

### ShaFile.from_file

[[find in source code]](../../dulwich/objects.py#L431)

```python
@classmethod
def from_file(f):
```

Get the contents of a SHA file on disk.

### ShaFile.from_path

[[find in source code]](../../dulwich/objects.py#L425)

```python
@classmethod
def from_path(path):
```

Open a SHA file from disk.

### ShaFile.from_raw_chunks

[[find in source code]](../../dulwich/objects.py#L454)

```python
@staticmethod
def from_raw_chunks(type_num, chunks, sha=None):
```

Creates an object of the indicated type from the raw chunks given.

#### Arguments

- `type_num` - The numeric type of the object.
- `chunks` - An iterable of the raw uncompressed contents.
- `sha` - Optional known sha for the object

### ShaFile.from_raw_string

[[find in source code]](../../dulwich/objects.py#L441)

```python
@staticmethod
def from_raw_string(type_num, string, sha=None):
```

Creates an object of the indicated type from the raw string given.

#### Arguments

- `type_num` - The numeric type of the object.
- `string` - The raw uncompressed contents.
- `sha` - Optional known sha for the object

### ShaFile.from_string

[[find in source code]](../../dulwich/objects.py#L467)

```python
@classmethod
def from_string(string):
```

Create a ShaFile from a string.

### ShaFile().get_type

[[find in source code]](../../dulwich/objects.py#L542)

```python
def get_type():
```

Return the type number for this object class.

### ShaFile().id

[[find in source code]](../../dulwich/objects.py#L537)

```python
@property
def id():
```

The hex SHA of this object.

### ShaFile().raw_length

[[find in source code]](../../dulwich/objects.py#L512)

```python
def raw_length():
```

Returns the length of the raw string of this object.

### ShaFile().set_raw_chunks

[[find in source code]](../../dulwich/objects.py#L361)

```python
def set_raw_chunks(chunks, sha=None):
```

Set the contents of this object from a list of chunks.

### ShaFile().set_raw_string

[[find in source code]](../../dulwich/objects.py#L355)

```python
def set_raw_string(text, sha=None):
```

Set the contents of this object from a serialized string.

### ShaFile().set_type

[[find in source code]](../../dulwich/objects.py#L546)

```python
def set_type(type):
```

Set the type number for this object class.

### ShaFile().sha

[[find in source code]](../../dulwich/objects.py#L519)

```python
def sha():
```

The SHA1 object that is the name of this object.

## SubmoduleEncountered

[[find in source code]](../../dulwich/objects.py#L1052)

```python
class SubmoduleEncountered(Exception):
    def __init__(path, sha):
```

A submodule was encountered while resolving a path.

## Tag

[[find in source code]](../../dulwich/objects.py#L721)

```python
class Tag(ShaFile):
    def __init__():
```

A Git Tag object.

#### See also

- [ShaFile](#shafile)

### Tag().check

[[find in source code]](../../dulwich/objects.py#L754)

```python
def check():
```

Check this object for internal consistency.

#### Raises

- `ObjectFormatException` - if the object is malformed in some way

### Tag.from_path

[[find in source code]](../../dulwich/objects.py#L747)

```python
@classmethod
def from_path(filename):
```

### Tag().sign

[[find in source code]](../../dulwich/objects.py#L885)

```python
def sign(keyid: Optional[str] = None):
```

### Tag().verify

[[find in source code]](../../dulwich/objects.py#L901)

```python
def verify(keyids: Optional[Iterable[str]] = None):
```

Verify GPG signature for this tag (if it is signed).

#### Arguments

- `keyids` - Optional iterable of trusted keyids for this tag.
  If this tag is not signed by any key in keyids verification will
  fail. If not specified, this function only verifies that the tag
  has a valid signature.

#### Raises

- `gpg.errors.BadSignatures` - if GPG signature verification fails
- `gpg.errors.MissingSignatures` - if tag was not signed by a key
  specified in keyids

## Tree

[[find in source code]](../../dulwich/objects.py#L1060)

```python
class Tree(ShaFile):
    def __init__():
```

A Git tree object

#### See also

- [ShaFile](#shafile)

### Tree().\_\_setitem\_\_

[[find in source code]](../../dulwich/objects.py#L1085)

```python
def __setitem__(name, value):
```

Set a tree entry by name.

#### Arguments

- `name` - The name of the entry, as a string.
- `value` - A tuple of (mode, hexsha), where mode is the mode of the
  entry as an integral type and hexsha is the hex SHA of the entry as
  a string.

### Tree().add

[[find in source code]](../../dulwich/objects.py#L1108)

```python
def add(name, mode, hexsha):
```

Add an entry to the tree.

#### Arguments

- `mode` - The mode of the entry as an integral type. Not all
  possible modes are supported by git; see check() for details.
- `name` - The name of the entry, as a string.
- `hexsha` - The hex SHA of the entry as a string.

### Tree().as_pretty_string

[[find in source code]](../../dulwich/objects.py#L1193)

```python
def as_pretty_string():
```

### Tree().check

[[find in source code]](../../dulwich/objects.py#L1155)

```python
def check():
```

Check this object for internal consistency.

#### Raises

- `ObjectFormatException` - if the object is malformed in some way

### Tree.from_path

[[find in source code]](../../dulwich/objects.py#L1072)

```python
@classmethod
def from_path(filename):
```

### Tree().items

[[find in source code]](../../dulwich/objects.py#L1137)

```python
def items():
```

Return the sorted entries in this tree.

Returns: List with (name, mode, sha) tuples

### Tree().iteritems

[[find in source code]](../../dulwich/objects.py#L1127)

```python
def iteritems(name_order=False):
```

Iterate over entries.

#### Arguments

  - `name_order` - If True, iterate in name order instead of tree
    order.
- `Returns` - Iterator over (name, mode, sha) tuples

### Tree().lookup_path

[[find in source code]](../../dulwich/objects.py#L1199)

```python
def lookup_path(lookup_obj, path):
```

Look up an object in a Git tree.

#### Arguments

  - `lookup_obj` - Callback for retrieving object by SHA1
  - `path` - Path to lookup
- `Returns` - A tuple of (mode, SHA) of the resulting path.

## TreeEntry

[[find in source code]](../../dulwich/objects.py#L937)

```python
class TreeEntry(namedtuple('TreeEntry', ['path', 'mode', 'sha'])):
```

Named tuple encapsulating a single tree entry.

### TreeEntry().in_path

[[find in source code]](../../dulwich/objects.py#L940)

```python
def in_path(path):
```

Return a copy of this entry with the given path prepended.

## S_ISGITLINK

[[find in source code]](../../dulwich/objects.py#L83)

```python
def S_ISGITLINK(m):
```

Check if a mode indicates a submodule.

#### Arguments

  - `m` - Mode to check
- `Returns` - a ``boolean``

## check_hexsha

[[find in source code]](../../dulwich/objects.py#L189)

```python
def check_hexsha(hex, error_msg):
```

Check if a string is a valid hex sha string.

#### Arguments

- `hex` - Hex string to check
- `error_msg` - Error message to use in exception

#### Raises

- `ObjectFormatException` - Raised when the string is not valid

## check_identity

[[find in source code]](../../dulwich/objects.py#L202)

```python
def check_identity(identity, error_msg):
```

Check if the specified identity is valid.

This will raise an exception if the identity is not valid.

#### Arguments

- `identity` - Identity string
- `error_msg` - Error message to use in exception

## check_time

[[find in source code]](../../dulwich/objects.py#L224)

```python
def check_time(time_seconds):
```

Check if the specified time is not prone to overflow error.

This will raise an exception if the time is not valid.

#### Arguments

- `time_seconds` - time in seconds

## filename_to_hex

[[find in source code]](../../dulwich/objects.py#L142)

```python
def filename_to_hex(filename):
```

Takes an object filename and returns its corresponding hex sha.

## format_timezone

[[find in source code]](../../dulwich/objects.py#L1251)

```python
def format_timezone(offset, unnecessary_negative_timezone=False):
```

Format a timezone for Git serialization.

#### Arguments

- `offset` - Timezone offset as seconds difference to UTC
- `unnecessary_negative_timezone` - Whether to use a minus sign for
  UTC or positive timezones (-0000 and --700 rather than +0000 / +0700).

## git_line

[[find in source code]](../../dulwich/objects.py#L240)

```python
def git_line(*items):
```

Formats items into a space separated line.

## hex_to_filename

[[find in source code]](../../dulwich/objects.py#L129)

```python
def hex_to_filename(path, hex):
```

Takes a hex sha and returns its filename relative to the given path.

## hex_to_sha

[[find in source code]](../../dulwich/objects.py#L107)

```python
def hex_to_sha(hex):
```

Takes a hex sha and returns a binary sha

## key_entry

[[find in source code]](../../dulwich/objects.py#L1014)

```python
def key_entry(entry):
```

Sort key for tree entry.

#### Arguments

- `entry` - (name, value) tuplee

## key_entry_name_order

[[find in source code]](../../dulwich/objects.py#L1026)

```python
def key_entry_name_order(entry):
```

Sort key for tree entry in name order.

## object_class

[[find in source code]](../../dulwich/objects.py#L178)

```python
def object_class(type):
```

Get the object class corresponding to the given type.

#### Arguments

  - `type` - Either a type name string or a numeric type.
- `Returns` - The ShaFile subclass corresponding to the given type, or None if
    type is not a valid type name/number.

## object_header

[[find in source code]](../../dulwich/objects.py#L155)

```python
def object_header(num_type: int, length: int) -> bytes:
```

Return an object header for the given numeric type and text length.

## parse_commit

[[find in source code]](../../dulwich/objects.py#L1296)

```python
def parse_commit(chunks):
```

Parse a commit object from chunks.

#### Arguments

  - `chunks` - Chunks to parse
- `Returns` - Tuple of (tree, parents, author_info, commit_info,
    encoding, mergetag, gpgsig, message, extra)

## parse_time_entry

[[find in source code]](../../dulwich/objects.py#L1271)

```python
def parse_time_entry(value):
```

Parse time entry behavior

#### Arguments

- `value` - Bytes representing a git commit/tag line

#### Raises

  ObjectFormatException in case of parsing error (malformed
  field date)
- `Returns` - Tuple of (author, time, (timezone, timezone_neg_utc))

## parse_timezone

[[find in source code]](../../dulwich/objects.py#L1222)

```python
def parse_timezone(text):
```

Parse a timezone text fragment (e.g. '+0100').

#### Arguments

  - `text` - Text to parse.
- `Returns` - Tuple with timezone as seconds difference to UTC
    and a boolean indicating whether this was a UTC timezone
    prefixed with a negative sign (-0000).

## parse_tree

[[find in source code]](../../dulwich/objects.py#L947)

```python
def parse_tree(text, strict=False):
```

Parse a tree text.

#### Arguments

  - `text` - Serialized text to parse
- `Returns` - iterator of tuples of (name, mode, sha)

#### Raises

- `ObjectFormatException` - if the object was malformed in some way

## pretty_format_tree_entry

[[find in source code]](../../dulwich/objects.py#L1031)

```python
def pretty_format_tree_entry(name, mode, hexsha, encoding='utf-8'):
```

Pretty format tree entry.

#### Arguments

  - `name` - Name of the directory entry
  - `mode` - Mode of entry
  - `hexsha` - Hexsha of the referenced object
- `Returns` - string describing the tree entry

## serializable_property

[[find in source code]](../../dulwich/objects.py#L165)

```python
def serializable_property(name: str, docstring: Optional[str] = None):
```

A property that helps tracking whether serialization is necessary.

## serialize_tree

[[find in source code]](../../dulwich/objects.py#L977)

```python
def serialize_tree(items):
```

Serialize the items in a tree to a text.

#### Arguments

  - `items` - Sorted iterable over (name, mode, sha) tuples
- `Returns` - Serialized tree text as chunks

## sha_to_hex

[[find in source code]](../../dulwich/objects.py#L100)

```python
def sha_to_hex(sha):
```

Takes a string and returns the hex of the sha within

## sorted_tree_items

[[find in source code]](../../dulwich/objects.py#L994)

```python
def sorted_tree_items(entries, name_order):
```

Iterate over a tree entries dictionary.

#### Arguments

  - `name_order` - If True, iterate entries in order of their name. If
    False, iterate entries in tree order, that is, treat subtree entries as
    having '/' appended.
  - `entries` - Dictionary mapping names to (mode, sha) tuples
- `Returns` - Iterator over (name, mode, hexsha)

## valid_hexsha

[[find in source code]](../../dulwich/objects.py#L118)

```python
def valid_hexsha(hex):
```
