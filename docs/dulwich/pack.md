# Pack

> Auto-generated documentation for [dulwich.pack](blob/master/dulwich/pack.py) module.

Classes for dealing with packed git objects.

- [Addons-update-tool](..\README.md#addons-update-tool) / [Modules](..\MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / Pack
    - [DeltaChainIterator](#deltachainiterator)
        - [DeltaChainIterator().ext_refs](#deltachainiteratorext_refs)
        - [DeltaChainIterator.for_pack_data](#deltachainiteratorfor_pack_data)
        - [DeltaChainIterator().record](#deltachainiteratorrecord)
        - [DeltaChainIterator().set_pack_data](#deltachainiteratorset_pack_data)
    - [FilePackIndex](#filepackindex)
        - [FilePackIndex().\_\_len\_\_](#filepackindex__len__)
        - [FilePackIndex().calculate_checksum](#filepackindexcalculate_checksum)
        - [FilePackIndex().check](#filepackindexcheck)
        - [FilePackIndex().close](#filepackindexclose)
        - [FilePackIndex().get_pack_checksum](#filepackindexget_pack_checksum)
        - [FilePackIndex().get_stored_checksum](#filepackindexget_stored_checksum)
        - [FilePackIndex().iterentries](#filepackindexiterentries)
        - [FilePackIndex().path](#filepackindexpath)
    - [MemoryPackIndex](#memorypackindex)
        - [MemoryPackIndex().get_pack_checksum](#memorypackindexget_pack_checksum)
        - [MemoryPackIndex().iterentries](#memorypackindexiterentries)
        - [MemoryPackIndex().object_sha1](#memorypackindexobject_sha1)
    - [Pack](#pack)
        - [Pack().\_\_contains\_\_](#pack__contains__)
        - [Pack().\_\_getitem\_\_](#pack__getitem__)
        - [Pack().\_\_iter\_\_](#pack__iter__)
        - [Pack().\_\_len\_\_](#pack__len__)
        - [Pack().check](#packcheck)
        - [Pack().check_length_and_checksum](#packcheck_length_and_checksum)
        - [Pack().close](#packclose)
        - [Pack().data](#packdata)
        - [Pack.from_lazy_objects](#packfrom_lazy_objects)
        - [Pack.from_objects](#packfrom_objects)
        - [Pack().get_raw](#packget_raw)
        - [Pack().get_raw_unresolved](#packget_raw_unresolved)
        - [Pack().get_stored_checksum](#packget_stored_checksum)
        - [Pack().index](#packindex)
        - [Pack().iterobjects](#packiterobjects)
        - [Pack().keep](#packkeep)
        - [Pack().name](#packname)
        - [Pack().pack_tuples](#packpack_tuples)
    - [PackData](#packdata)
        - [PackData().\_\_len\_\_](#packdata__len__)
        - [PackData().calculate_checksum](#packdatacalculate_checksum)
        - [PackData().check](#packdatacheck)
        - [PackData().close](#packdataclose)
        - [PackData().create_index](#packdatacreate_index)
        - [PackData().create_index_v1](#packdatacreate_index_v1)
        - [PackData().create_index_v2](#packdatacreate_index_v2)
        - [PackData().filename](#packdatafilename)
        - [PackData.from_file](#packdatafrom_file)
        - [PackData.from_path](#packdatafrom_path)
        - [PackData().get_compressed_data_at](#packdataget_compressed_data_at)
        - [PackData().get_object_at](#packdataget_object_at)
        - [PackData().get_ref](#packdataget_ref)
        - [PackData().get_stored_checksum](#packdataget_stored_checksum)
        - [PackData().iterentries](#packdataiterentries)
        - [PackData().iterobjects](#packdataiterobjects)
        - [PackData().path](#packdatapath)
        - [PackData().resolve_object](#packdataresolve_object)
        - [PackData().sorted_entries](#packdatasorted_entries)
    - [PackFileDisappeared](#packfiledisappeared)
    - [PackIndex](#packindex)
        - [PackIndex().\_\_iter\_\_](#packindex__iter__)
        - [PackIndex().\_\_len\_\_](#packindex__len__)
        - [PackIndex().get_pack_checksum](#packindexget_pack_checksum)
        - [PackIndex().iterentries](#packindexiterentries)
        - [PackIndex().object_index](#packindexobject_index)
        - [PackIndex().object_sha1](#packindexobject_sha1)
        - [PackIndex().objects_sha1](#packindexobjects_sha1)
    - [PackIndex1](#packindex1)
    - [PackIndex2](#packindex2)
    - [PackIndexer](#packindexer)
    - [PackInflater](#packinflater)
    - [PackStreamCopier](#packstreamcopier)
        - [PackStreamCopier().verify](#packstreamcopierverify)
    - [PackStreamReader](#packstreamreader)
        - [PackStreamReader().offset](#packstreamreaderoffset)
        - [PackStreamReader().read](#packstreamreaderread)
        - [PackStreamReader().read_objects](#packstreamreaderread_objects)
        - [PackStreamReader().recv](#packstreamreaderrecv)
    - [SHA1Reader](#sha1reader)
        - [SHA1Reader().check_sha](#sha1readercheck_sha)
        - [SHA1Reader().close](#sha1readerclose)
        - [SHA1Reader().read](#sha1readerread)
        - [SHA1Reader().tell](#sha1readertell)
    - [SHA1Writer](#sha1writer)
        - [SHA1Writer().close](#sha1writerclose)
        - [SHA1Writer().offset](#sha1writeroffset)
        - [SHA1Writer().tell](#sha1writertell)
        - [SHA1Writer().write](#sha1writerwrite)
        - [SHA1Writer().write_sha](#sha1writerwrite_sha)
    - [UnpackedObject](#unpackedobject)
        - [UnpackedObject().sha](#unpackedobjectsha)
        - [UnpackedObject().sha_file](#unpackedobjectsha_file)
    - [apply_delta](#apply_delta)
    - [bisect_find_sha](#bisect_find_sha)
    - [chunks_length](#chunks_length)
    - [compute_file_sha](#compute_file_sha)
    - [create_delta](#create_delta)
    - [deltify_pack_objects](#deltify_pack_objects)
    - [iter_sha1](#iter_sha1)
    - [load_pack_index](#load_pack_index)
    - [load_pack_index_file](#load_pack_index_file)
    - [obj_sha](#obj_sha)
    - [pack_object_header](#pack_object_header)
    - [pack_objects_to_data](#pack_objects_to_data)
    - [read_pack_header](#read_pack_header)
    - [read_zlib_chunks](#read_zlib_chunks)
    - [take_msb_bytes](#take_msb_bytes)
    - [unpack_object](#unpack_object)
    - [write_pack](#write_pack)
    - [write_pack_data](#write_pack_data)
    - [write_pack_header](#write_pack_header)
    - [write_pack_index_v1](#write_pack_index_v1)
    - [write_pack_index_v2](#write_pack_index_v2)
    - [write_pack_object](#write_pack_object)
    - [write_pack_objects](#write_pack_objects)

A pack is a compact representation of a bunch of objects, stored
using deltas where possible.

They have two parts, the pack file, which stores the data, and an index
that tells you where the data is.

To find an object you look in all of the index files 'til you find a
match for the object name. You then use the pointer got from this as
a pointer in to the corresponding packfile.

## DeltaChainIterator

[[find in source code]](blob/master/dulwich/pack.py#L1329)

```python
class DeltaChainIterator(object):
    def __init__(file_obj, resolve_ext_ref=None):
```

Abstract iterator over pack data based on delta chains.

Each object in the pack is guaranteed to be inflated exactly once,
regardless of how many objects reference it as a delta base. As a result,
memory usage is proportional to the length of the longest delta chain.

Subclasses can override _result to define the result type of the iterator.
By default, results are UnpackedObjects with the following members set:

* offset
* obj_type_num
* obj_chunks
* pack_type_num
* delta_base     (for delta types)
* comp_chunks    (if _include_comp is True)
* decomp_chunks
* decomp_len
* crc32          (if _compute_crc32 is True)

### DeltaChainIterator().ext_refs

[[find in source code]](blob/master/dulwich/pack.py#L1459)

```python
def ext_refs():
```

### DeltaChainIterator.for_pack_data

[[find in source code]](blob/master/dulwich/pack.py#L1362)

```python
@classmethod
def for_pack_data(pack_data, resolve_ext_ref=None):
```

### DeltaChainIterator().record

[[find in source code]](blob/master/dulwich/pack.py#L1370)

```python
def record(unpacked):
```

### DeltaChainIterator().set_pack_data

[[find in source code]](blob/master/dulwich/pack.py#L1381)

```python
def set_pack_data(pack_data):
```

## FilePackIndex

[[find in source code]](blob/master/dulwich/pack.py#L475)

```python
class FilePackIndex(PackIndex):
    def __init__(filename, file=None, contents=None, size=None):
```

Pack index that is based on a file.

To do the loop it opens the file, and indexes first 256 4 byte groups
with the first byte of the sha id. The value in the four byte group indexed
is the end of the group that shares the same starting byte. Subtract one
from the starting byte and index again to find the start of the group.
The values are sorted by sha id within the group, so do the math to find
the start and end offset and then bisect in to find if the value is
present.

#### See also

- [PackIndex](#packindex)

### FilePackIndex().\_\_len\_\_

[[find in source code]](blob/master/dulwich/pack.py#L524)

```python
def __len__():
```

Return the number of entries in this pack index.

### FilePackIndex().calculate_checksum

[[find in source code]](blob/master/dulwich/pack.py#L577)

```python
def calculate_checksum():
```

Calculate the SHA1 checksum over this pack index.

Returns: This is a 20-byte binary digest

### FilePackIndex().check

[[find in source code]](blob/master/dulwich/pack.py#L570)

```python
def check():
```

Check that the stored checksum matches the actual checksum.

### FilePackIndex().close

[[find in source code]](blob/master/dulwich/pack.py#L519)

```python
def close():
```

### FilePackIndex().get_pack_checksum

[[find in source code]](blob/master/dulwich/pack.py#L584)

```python
def get_pack_checksum():
```

Return the SHA1 checksum stored for the corresponding packfile.

Returns: 20-byte binary digest

### FilePackIndex().get_stored_checksum

[[find in source code]](blob/master/dulwich/pack.py#L591)

```python
def get_stored_checksum():
```

Return the SHA1 checksum stored for this index.

Returns: 20-byte binary digest

### FilePackIndex().iterentries

[[find in source code]](blob/master/dulwich/pack.py#L552)

```python
def iterentries():
```

Iterate over the entries in this pack index.

Returns: iterator over tuples with object name, offset in packfile and
    crc32 checksum.

### FilePackIndex().path

[[find in source code]](blob/master/dulwich/pack.py#L505)

```python
@property
def path():
```

## MemoryPackIndex

[[find in source code]](blob/master/dulwich/pack.py#L438)

```python
class MemoryPackIndex(PackIndex):
    def __init__(entries, pack_checksum=None):
```

Pack index that is stored entirely in memory.

#### See also

- [PackIndex](#packindex)

### MemoryPackIndex().get_pack_checksum

[[find in source code]](blob/master/dulwich/pack.py#L456)

```python
def get_pack_checksum():
```

### MemoryPackIndex().iterentries

[[find in source code]](blob/master/dulwich/pack.py#L471)

```python
def iterentries():
```

### MemoryPackIndex().object_sha1

[[find in source code]](blob/master/dulwich/pack.py#L465)

```python
def object_sha1(index):
```

## Pack

[[find in source code]](blob/master/dulwich/pack.py#L1965)

```python
class Pack(object):
    def __init__(basename, resolve_ext_ref=None):
```

A Git pack object.

### Pack().\_\_contains\_\_

[[find in source code]](blob/master/dulwich/pack.py#L2074)

```python
def __contains__(sha1):
```

Check whether this pack contains a particular SHA1.

### Pack().\_\_getitem\_\_

[[find in source code]](blob/master/dulwich/pack.py#L2103)

```python
def __getitem__(sha1):
```

Retrieve the specified SHA1.

### Pack().\_\_iter\_\_

[[find in source code]](blob/master/dulwich/pack.py#L2044)

```python
def __iter__():
```

Iterate over all the sha1s of the objects in this pack.

### Pack().\_\_len\_\_

[[find in source code]](blob/master/dulwich/pack.py#L2037)

```python
def __len__():
```

Number of entries in this pack.

### Pack().check

[[find in source code]](blob/master/dulwich/pack.py#L2059)

```python
def check():
```

Check the integrity of this pack.

#### Raises

- `ChecksumMismatch` - if a checksum for the index or data is wrong

### Pack().check_length_and_checksum

[[find in source code]](blob/master/dulwich/pack.py#L2048)

```python
def check_length_and_checksum():
```

Sanity check the length and checksum of the pack index and data.

### Pack().close

[[find in source code]](blob/master/dulwich/pack.py#L2022)

```python
def close():
```

### Pack().data

[[find in source code]](blob/master/dulwich/pack.py#L2003)

```python
@property
def data():
```

The pack data object being used.

### Pack.from_lazy_objects

[[find in source code]](blob/master/dulwich/pack.py#L1978)

```python
@classmethod
def from_lazy_objects(data_fn, idx_fn):
```

Create a new pack object from callables to load pack data and
index objects.

### Pack.from_objects

[[find in source code]](blob/master/dulwich/pack.py#L1987)

```python
@classmethod
def from_objects(data, idx):
```

Create a new pack object from pack data and index objects.

### Pack().get_raw

[[find in source code]](blob/master/dulwich/pack.py#L2097)

```python
def get_raw(sha1):
```

### Pack().get_raw_unresolved

[[find in source code]](blob/master/dulwich/pack.py#L2082)

```python
def get_raw_unresolved(sha1):
```

Get raw unresolved data for a SHA.

#### Arguments

  - `sha1` - SHA to return data for
- `Returns` - Tuple with pack object type, delta base (if applicable),
    list of data chunks

### Pack().get_stored_checksum

[[find in source code]](blob/master/dulwich/pack.py#L2071)

```python
def get_stored_checksum():
```

### Pack().index

[[find in source code]](blob/master/dulwich/pack.py#L2012)

```python
@property
def index():
```

The index being used.

Note: This may be an in-memory index

### Pack().iterobjects

[[find in source code]](blob/master/dulwich/pack.py#L2108)

```python
def iterobjects():
```

Iterate over the objects in this pack.

### Pack().keep

[[find in source code]](blob/master/dulwich/pack.py#L2133)

```python
def keep(msg=None):
```

Add a .keep file for the pack, preventing git from garbage collecting it.

#### Arguments

  - `msg` - A message written inside the .keep file; can be used later
    to determine whether or not a .keep file is obsolete.
- `Returns` - The path of the .keep file, as a string.

### Pack().name

[[find in source code]](blob/master/dulwich/pack.py#L1999)

```python
def name():
```

The SHA over the SHAs of the objects in this pack.

### Pack().pack_tuples

[[find in source code]](blob/master/dulwich/pack.py#L2114)

```python
def pack_tuples():
```

Provide an iterable for use with write_pack_objects.

Returns: Object that can iterate over (object, path) tuples
    and provides __len__

## PackData

[[find in source code]](blob/master/dulwich/pack.py#L1015)

```python
class PackData(object):
    def __init__(filename, file=None, size=None):
```

The data contained in a packfile.

Pack files can be accessed both sequentially for exploding a pack, and
directly with the help of an index to retrieve a specific object.

The objects within are either complete or a delta against another.

The header is variable length. If the MSB of each byte is set then it
indicates that the subsequent byte is still part of the header.
For the first byte the next MS bits are the type, which tells you the type
of object, and whether it is a delta. The LS byte is the lowest bits of the
size. For each subsequent byte the LS 7 bits are the next MS bits of the
size, i.e. the last byte of the header contains the MS bits of the size.

For the complete objects the data is stored as zlib deflated data.
The size in the header is the uncompressed object size, so to uncompress
you need to just keep feeding data to zlib until you get an object back,
or it errors on bad data. This is done here by just giving the complete
buffer from the start of the deflated object on. This is bad, but until I
get mmap sorted out it will have to do.

Currently there are no integrity checks done. Also no attempt is made to
try and detect the delta case, or a request for an object at the wrong
position.  It will all just throw a zlib or KeyError.

### PackData().\_\_len\_\_

[[find in source code]](blob/master/dulwich/pack.py#L1114)

```python
def __len__():
```

Returns the number of objects in this pack.

### PackData().calculate_checksum

[[find in source code]](blob/master/dulwich/pack.py#L1118)

```python
def calculate_checksum():
```

Calculate the checksum for this pack.

Returns: 20-byte binary SHA1 digest

### PackData().check

[[find in source code]](blob/master/dulwich/pack.py#L1289)

```python
def check():
```

Check the consistency of this pack.

### PackData().close

[[find in source code]](blob/master/dulwich/pack.py#L1080)

```python
def close():
```

### PackData().create_index

[[find in source code]](blob/master/dulwich/pack.py#L1269)

```python
def create_index(filename, progress=None, version=2):
```

Create an  index file for this data file.

#### Arguments

  - `filename` - Index filename.
  - `progress` - Progress report function
- `Returns` - Checksum of index file

### PackData().create_index_v1

[[find in source code]](blob/master/dulwich/pack.py#L1245)

```python
def create_index_v1(filename, progress=None):
```

Create a version 1 file for this data file.

#### Arguments

  - `filename` - Index filename.
  - `progress` - Progress report function
- `Returns` - Checksum of index file

### PackData().create_index_v2

[[find in source code]](blob/master/dulwich/pack.py#L1257)

```python
def create_index_v2(filename, progress=None):
```

Create a version 2 index file for this data file.

#### Arguments

  - `filename` - Index filename.
  - `progress` - Progress report function
- `Returns` - Checksum of index file

### PackData().filename

[[find in source code]](blob/master/dulwich/pack.py#L1064)

```python
@property
def filename():
```

### PackData.from_file

[[find in source code]](blob/master/dulwich/pack.py#L1072)

```python
@classmethod
def from_file(file, size=None):
```

### PackData.from_path

[[find in source code]](blob/master/dulwich/pack.py#L1076)

```python
@classmethod
def from_path(path):
```

### PackData().get_compressed_data_at

[[find in source code]](blob/master/dulwich/pack.py#L1296)

```python
def get_compressed_data_at(offset):
```

Given offset in the packfile return compressed data that is there.

Using the associated index the location of an object can be looked up,
and then the packfile can be asked directly for that object using this
function.

### PackData().get_object_at

[[find in source code]](blob/master/dulwich/pack.py#L1312)

```python
def get_object_at(offset):
```

Given an offset in to the packfile return the object that is there.

Using the associated index the location of an object can be looked up,
and then the packfile can be asked directly for that object using this
function.

### PackData().get_ref

[[find in source code]](blob/master/dulwich/pack.py#L1125)

```python
def get_ref(sha):
```

Get the object for a ref SHA, only looking in this pack.

### PackData().get_stored_checksum

[[find in source code]](blob/master/dulwich/pack.py#L1284)

```python
def get_stored_checksum():
```

Return the expected checksum stored in this pack.

### PackData().iterentries

[[find in source code]](blob/master/dulwich/pack.py#L1218)

```python
def iterentries(progress=None):
```

Yield entries summarizing the contents of this pack.

#### Arguments

  - `progress` - Progress function, called with current and total
    object count.
- `Returns` - iterator of tuples with (sha, offset, crc32)

### PackData().iterobjects

[[find in source code]](blob/master/dulwich/pack.py#L1184)

```python
def iterobjects(progress=None, compute_crc32=True):
```

### PackData().path

[[find in source code]](blob/master/dulwich/pack.py#L1068)

```python
@property
def path():
```

### PackData().resolve_object

[[find in source code]](blob/master/dulwich/pack.py#L1142)

```python
def resolve_object(offset, type, obj, get_ref=None):
```

Resolve an object, possibly resolving deltas when necessary.

Returns: Tuple with object type and contents.

### PackData().sorted_entries

[[find in source code]](blob/master/dulwich/pack.py#L1234)

```python
def sorted_entries(progress=None):
```

Return entries in this pack, sorted by SHA.

#### Arguments

  - `progress` - Progress function, called with current and total
    object count
- `Returns` - List of tuples with (sha, offset, crc32)

## PackFileDisappeared

[[find in source code]](blob/master/dulwich/pack.py#L109)

```python
class PackFileDisappeared(Exception):
    def __init__(obj):
```

## PackIndex

[[find in source code]](blob/master/dulwich/pack.py#L348)

```python
class PackIndex(object):
```

An index in to a packfile.

Given a sha id of an object a pack index can tell you the location in the
packfile of that object if it has it.

### PackIndex().\_\_iter\_\_

[[find in source code]](blob/master/dulwich/pack.py#L373)

```python
def __iter__():
```

Iterate over the SHAs in this pack.

### PackIndex().\_\_len\_\_

[[find in source code]](blob/master/dulwich/pack.py#L369)

```python
def __len__():
```

Return the number of entries in this pack index.

### PackIndex().get_pack_checksum

[[find in source code]](blob/master/dulwich/pack.py#L385)

```python
def get_pack_checksum():
```

Return the SHA1 checksum stored for the corresponding packfile.

Returns: 20-byte binary digest

### PackIndex().iterentries

[[find in source code]](blob/master/dulwich/pack.py#L377)

```python
def iterentries():
```

Iterate over the entries in this pack index.

Returns: iterator over tuples with object name, offset in packfile and
    crc32 checksum.

### PackIndex().object_index

[[find in source code]](blob/master/dulwich/pack.py#L392)

```python
def object_index(sha):
```

Return the index in to the corresponding packfile for the object.

Given the name of an object it will return the offset that object
lives at within the corresponding pack file. If the pack file doesn't
have the object then None will be returned.

### PackIndex().object_sha1

[[find in source code]](blob/master/dulwich/pack.py#L409)

```python
def object_sha1(index):
```

Return the SHA1 corresponding to the index in the pack file.

### PackIndex().objects_sha1

[[find in source code]](blob/master/dulwich/pack.py#L426)

```python
def objects_sha1():
```

Return the hex SHA1 over all the shas of all objects in this pack.

Note: This is used for the filename of the pack.

## PackIndex1

[[find in source code]](blob/master/dulwich/pack.py#L617)

```python
class PackIndex1(FilePackIndex):
    def __init__(filename, file=None, contents=None, size=None):
```

Version 1 Pack Index file.

#### See also

- [FilePackIndex](#filepackindex)

## PackIndex2

[[find in source code]](blob/master/dulwich/pack.py#L642)

```python
class PackIndex2(FilePackIndex):
    def __init__(filename, file=None, contents=None, size=None):
```

Version 2 Pack Index file.

#### See also

- [FilePackIndex](#filepackindex)

## PackIndexer

[[find in source code]](blob/master/dulwich/pack.py#L1463)

```python
class PackIndexer(DeltaChainIterator):
```

Delta chain iterator that yields index entries.

#### See also

- [DeltaChainIterator](#deltachainiterator)

## PackInflater

[[find in source code]](blob/master/dulwich/pack.py#L1472)

```python
class PackInflater(DeltaChainIterator):
```

Delta chain iterator that yields ShaFile objects.

#### See also

- [DeltaChainIterator](#deltachainiterator)

## PackStreamCopier

[[find in source code]](blob/master/dulwich/pack.py#L932)

```python
class PackStreamCopier(PackStreamReader):
    def __init__(read_all, read_some, outfile, delta_iter=None):
```

Class to verify a pack stream as it is being read.

The pack is read from a ReceivableProtocol using read() or recv() as
appropriate and written out to the given file-like object.

#### See also

- [PackStreamReader](#packstreamreader)

### PackStreamCopier().verify

[[find in source code]](blob/master/dulwich/pack.py#L961)

```python
def verify():
```

Verify a pack stream and write it to the output file.

See PackStreamReader.iterobjects for a list of exceptions this may
throw.

## PackStreamReader

[[find in source code]](blob/master/dulwich/pack.py#L791)

```python
class PackStreamReader(object):
    def __init__(read_all, read_some=None, zlib_bufsize=_ZLIB_BUFSIZE):
```

Class to read a pack stream.

The pack is read from a ReceivableProtocol using read() or recv() as
appropriate.

### PackStreamReader().offset

[[find in source code]](blob/master/dulwich/pack.py#L851)

```python
@property
def offset():
```

### PackStreamReader().read

[[find in source code]](blob/master/dulwich/pack.py#L855)

```python
def read(size):
```

Read, blocking until size bytes are read.

### PackStreamReader().read_objects

[[find in source code]](blob/master/dulwich/pack.py#L877)

```python
def read_objects(compute_crc32=False):
```

Read the objects in this pack file.

#### Arguments

  - `compute_crc32` - If True, compute the CRC32 of the compressed
    data. If False, the returned CRC32 will be None.
- `Returns` - Iterator over UnpackedObjects with the following members set:
    offset
    obj_type_num
    obj_chunks (for non-delta types)
    delta_base (for delta types)
    decomp_chunks
    decomp_len
    crc32 (if compute_crc32 is True)

#### Raises

- `ChecksumMismatch` - if the checksum of the pack contents does not
  match the checksum in the pack trailer.
- `zlib.error` - if an error occurred during zlib decompression.
- `IOError` - if an error occurred writing to the output file.

### PackStreamReader().recv

[[find in source code]](blob/master/dulwich/pack.py#L864)

```python
def recv(size):
```

Read up to size bytes, blocking until one byte is read.

## SHA1Reader

[[find in source code]](blob/master/dulwich/pack.py#L1479)

```python
class SHA1Reader(object):
    def __init__(f):
```

Wrapper for file-like object that remembers the SHA1 of its data.

### SHA1Reader().check_sha

[[find in source code]](blob/master/dulwich/pack.py#L1491)

```python
def check_sha():
```

### SHA1Reader().close

[[find in source code]](blob/master/dulwich/pack.py#L1496)

```python
def close():
```

### SHA1Reader().read

[[find in source code]](blob/master/dulwich/pack.py#L1486)

```python
def read(num=None):
```

### SHA1Reader().tell

[[find in source code]](blob/master/dulwich/pack.py#L1499)

```python
def tell():
```

## SHA1Writer

[[find in source code]](blob/master/dulwich/pack.py#L1503)

```python
class SHA1Writer(object):
    def __init__(f):
```

Wrapper for file-like object that remembers the SHA1 of its data.

### SHA1Writer().close

[[find in source code]](blob/master/dulwich/pack.py#L1523)

```python
def close():
```

### SHA1Writer().offset

[[find in source code]](blob/master/dulwich/pack.py#L1528)

```python
def offset():
```

### SHA1Writer().tell

[[find in source code]](blob/master/dulwich/pack.py#L1531)

```python
def tell():
```

### SHA1Writer().write

[[find in source code]](blob/master/dulwich/pack.py#L1511)

```python
def write(data):
```

### SHA1Writer().write_sha

[[find in source code]](blob/master/dulwich/pack.py#L1516)

```python
def write_sha():
```

## UnpackedObject

[[find in source code]](blob/master/dulwich/pack.py#L114)

```python
class UnpackedObject(object):
    def __init__(pack_type_num, delta_base, decomp_len, crc32):
```

Class encapsulating an object unpacked from a pack file.

These objects should only be created from within unpack_object. Most
members start out as empty and are filled in at various points by
read_zlib_chunks, unpack_object, DeltaChainIterator, etc.

End users of this object should take care that the function they're getting
this object from is guaranteed to set the members they need.

### UnpackedObject().sha

[[find in source code]](blob/master/dulwich/pack.py#L158)

```python
def sha():
```

Return the binary SHA of this object.

### UnpackedObject().sha_file

[[find in source code]](blob/master/dulwich/pack.py#L164)

```python
def sha_file():
```

Return a ShaFile from this object.

## apply_delta

[[find in source code]](blob/master/dulwich/pack.py#L1853)

```python
def apply_delta(src_buf, delta):
```

Based on the similar function in git's patch-delta.c.

#### Arguments

- `src_buf` - Source buffer
- `delta` - Delta instructions

## bisect_find_sha

[[find in source code]](blob/master/dulwich/pack.py#L325)

```python
def bisect_find_sha(start, end, sha, unpack_name):
```

Find a SHA in a data blob with sorted SHAs.

#### Arguments

  - `start` - Start index of range to search
  - `end` - End index of range to search
  - `sha` - Sha to find
  - `unpack_name` - Callback to retrieve SHA by index
- `Returns` - Index of the SHA, or None if it wasn't found

## chunks_length

[[find in source code]](blob/master/dulwich/pack.py#L703)

```python
def chunks_length(chunks):
```

## compute_file_sha

[[find in source code]](blob/master/dulwich/pack.py#L987)

```python
def compute_file_sha(f, start_ofs=0, end_ofs=0, buffer_size=1 << 16):
```

Hash a portion of a file into a new SHA.

#### Arguments

  - `f` - A file-like object to read from that supports seek().
  - `start_ofs` - The offset in the file to start reading at.
  - `end_ofs` - The offset in the file to end reading at, relative to the
    end of the file.
  - `buffer_size` - A buffer size for reading.
- `Returns` - A new SHA object updated with data read from the file.

## create_delta

[[find in source code]](blob/master/dulwich/pack.py#L1809)

```python
def create_delta(base_buf, target_buf):
```

Use python difflib to work out how to transform base_buf to target_buf.

#### Arguments

- `base_buf` - Base buffer
- `target_buf` - Target buffer

## deltify_pack_objects

[[find in source code]](blob/master/dulwich/pack.py#L1629)

```python
def deltify_pack_objects(objects, window_size=None):
```

Generate deltas for pack objects.

#### Arguments

  - `objects` - An iterable of (object, path) tuples to deltify.
  - `window_size` - Window size; None for default
- `Returns` - Iterator over type_num, object id, delta_base, content
    delta_base is None for full text entries

## iter_sha1

[[find in source code]](blob/master/dulwich/pack.py#L260)

```python
def iter_sha1(iter):
```

Return the hexdigest of the SHA1 over a set of names.

#### Arguments

  - `iter` - Iterator over string objects
- `Returns` - 40-byte hex sha1 digest

## load_pack_index

[[find in source code]](blob/master/dulwich/pack.py#L273)

```python
def load_pack_index(path):
```

Load an index file by path.

#### Arguments

  - `filename` - Path to the index file
- `Returns` - A PackIndex loaded from the given path

## load_pack_index_file

[[find in source code]](blob/master/dulwich/pack.py#L306)

```python
def load_pack_index_file(path, f):
```

Load an index file from a file-like object.

#### Arguments

  - `path` - Path for the index file
  - `f` - File-like object
- `Returns` - A PackIndex loaded from the given file

## obj_sha

[[find in source code]](blob/master/dulwich/pack.py#L975)

```python
def obj_sha(type, chunks):
```

Compute the SHA for a numeric type and object chunks.

## pack_object_header

[[find in source code]](blob/master/dulwich/pack.py#L1535)

```python
def pack_object_header(type_num, delta_base, size):
```

Create a pack object header for the given object info.

#### Arguments

  - `type_num` - Numeric type of the object.
  - `delta_base` - Delta base offset or ref, or None for whole objects.
  - `size` - Uncompressed object size.
- `Returns` - A header for a packed object.

## pack_objects_to_data

[[find in source code]](blob/master/dulwich/pack.py#L1667)

```python
def pack_objects_to_data(objects):
```

Create pack data from objects

#### Arguments

  - `objects` - Pack objects
- `Returns` - Tuples with (type_num, hexdigest, delta base, object chunks)

## read_pack_header

[[find in source code]](blob/master/dulwich/pack.py#L683)

```python
def read_pack_header(read):
```

Read the header of a pack file.

#### Arguments

  - `read` - Read function
- `Returns` - Tuple of (pack version, number of objects). If no data is
    available to read, returns (None, None).

## read_zlib_chunks

[[find in source code]](blob/master/dulwich/pack.py#L196)

```python
def read_zlib_chunks(
    read_some,
    unpacked,
    include_comp=False,
    buffer_size=_ZLIB_BUFSIZE,
):
```

Read zlib data from a buffer.

This function requires that the buffer have additional data following the
compressed data, which is guaranteed to be the case for git pack files.

#### Arguments

  - `read_some` - Read function that returns at least one byte, but may
    return less than the requested size.
  - `unpacked` - An UnpackedObject to write result data to. If its crc32
    attr is not None, the CRC32 of the compressed bytes will be computed
    using this starting CRC32.
    After this function, will have the following attrs set:
    * comp_chunks    (if include_comp is True)
    * decomp_chunks
    * decomp_len
    * crc32
  - `include_comp` - If True, include compressed data in the result.
  - `buffer_size` - Size of the read buffer.
- `Returns` - Leftover unused data from the decompression.

#### Raises

- `zlib.error` - if a decompression error occurred.

## take_msb_bytes

[[find in source code]](blob/master/dulwich/pack.py#L94)

```python
def take_msb_bytes(read, crc32=None):
```

Read bytes marked with most significant bit.

#### Arguments

- `read` - Read function

## unpack_object

[[find in source code]](blob/master/dulwich/pack.py#L710)

```python
def unpack_object(
    read_all,
    read_some=None,
    compute_crc32=False,
    include_comp=False,
    zlib_bufsize=_ZLIB_BUFSIZE,
):
```

Unpack a Git object.

#### Arguments

  - `read_all` - Read function that blocks until the number of requested
    bytes are read.
  - `read_some` - Read function that returns at least one byte, but may not
    return the number of bytes requested.
  - `compute_crc32` - If True, compute the CRC32 of the compressed data. If
    False, the returned CRC32 will be None.
  - `include_comp` - If True, include compressed data in the result.
  - `zlib_bufsize` - An optional buffer size for zlib operations.
- `Returns` - A tuple of (unpacked, unused), where unused is the unused data
    leftover from decompression, and unpacked in an UnpackedObject with
    the following attrs set:

* obj_chunks     (for non-delta types)
* pack_type_num
* delta_base     (for delta types)
* comp_chunks    (if include_comp is True)
* decomp_chunks
* decomp_len
* crc32          (if compute_crc32 is True)

## write_pack

[[find in source code]](blob/master/dulwich/pack.py#L1591)

```python
def write_pack(
    filename,
    objects,
    deltify=None,
    delta_window_size=None,
    compression_level=-1,
):
```

Write a new pack data file.

#### Arguments

  - `filename` - Path to the new pack file (without .pack extension)
  - `objects` - Iterable of (object, path) tuples to write.
    Should provide __len__
  - `window_size` - Delta window size
  - `deltify` - Whether to deltify pack objects
  - `compression_level` - the zlib compression level
- `Returns` - Tuple with checksum of pack file and index file

## write_pack_data

[[find in source code]](blob/master/dulwich/pack.py#L1717)

```python
def write_pack_data(
    f,
    num_records,
    records,
    progress=None,
    compression_level=-1,
):
```

Write a new pack data file.

#### Arguments

  - `f` - File to write to
  - `num_records` - Number of records
  - `records` - Iterator over type_num, object_id, delta_base, raw
  - `progress` - Function to report progress to
  - `compression_level` - the zlib compression level
- `Returns` - Dict mapping id -> (offset, crc32 checksum), pack checksum

## write_pack_header

[[find in source code]](blob/master/dulwich/pack.py#L1622)

```python
def write_pack_header(f, num_objects):
```

Write a pack header for the given number of objects.

## write_pack_index_v1

[[find in source code]](blob/master/dulwich/pack.py#L1750)

```python
def write_pack_index_v1(f, entries, pack_checksum):
```

Write a new pack index file.

#### Arguments

  - `f` - A file-like object to write to
  - `entries` - List of tuples with object name (sha), offset_in_pack,
    and crc32_checksum.
  - `pack_checksum` - Checksum of the pack file.
- `Returns` - The SHA of the written index file

## write_pack_index_v2

[[find in source code]](blob/master/dulwich/pack.py#L1924)

```python
def write_pack_index_v2(f, entries, pack_checksum):
```

Write a new pack index file.

#### Arguments

  - `f` - File-like object to write to
  - `entries` - List of tuples with object name (sha), offset_in_pack, and
    crc32_checksum.
  - `pack_checksum` - Checksum of the pack file.
- `Returns` - The SHA of the index file written

## write_pack_object

[[find in source code]](blob/master/dulwich/pack.py#L1566)

```python
def write_pack_object(f, type, object, sha=None, compression_level=-1):
```

Write pack object to a file.

#### Arguments

  - `f` - File to write to
  - `type` - Numeric type of the object
  - `object` - Object to write
  - `compression_level` - the zlib compression level
- `Returns` - Tuple with offset at which the object was written, and crc32

## write_pack_objects

[[find in source code]](blob/master/dulwich/pack.py#L1684)

```python
def write_pack_objects(
    f,
    objects,
    delta_window_size=None,
    deltify=None,
    compression_level=-1,
):
```

Write a new pack data file.

#### Arguments

  - `f` - File to write to
  - `objects` - Iterable of (object, path) tuples to write.
    Should provide __len__
  - `window_size` - Sliding window size for searching for deltas;
                    Set to None for default window size.
  - `deltify` - Whether to deltify objects
  - `compression_level` - the zlib compression level to use
- `Returns` - Dict mapping id -> (offset, crc32 checksum), pack checksum
