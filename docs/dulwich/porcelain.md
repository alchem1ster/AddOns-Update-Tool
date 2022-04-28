# Porcelain

> Auto-generated documentation for [dulwich.porcelain](../../dulwich/porcelain.py) module.

Simple wrapper that provides porcelain-like functions on top of Dulwich.

- [AddOns-Update-Tool](../README.md#addons-update-tool-index) / [Modules](../MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / Porcelain
    - [DivergedBranches](#divergedbranches)
    - [Error](#error)
    - [NoneStream](#nonestream)
        - [NoneStream().read](#nonestreamread)
        - [NoneStream().readall](#nonestreamreadall)
        - [NoneStream().readinto](#nonestreamreadinto)
        - [NoneStream().write](#nonestreamwrite)
    - [RemoteExists](#remoteexists)
    - [active_branch](#active_branch)
    - [add](#add)
    - [archive](#archive)
    - [branch_create](#branch_create)
    - [branch_delete](#branch_delete)
    - [branch_list](#branch_list)
    - [check_diverged](#check_diverged)
    - [check_ignore](#check_ignore)
    - [check_mailmap](#check_mailmap)
    - [clean](#clean)
    - [clone](#clone)
    - [commit](#commit)
    - [commit_decode](#commit_decode)
    - [commit_encode](#commit_encode)
    - [commit_tree](#commit_tree)
    - [daemon](#daemon)
    - [describe](#describe)
    - [diff_tree](#diff_tree)
    - [fetch](#fetch)
    - [find_unique_abbrev](#find_unique_abbrev)
    - [fsck](#fsck)
    - [get_branch_remote](#get_branch_remote)
    - [get_object_by_path](#get_object_by_path)
    - [get_remote_repo](#get_remote_repo)
    - [get_tree_changes](#get_tree_changes)
    - [get_untracked_paths](#get_untracked_paths)
    - [init](#init)
    - [list_tags](#list_tags)
    - [log](#log)
    - [ls_files](#ls_files)
    - [ls_remote](#ls_remote)
    - [ls_tree](#ls_tree)
    - [open_repo](#open_repo)
    - [open_repo_closing](#open_repo_closing)
    - [pack_objects](#pack_objects)
    - [path_to_tree_path](#path_to_tree_path)
    - [print_commit](#print_commit)
    - [print_name_status](#print_name_status)
    - [print_tag](#print_tag)
    - [pull](#pull)
    - [push](#push)
    - [receive_pack](#receive_pack)
    - [remote_add](#remote_add)
    - [remove](#remove)
    - [repack](#repack)
    - [reset](#reset)
    - [reset_file](#reset_file)
    - [rev_list](#rev_list)
    - [show](#show)
    - [show_blob](#show_blob)
    - [show_commit](#show_commit)
    - [show_object](#show_object)
    - [show_tag](#show_tag)
    - [show_tree](#show_tree)
    - [stash_drop](#stash_drop)
    - [stash_list](#stash_list)
    - [stash_pop](#stash_pop)
    - [stash_push](#stash_push)
    - [status](#status)
    - [symbolic_ref](#symbolic_ref)
    - [tag](#tag)
    - [tag_create](#tag_create)
    - [tag_delete](#tag_delete)
    - [tag_list](#tag_list)
    - [update_head](#update_head)
    - [update_server_info](#update_server_info)
    - [upload_pack](#upload_pack)
    - [web_daemon](#web_daemon)
    - [write_tree](#write_tree)

Currently implemented:
 * archive
 * add
 * branch{_create,_delete,_list}
 * check-ignore
 * checkout
 * clone
 * commit
 * commit-tree
 * daemon
 * describe
 * diff-tree
 * fetch
 * init
 * ls-files
 * ls-remote
 * ls-tree
 * pull
 * push
 * rm
 * remote{_add}
 * receive-pack
 * reset
 * rev-list
 * tag{_create,_delete,_list}
 * upload-pack
 * update-server-info
 * status
 * symbolic-ref

These functions are meant to behave similarly to the git subcommands.
Differences in behaviour are considered bugs.

Note: one of the consequences of this is that paths tend to be
interpreted relative to the current working directory rather than relative
to the repository root.

Functions should generally accept both unicode strings and bytestrings

#### Attributes

- `GitStatus` - Module level tuple definition for status output: `namedtuple('GitStatus', 'staged unstaged untracked')`

## DivergedBranches

[[find in source code]](../../dulwich/porcelain.py#L256)

```python
class DivergedBranches(Error):
```

Branches have diverged and fast-forward is not possible.

#### See also

- [Error](#error)

## Error

[[find in source code]](../../dulwich/porcelain.py#L180)

```python
class Error(Exception):
    def __init__(msg, inner=None):
```

Porcelain-based error.

## NoneStream

[[find in source code]](../../dulwich/porcelain.py#L157)

```python
class NoneStream(RawIOBase):
```

Fallback if stdout or stderr are unavailable, does nothing.

### NoneStream().read

[[find in source code]](../../dulwich/porcelain.py#L160)

```python
def read(size=-1):
```

### NoneStream().readall

[[find in source code]](../../dulwich/porcelain.py#L163)

```python
def readall():
```

### NoneStream().readinto

[[find in source code]](../../dulwich/porcelain.py#L166)

```python
def readinto(b):
```

### NoneStream().write

[[find in source code]](../../dulwich/porcelain.py#L169)

```python
def write(b):
```

## RemoteExists

[[find in source code]](../../dulwich/porcelain.py#L188)

```python
class RemoteExists(Error):
```

Raised when the remote already exists.

#### See also

- [Error](#error)

## active_branch

[[find in source code]](../../dulwich/porcelain.py#L1465)

```python
def active_branch(repo):
```

Return the active branch in the repository, if any.

#### Arguments

- `repo` - Repository to open

#### Returns

branch name

#### Raises

- `KeyError` - if the repository does not have a working tree
- `IndexError` - if HEAD is floating

## add

[[find in source code]](../../dulwich/porcelain.py#L456)

```python
def add(repo='.', paths=None):
```

Add files to the staging area.

#### Arguments

  - `repo` - Repository for the files
  - `paths` - Paths to add.  No value passed stages all modified files.
- `Returns` - Tuple with set of added files and ignored files

If the repository contains ignored directories, the returned set will
contain the path to an ignored directory (with trailing slash). Individual
files within ignored directories will not be returned.

## archive

[[find in source code]](../../dulwich/porcelain.py#L276)

```python
def archive(
    repo,
    committish=None,
    outstream=default_bytes_out_stream,
    errstream=default_bytes_err_stream,
):
```

Create an archive.

#### Arguments

- `repo` - Path of repository for which to generate an archive.
- `committish` - Commit SHA1 or ref to use
- `outstream` - Output stream (defaults to stdout)
- `errstream` - Error stream (defaults to stderr)

#### See also

- [default_bytes_err_stream](#default_bytes_err_stream)
- [default_bytes_out_stream](#default_bytes_out_stream)

## branch_create

[[find in source code]](../../dulwich/porcelain.py#L1433)

```python
def branch_create(repo, name, objectish=None, force=False):
```

Create a branch.

#### Arguments

- `repo` - Path to the repository
- `name` - Name of the new branch
- `objectish` - Target object to point new branch at (defaults to HEAD)
- `force` - Force creation of branch, even if it already exists

## branch_delete

[[find in source code]](../../dulwich/porcelain.py#L1417)

```python
def branch_delete(repo, name):
```

Delete a branch.

#### Arguments

- `repo` - Path to the repository
- `name` - Name of the branch

## branch_list

[[find in source code]](../../dulwich/porcelain.py#L1455)

```python
def branch_list(repo):
```

List all branches.

#### Arguments

- `repo` - Path to the repository

## check_diverged

[[find in source code]](../../dulwich/porcelain.py#L260)

```python
def check_diverged(repo, current_sha, new_sha):
```

Check if updating to a sha can be done with fast forwarding.

#### Arguments

- `repo` - Repository object
- `current_sha` - Current head sha
- `new_sha` - New head sha

## check_ignore

[[find in source code]](../../dulwich/porcelain.py#L1652)

```python
def check_ignore(repo, paths, no_index=False):
```

Debug gitignore files.

#### Arguments

  - `repo` - Path to the repository
  - `paths` - List of paths to check for
  - `no_index` - Don't check index
- `Returns` - List of ignored files

## check_mailmap

[[find in source code]](../../dulwich/porcelain.py#L1719)

```python
def check_mailmap(repo, contact):
```

Check canonical name and email of contact.

#### Arguments

  - `repo` - Path to the repository
  - `contact` - Contact name and/or email
- `Returns` - Canonical contact data

## clean

[[find in source code]](../../dulwich/porcelain.py#L509)

```python
def clean(repo='.', target_dir=None):
```

Remove any untracked files from the target directory recursively

Equivalent to running ``git clean -fd`` in target_dir.

#### Arguments

- `repo` - Repository where the files may be tracked
- `target_dir` - Directory to clean - current directory if None

## clone

[[find in source code]](../../dulwich/porcelain.py#L394)

```python
def clone(
    source,
    target=None,
    bare=False,
    checkout=None,
    errstream=default_bytes_err_stream,
    outstream=None,
    origin='origin',
    depth=None,
    branch=None,
    **kwargs,
):
```

Clone a local or remote git repository.

#### Arguments

  - `source` - Path or URL for source repository
  - `target` - Path to target repository (optional)
  - `bare` - Whether or not to create a bare repository
  - `checkout` - Whether or not to check-out HEAD after cloning
  - `errstream` - Optional stream to write progress to
  - `outstream` - Optional stream to write progress to (deprecated)
  - `origin` - Name of remote from the repository used to clone
  - `depth` - Depth to fetch at
  - `branch` - Optional branch or tag to be used as HEAD in the new repository
    instead of the cloned repository's HEAD.
- `Returns` - The new repository

#### See also

- [default_bytes_err_stream](#default_bytes_err_stream)

## commit

[[find in source code]](../../dulwich/porcelain.py#L326)

```python
def commit(
    repo='.',
    message=None,
    author=None,
    committer=None,
    encoding=None,
    no_verify=False,
):
```

Create a new commit.

#### Arguments

  - `repo` - Path to repository
  - `message` - Optional commit message
  - `author` - Optional author name and email
  - `committer` - Optional committer name and email
  - `no_verify` - Skip pre-commit and commit-msg hooks
- `Returns` - SHA1 of the new commit

## commit_decode

[[find in source code]](../../dulwich/porcelain.py#L608)

```python
def commit_decode(commit, contents, default_encoding=DEFAULT_ENCODING):
```

#### See also

- [DEFAULT_ENCODING](#default_encoding)

## commit_encode

[[find in source code]](../../dulwich/porcelain.py#L616)

```python
def commit_encode(commit, contents, default_encoding=DEFAULT_ENCODING):
```

#### See also

- [DEFAULT_ENCODING](#default_encoding)

## commit_tree

[[find in source code]](../../dulwich/porcelain.py#L362)

```python
def commit_tree(repo, tree, message=None, author=None, committer=None):
```

Create a new commit object.

#### Arguments

- `repo` - Path to repository
- `tree` - An existing tree object
- `author` - Optional author name and email
- `committer` - Optional committer name and email

## daemon

[[find in source code]](../../dulwich/porcelain.py#L1312)

```python
def daemon(path='.', address=None, port=None):
```

Run a daemon serving Git requests over TCP/IP.

#### Arguments

- `path` - Path to the directory to serve.
- `address` - Optional address to listen on (defaults to ::)
- `port` - Optional port to listen on (defaults to TCP_GIT_PORT)

## describe

[[find in source code]](../../dulwich/porcelain.py#L1805)

```python
def describe(repo):
```

Describe the repository version.

#### Arguments

  - `repo` - git repository
- `Returns` - a string description of the current git revision

- `Examples` - "gabcdefh", "v0.1" or "v0.1-5-gabcdefh".

## diff_tree

[[find in source code]](../../dulwich/porcelain.py#L840)

```python
def diff_tree(repo, old_tree, new_tree, outstream=default_bytes_out_stream):
```

Compares the content and mode of blobs found via two tree objects.

#### Arguments

- `repo` - Path to repository
- `old_tree` - Id of old tree
- `new_tree` - Id of new tree
- `outstream` - Stream to write to

#### See also

- [default_bytes_out_stream](#default_bytes_out_stream)

## fetch

[[find in source code]](../../dulwich/porcelain.py#L1503)

```python
def fetch(
    repo,
    remote_location=None,
    outstream=sys.stdout,
    errstream=default_bytes_err_stream,
    message=None,
    depth=None,
    prune=False,
    prune_tags=False,
    force=False,
    **kwargs,
):
```

Fetch objects from a remote server.

#### Arguments

- `repo` - Path to the repository
- `remote_location` - String identifying a remote server
- `outstream` - Output stream (defaults to stdout)
- `errstream` - Error stream (defaults to stderr)
- `message` - Reflog message (defaults to b"fetch: from <remote_name>")
- `depth` - Depth to fetch at
- `prune` - Prune remote removed refs
- `prune_tags` - Prune reomte removed tags

#### Returns

Dictionary with refs on the remote

#### See also

- [default_bytes_err_stream](#default_bytes_err_stream)

## find_unique_abbrev

[[find in source code]](../../dulwich/porcelain.py#L1798)

```python
def find_unique_abbrev(object_store, object_id):
```

For now, just return 7 characters.

## fsck

[[find in source code]](../../dulwich/porcelain.py#L1737)

```python
def fsck(repo):
```

Check a repository.

#### Arguments

  - `repo` - A path to the repository
- `Returns` - Iterator over errors/warnings

## get_branch_remote

[[find in source code]](../../dulwich/porcelain.py#L1483)

```python
def get_branch_remote(repo):
```

Return the active branch's remote name, if any.

#### Arguments

- `repo` - Repository to open

#### Returns

remote name

#### Raises

- `KeyError` - if the repository does not have a working tree

## get_object_by_path

[[find in source code]](../../dulwich/porcelain.py#L1878)

```python
def get_object_by_path(repo, path, committish=None):
```

Get an object by path.

#### Arguments

  - `repo` - A path to the repository
  - `path` - Path to look up
  - `committish` - Commit to look up path in
- `Returns` - A `ShaFile` object

## get_remote_repo

[[find in source code]](../../dulwich/porcelain.py#L992)

```python
def get_remote_repo(
    repo: Repo,
    remote_location: Optional[Union[str, bytes]] = None,
) -> Tuple[Optional[str], str]:
```

#### See also

- [Repo](repo.md#repo)

## get_tree_changes

[[find in source code]](../../dulwich/porcelain.py#L1277)

```python
def get_tree_changes(repo):
```

Return add/delete/modify changes to tree by comparing index to HEAD.

#### Arguments

  - `repo` - repo path or object
- `Returns` - dict with lists for each type of change

## get_untracked_paths

[[find in source code]](../../dulwich/porcelain.py#L1233)

```python
def get_untracked_paths(frompath, basepath, index, exclude_ignored=False):
```

Get untracked paths.

#### Arguments

- `frompath` - Path to walk
- `basepath` - Path to compare to
- `index` - Index to check against
- `exclude_ignored` - Whether to exclude ignored paths

- `Note` - ignored directories will never be walked for performance reasons.
  If exclude_ignored is False, only the path to an ignored directory will
  be yielded, no files inside the directory will be returned

## init

[[find in source code]](../../dulwich/porcelain.py#L377)

```python
def init(path='.', bare=False):
```

Create a new git repository.

#### Arguments

  - `path` - Path to repository.
  - `bare` - Whether to create a bare repository.
- `Returns` - A Repo instance

## list_tags

[[find in source code]](../../dulwich/porcelain.py#L935)

```python
def list_tags(*args, **kwargs):
```

## log

[[find in source code]](../../dulwich/porcelain.py#L767)

```python
def log(
    repo='.',
    paths=None,
    outstream=sys.stdout,
    max_entries=None,
    reverse=False,
    name_status=False,
):
```

Write commit logs.

#### Arguments

- `repo` - Path to repository
- `paths` - Optional set of specific paths to print entries for
- `outstream` - Stream to write log output to
- `reverse` - Reverse order in which entries are printed
- `name_status` - Print name status
- `max_entries` - Optional maximum number of entries to display

## ls_files

[[find in source code]](../../dulwich/porcelain.py#L1792)

```python
def ls_files(repo):
```

List all files in an index.

## ls_remote

[[find in source code]](../../dulwich/porcelain.py#L1551)

```python
def ls_remote(remote, config=None, **kwargs):
```

List the refs in a remote.

#### Arguments

- `remote` - Remote repository location
- `config` - Configuration to use

#### Returns

Dictionary with remote refs

## ls_tree

[[find in source code]](../../dulwich/porcelain.py#L1598)

```python
def ls_tree(
    repo,
    treeish=b'HEAD',
    outstream=sys.stdout,
    recursive=False,
    name_only=False,
):
```

List contents of a tree.

#### Arguments

- `repo` - Path to the repository
- `treeish` - Tree id to list
- `outstream` - Output stream (defaults to stdout)
- `recursive` - Whether to recursively list files
- `name_only` - Only print item name

## open_repo

[[find in source code]](../../dulwich/porcelain.py#L192)

```python
def open_repo(path_or_repo):
```

Open an argument that can be a repository or a path for a repository.

## open_repo_closing

[[find in source code]](../../dulwich/porcelain.py#L205)

```python
def open_repo_closing(path_or_repo):
```

Open an argument that can be a repository or a path for a repository.
returns a context manager that will close the repo on exit if the argument
is a path, else does nothing if the argument is a repo.

## pack_objects

[[find in source code]](../../dulwich/porcelain.py#L1578)

```python
def pack_objects(repo, object_ids, packf, idxf, delta_window_size=None):
```

Pack objects into a file.

#### Arguments

- `repo` - Path to the repository
- `object_ids` - List of object ids to write
- `packf` - File-like object to write to
- `idxf` - File-like object to write to (can be None)

## path_to_tree_path

[[find in source code]](../../dulwich/porcelain.py#L215)

```python
def path_to_tree_path(repopath, path, tree_encoding=DEFAULT_ENCODING):
```

Convert a path to a path usable in an index, e.g. bytes and relative to
the repository root.

#### Arguments

  - `repopath` - Repository path, absolute or relative to the cwd
  - `path` - A path, absolute or relative to the cwd
- `Returns` - A path formatted for use in e.g. an index

#### See also

- [DEFAULT_ENCODING](#default_encoding)

## print_commit

[[find in source code]](../../dulwich/porcelain.py#L624)

```python
def print_commit(commit, decode, outstream=sys.stdout):
```

Write a human-readable commit log entry.

#### Arguments

- `commit` - A `Commit` object
- `outstream` - A stream file to write to

## print_name_status

[[find in source code]](../../dulwich/porcelain.py#L738)

```python
def print_name_status(changes):
```

Print a simple status summary, listing changed files.

## print_tag

[[find in source code]](../../dulwich/porcelain.py#L652)

```python
def print_tag(tag, decode, outstream=sys.stdout):
```

Write a human-readable tag.

#### Arguments

- `tag` - A `Tag` object
- `decode` - Function for decoding bytes to unicode string
- `outstream` - A stream to write to

## pull

[[find in source code]](../../dulwich/porcelain.py#L1109)

```python
def pull(
    repo,
    remote_location=None,
    refspecs=None,
    outstream=default_bytes_out_stream,
    errstream=default_bytes_err_stream,
    fast_forward=True,
    force=False,
    **kwargs,
):
```

Pull from remote via dulwich.client

#### Arguments

- `repo` - Path to repository
- `remote_location` - Location of the remote
- `refspecs` - refspecs to fetch
- `outstream` - A stream file to write to output
- `errstream` - A stream file to write to errors

#### See also

- [default_bytes_err_stream](#default_bytes_err_stream)
- [default_bytes_out_stream](#default_bytes_out_stream)

## push

[[find in source code]](../../dulwich/porcelain.py#L1017)

```python
def push(
    repo,
    remote_location=None,
    refspecs=None,
    outstream=default_bytes_out_stream,
    errstream=default_bytes_err_stream,
    force=False,
    **kwargs,
):
```

Remote push with dulwich via dulwich.client

#### Arguments

- `repo` - Path to repository
- `remote_location` - Location of the remote
- `refspecs` - Refs to push to remote
- `outstream` - A stream file to write output
- `errstream` - A stream file to write errors
- `force` - Force overwriting refs

#### See also

- [default_bytes_err_stream](#default_bytes_err_stream)
- [default_bytes_out_stream](#default_bytes_out_stream)

## receive_pack

[[find in source code]](../../dulwich/porcelain.py#L1379)

```python
def receive_pack(path='.', inf=None, outf=None):
```

Receive a pack file after negotiating its contents using smart protocol.

#### Arguments

- `path` - Path to the repository
- `inf` - Input stream to communicate with client
- `outf` - Output stream to communicate with client

## remote_add

[[find in source code]](../../dulwich/porcelain.py#L1631)

```python
def remote_add(repo, name, url):
```

Add a remote.

#### Arguments

- `repo` - Path to the repository
- `name` - Remote name
- `url` - Remote URL

## remove

[[find in source code]](../../dulwich/porcelain.py#L557)

```python
def remove(repo='.', paths=None, cached=False):
```

Remove files from the staging area.

#### Arguments

- `repo` - Repository for the files
- `paths` - Paths to remove

## repack

[[find in source code]](../../dulwich/porcelain.py#L1566)

```python
def repack(repo):
```

Repack loose files in a repository.

Currently this only packs loose objects.

#### Arguments

- `repo` - Path to the repository

## reset

[[find in source code]](../../dulwich/porcelain.py#L975)

```python
def reset(repo, mode, treeish='HEAD'):
```

Reset current HEAD to the specified state.

#### Arguments

- `repo` - Path to repository
- `mode` - Mode ("hard", "soft", "mixed")
- `treeish` - Treeish to reset to

## reset_file

[[find in source code]](../../dulwich/porcelain.py#L1701)

```python
def reset_file(repo, file_path: str, target: bytes = b'HEAD'):
```

Reset the file to specific commit or branch.

#### Arguments

- `repo` - dulwich Repo object
- `file_path` - file to reset, relative to the repository path
- `target` - branch or commit or b'HEAD' to reset

## rev_list

[[find in source code]](../../dulwich/porcelain.py#L853)

```python
def rev_list(repo, commits, outstream=sys.stdout):
```

Lists commit objects in reverse chronological order.

#### Arguments

- `repo` - Path to repository
- `commits` - Commits over which to iterate
- `outstream` - Stream to write to

## show

[[find in source code]](../../dulwich/porcelain.py#L805)

```python
def show(
    repo='.',
    objects=None,
    outstream=sys.stdout,
    default_encoding=DEFAULT_ENCODING,
):
```

Print the changes in a commit.

#### Arguments

- `repo` - Path to repository
- `objects` - Objects to show (defaults to [HEAD])
- `outstream` - Stream to write to
- `default_encoding` - Default encoding to use if none is set in the
  commit

#### See also

- [DEFAULT_ENCODING](#default_encoding)

## show_blob

[[find in source code]](../../dulwich/porcelain.py#L670)

```python
def show_blob(repo, blob, decode, outstream=sys.stdout):
```

Write a blob to a stream.

#### Arguments

- `repo` - A `Repo` object
- `blob` - A `Blob` object
- `decode` - Function for decoding bytes to unicode string
- `outstream` - A stream file to write to

## show_commit

[[find in source code]](../../dulwich/porcelain.py#L682)

```python
def show_commit(repo, commit, decode, outstream=sys.stdout):
```

Show a commit to a stream.

#### Arguments

- `repo` - A `Repo` object
- `commit` - A `Commit` object
- `decode` - Function for decoding bytes to unicode string
- `outstream` - Stream to write to

## show_object

[[find in source code]](../../dulwich/porcelain.py#L729)

```python
def show_object(repo, obj, decode, outstream):
```

## show_tag

[[find in source code]](../../dulwich/porcelain.py#L716)

```python
def show_tag(repo, tag, decode, outstream=sys.stdout):
```

Print a tag to a stream.

#### Arguments

- `repo` - A `Repo` object
- `tag` - A `Tag` object
- `decode` - Function for decoding bytes to unicode string
- `outstream` - Stream to write to

## show_tree

[[find in source code]](../../dulwich/porcelain.py#L703)

```python
def show_tree(repo, tree, decode, outstream=sys.stdout):
```

Print a tree to a stream.

#### Arguments

- `repo` - A `Repo` object
- `tree` - A `Tree` object
- `decode` - Function for decoding bytes to unicode string
- `outstream` - Stream to write to

## stash_drop

[[find in source code]](../../dulwich/porcelain.py#L1783)

```python
def stash_drop(repo, index):
```

Drop a stash from the stack.

## stash_list

[[find in source code]](../../dulwich/porcelain.py#L1756)

```python
def stash_list(repo):
```

List all stashes in a repository.

## stash_pop

[[find in source code]](../../dulwich/porcelain.py#L1774)

```python
def stash_pop(repo, index):
```

Pop a stash from the stack.

## stash_push

[[find in source code]](../../dulwich/porcelain.py#L1765)

```python
def stash_push(repo):
```

Push a new stash onto the stack.

## status

[[find in source code]](../../dulwich/porcelain.py#L1171)

```python
def status(repo='.', ignored=False):
```

Returns staged, unstaged, and untracked changes relative to the HEAD.

#### Arguments

  - `repo` - Path to repository or repository object
  - `ignored` - Whether to include ignored files in untracked
- `Returns` - GitStatus tuple,
    staged -  dict with lists of staged paths (diff index/HEAD)
    unstaged -  list of unstaged paths (diff index/working-tree)
    untracked - list of untracked, un-ignored & non-.git paths

## symbolic_ref

[[find in source code]](../../dulwich/porcelain.py#L311)

```python
def symbolic_ref(repo, ref_name, force=False):
```

Set git symbolic ref into HEAD.

#### Arguments

- `repo` - path to the repository
- `ref_name` - short name of the new ref
- `force` - force settings without checking if it exists in refs/heads

## tag

[[find in source code]](../../dulwich/porcelain.py#L866)

```python
def tag(*args, **kwargs):
```

## tag_create

[[find in source code]](../../dulwich/porcelain.py#L875)

```python
def tag_create(
    repo,
    tag,
    author=None,
    message=None,
    annotated=False,
    objectish='HEAD',
    tag_time=None,
    tag_timezone=None,
    sign=False,
):
```

Creates a tag in git via dulwich calls:

#### Arguments

- `repo` - Path to repository
- `tag` - tag string
- `author` - tag author (optional, if annotated is set)
- `message` - tag message (optional)
- `annotated` - whether to create an annotated tag
- `objectish` - object the tag should point at, defaults to HEAD
- `tag_time` - Optional time for annotated tag
- `tag_timezone` - Optional timezone for annotated tag
- `sign` - GPG Sign the tag (bool, defaults to False,
  pass True to use default GPG key,
  pass a str containing Key ID to use a specific GPG key)

## tag_delete

[[find in source code]](../../dulwich/porcelain.py#L957)

```python
def tag_delete(repo, name):
```

Remove a tag.

#### Arguments

- `repo` - Path to repository
- `name` - Name of tag to remove

## tag_list

[[find in source code]](../../dulwich/porcelain.py#L945)

```python
def tag_list(repo, outstream=sys.stdout):
```

List all tags.

#### Arguments

- `repo` - Path to repository
- `outstream` - Stream to write tags to

## update_head

[[find in source code]](../../dulwich/porcelain.py#L1673)

```python
def update_head(repo, target, detached=False, new_branch=None):
```

Update HEAD to point at a new branch/commit.

Note that this does not actually update the working tree.

#### Arguments

- `repo` - Path to the repository
- `detached` - Create a detached head
- `target` - Branch or committish to switch to
- `new_branch` - New branch to create

## update_server_info

[[find in source code]](../../dulwich/porcelain.py#L301)

```python
def update_server_info(repo='.'):
```

Update server info files for a repository.

#### Arguments

- `repo` - path to the repository

## upload_pack

[[find in source code]](../../dulwich/porcelain.py#L1353)

```python
def upload_pack(path='.', inf=None, outf=None):
```

Upload a pack file after negotiating its contents using smart protocol.

#### Arguments

- `path` - Path to the repository
- `inf` - Input stream to communicate with client
- `outf` - Output stream to communicate with client

## web_daemon

[[find in source code]](../../dulwich/porcelain.py#L1326)

```python
def web_daemon(path='.', address=None, port=None):
```

Run a daemon serving Git requests over HTTP.

#### Arguments

- `path` - Path to the directory to serve
- `address` - Optional address to listen on (defaults to ::)
- `port` - Optional port to listen on (defaults to 80)

## write_tree

[[find in source code]](../../dulwich/porcelain.py#L1901)

```python
def write_tree(repo):
```

Write a tree object from the index.

#### Arguments

  - `repo` - Repository for which to write tree
- `Returns` - tree id for the tree that was written
