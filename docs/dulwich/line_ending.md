# Line Ending

> Auto-generated documentation for [dulwich.line_ending](blob/master/dulwich/line_ending.py) module.

All line-ending related functions, from conversions to config processing

- [Addons-update-tool](..\README.md#addons-update-tool) / [Modules](..\MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / Line Ending
    - [BlobNormalizer](#blobnormalizer)
        - [BlobNormalizer().checkin_normalize](#blobnormalizercheckin_normalize)
        - [BlobNormalizer().checkout_normalize](#blobnormalizercheckout_normalize)
    - [TreeBlobNormalizer](#treeblobnormalizer)
        - [TreeBlobNormalizer().checkin_normalize](#treeblobnormalizercheckin_normalize)
    - [convert_crlf_to_lf](#convert_crlf_to_lf)
    - [convert_lf_to_crlf](#convert_lf_to_crlf)
    - [get_checkin_filter](#get_checkin_filter)
    - [get_checkin_filter_autocrlf](#get_checkin_filter_autocrlf)
    - [get_checkout_filter](#get_checkout_filter)
    - [get_checkout_filter_autocrlf](#get_checkout_filter_autocrlf)
    - [normalize_blob](#normalize_blob)

Line-ending normalization is a complex beast. Here is some notes and details
about how it seems to work.

The normalization is a two-fold process that happens at two moments:

- When reading a file from the index and to the working directory. For example
  when doing a `git clone` or `git checkout` call. We call this process the
  read filter in this module.
- When writing a file to the index from the working directory. For example
  when doing a `git add` call. We call this process the write filter in this
  module.

Note that when checking status (getting unstaged changes), whether or not
normalization is done on write depends on whether or not the file in the
working dir has also been normalized on read:

- For autocrlf=true all files are always normalized on both read and write.
- For autocrlf=input files are only normalized on write if they are newly
  "added". Since files which are already committed are not normalized on
  checkout into the working tree, they are also left alone when staging
  modifications into the index.

One thing to know is that Git does line-ending normalization only on text
files. How does Git know that a file is text? We can either mark a file as a
text file, a binary file or ask Git to automatically decides. Git has an
heuristic to detect if a file is a text file or a binary file. It seems based
on the percentage of non-printable characters in files.

The code for this heuristic is here:
https://git.kernel.org/pub/scm/git/git.git/tree/convert.c#n46

Dulwich have an implementation with a slightly different heuristic, the
`is_binary` function in [Patch](patch.md#patch).

The binary detection heuristic implementation is close to the one in JGit:
https://github.com/eclipse/jgit/blob/f6873ffe522bbc3536969a3a3546bf9a819b92bf/org.eclipse.jgit/src/org/eclipse/jgit/diff/RawText.java#L300

There is multiple variables that impact the normalization.

First, a repository can contains a `.gitattributes` file (or more than one...)
that can further customize the operation on some file patterns, for example:

*.txt text

Force all `.txt` files to be treated as text files and to have their lines
endings normalized.

*.jpg -text

Force all `.jpg` files to be treated as binary files and to not have their
lines endings converted.

*.vcproj text eol=crlf

Force all `.vcproj` files to be treated as text files and to have their lines
endings converted into `CRLF` in working directory no matter the native EOL of
the platform.

*.sh text eol=lf

Force all `.sh` files to be treated as text files and to have their lines
endings converted into `LF` in working directory no matter the native EOL of
the platform.

If the `eol` attribute is not defined, Git uses the `core.eol` configuration
value described later.

* text=auto

Force all files to be scanned by the text file heuristic detection and to have
their line endings normalized in case they are detected as text files.

Git also have a obsolete attribute named `crlf` that can be translated to the
corresponding text attribute value.

Then there are some configuration option (that can be defined at the
repository or user level):

- core.autocrlf
- core.eol

`core.autocrlf` is taken into account for all files that doesn't have a `text`
attribute defined in `.gitattributes`; it takes three possible values:

- `true`: This forces all files on the working directory to have CRLF
  line-endings in the working directory and convert line-endings to LF
  when writing to the index. When autocrlf is set to true, eol value is
  ignored.
- `input`: Quite similar to the `true` value but only force the write
  filter, ie line-ending of new files added to the index will get their
  line-endings converted to LF.
- `false` (default): No normalization is done.

`core.eol` is the top-level configuration to define the line-ending to use
when applying the read_filer. It takes three possible values:

- `lf`: When normalization is done, force line-endings to be `LF` in the
  working directory.
- `crlf`: When normalization is done, force line-endings to be `CRLF` in
  the working directory.
- `native` (default): When normalization is done, force line-endings to be
  the platform's native line ending.

One thing to remember is when line-ending normalization is done on a file, Git
always normalize line-ending to `LF` when writing to the index.

There are sources that seems to indicate that Git won't do line-ending
normalization when a file contains mixed line-endings. I think this logic
might be in text / binary detection heuristic but couldn't find it yet.

Sources:
- https://git-scm.com/docs/git-config#git-config-coreeol
- https://git-scm.com/docs/git-config#git-config-coreautocrlf
- https://git-scm.com/docs/gitattributes#_checking_out_and_checking_in
- https://adaptivepatchwork.com/2012/03/01/mind-the-end-of-your-line/

## BlobNormalizer

[[find in source code]](blob/master/dulwich/line_ending.py#L217)

```python
class BlobNormalizer(object):
    def __init__(config_stack, gitattributes):
```

An object to store computation result of which filter to apply based
on configuration, gitattributes, path and operation (checkin or checkout)

### BlobNormalizer().checkin_normalize

[[find in source code]](blob/master/dulwich/line_ending.py#L244)

```python
def checkin_normalize(blob, tree_path):
```

Normalize a blob during a checkin operation

### BlobNormalizer().checkout_normalize

[[find in source code]](blob/master/dulwich/line_ending.py#L253)

```python
def checkout_normalize(blob, tree_path):
```

Normalize a blob during a checkout operation

## TreeBlobNormalizer

[[find in source code]](blob/master/dulwich/line_ending.py#L287)

```python
class TreeBlobNormalizer(BlobNormalizer):
    def __init__(config_stack, git_attributes, object_store, tree=None):
```

#### See also

- [BlobNormalizer](#blobnormalizer)

### TreeBlobNormalizer().checkin_normalize

[[find in source code]](blob/master/dulwich/line_ending.py#L297)

```python
def checkin_normalize(blob, tree_path):
```

## convert_crlf_to_lf

[[find in source code]](blob/master/dulwich/line_ending.py#L146)

```python
def convert_crlf_to_lf(text_hunk):
```

Convert CRLF in text hunk into LF

#### Arguments

  - `text_hunk` - A bytes string representing a text hunk
- `Returns` - The text hunk with the same type, with CRLF replaced into LF

## convert_lf_to_crlf

[[find in source code]](blob/master/dulwich/line_ending.py#L156)

```python
def convert_lf_to_crlf(text_hunk):
```

Convert LF in text hunk into CRLF

#### Arguments

  - `text_hunk` - A bytes string representing a text hunk
- `Returns` - The text hunk with the same type, with LF replaced into CRLF

## get_checkin_filter

[[find in source code]](blob/master/dulwich/line_ending.py#L176)

```python
def get_checkin_filter(core_eol, core_autocrlf, git_attributes):
```

Returns the correct checkin filter based on the passed arguments

## get_checkin_filter_autocrlf

[[find in source code]](blob/master/dulwich/line_ending.py#L200)

```python
def get_checkin_filter_autocrlf(core_autocrlf):
```

Returns the correct checkin filter base on autocrlf value

#### Arguments

  - `core_autocrlf` - The bytes configuration value of core.autocrlf.
    Valid values are: b'true', b'false' or b'input'.
- `Returns` - Either None if no filter has to be applied or a function
    accepting a single argument, a binary text hunk

## get_checkout_filter

[[find in source code]](blob/master/dulwich/line_ending.py#L168)

```python
def get_checkout_filter(core_eol, core_autocrlf, git_attributes):
```

Returns the correct checkout filter based on the passed arguments

## get_checkout_filter_autocrlf

[[find in source code]](blob/master/dulwich/line_ending.py#L184)

```python
def get_checkout_filter_autocrlf(core_autocrlf):
```

Returns the correct checkout filter base on autocrlf value

#### Arguments

  - `core_autocrlf` - The bytes configuration value of core.autocrlf.
    Valid values are: b'true', b'false' or b'input'.
- `Returns` - Either None if no filter has to be applied or a function
    accepting a single argument, a binary text hunk

## normalize_blob

[[find in source code]](blob/master/dulwich/line_ending.py#L263)

```python
def normalize_blob(blob, conversion, binary_detection):
```

Takes a blob as input returns either the original blob if
binary_detection is True and the blob content looks like binary, else
return a new blob with converted data
