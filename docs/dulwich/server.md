# Server

> Auto-generated documentation for [dulwich.server](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py) module.

Git smart network protocol server implementation.

- [AddOns-Update-Tool](../README.md#addons-update-tool-index) / [Modules](../MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / Server
    - [Backend](#backend)
        - [Backend().open_repository](#backendopen_repository)
    - [BackendRepo](#backendrepo)
        - [BackendRepo().fetch_objects](#backendrepofetch_objects)
        - [BackendRepo().get_peeled](#backendrepoget_peeled)
        - [BackendRepo().get_refs](#backendrepoget_refs)
    - [DictBackend](#dictbackend)
        - [DictBackend().open_repository](#dictbackendopen_repository)
    - [FileSystemBackend](#filesystembackend)
        - [FileSystemBackend().open_repository](#filesystembackendopen_repository)
    - [Handler](#handler)
        - [Handler().handle](#handlerhandle)
    - [MultiAckDetailedGraphWalkerImpl](#multiackdetailedgraphwalkerimpl)
        - [MultiAckDetailedGraphWalkerImpl().ack](#multiackdetailedgraphwalkerimplack)
        - [MultiAckDetailedGraphWalkerImpl().handle_done](#multiackdetailedgraphwalkerimplhandle_done)
        - [MultiAckDetailedGraphWalkerImpl().next](#multiackdetailedgraphwalkerimplnext)
    - [MultiAckGraphWalkerImpl](#multiackgraphwalkerimpl)
        - [MultiAckGraphWalkerImpl().ack](#multiackgraphwalkerimplack)
        - [MultiAckGraphWalkerImpl().handle_done](#multiackgraphwalkerimplhandle_done)
        - [MultiAckGraphWalkerImpl().next](#multiackgraphwalkerimplnext)
    - [PackHandler](#packhandler)
        - [PackHandler.capabilities](#packhandlercapabilities)
        - [PackHandler.capability_line](#packhandlercapability_line)
        - [PackHandler().has_capability](#packhandlerhas_capability)
        - [PackHandler.innocuous_capabilities](#packhandlerinnocuous_capabilities)
        - [PackHandler().notify_done](#packhandlernotify_done)
        - [PackHandler.required_capabilities](#packhandlerrequired_capabilities)
        - [PackHandler().set_client_capabilities](#packhandlerset_client_capabilities)
    - [ReceivePackHandler](#receivepackhandler)
        - [ReceivePackHandler.capabilities](#receivepackhandlercapabilities)
        - [ReceivePackHandler().handle](#receivepackhandlerhandle)
    - [SingleAckGraphWalkerImpl](#singleackgraphwalkerimpl)
        - [SingleAckGraphWalkerImpl().ack](#singleackgraphwalkerimplack)
        - [SingleAckGraphWalkerImpl().handle_done](#singleackgraphwalkerimplhandle_done)
        - [SingleAckGraphWalkerImpl().next](#singleackgraphwalkerimplnext)
    - [TCPGitRequestHandler](#tcpgitrequesthandler)
        - [TCPGitRequestHandler().handle](#tcpgitrequesthandlerhandle)
    - [TCPGitServer](#tcpgitserver)
        - [TCPGitServer().handle_error](#tcpgitserverhandle_error)
        - [TCPGitServer().verify_request](#tcpgitserververify_request)
    - [UploadArchiveHandler](#uploadarchivehandler)
        - [UploadArchiveHandler().handle](#uploadarchivehandlerhandle)
    - [UploadPackHandler](#uploadpackhandler)
        - [UploadPackHandler.capabilities](#uploadpackhandlercapabilities)
        - [UploadPackHandler().get_tagged](#uploadpackhandlerget_tagged)
        - [UploadPackHandler().handle](#uploadpackhandlerhandle)
        - [UploadPackHandler().progress](#uploadpackhandlerprogress)
        - [UploadPackHandler.required_capabilities](#uploadpackhandlerrequired_capabilities)
    - [generate_info_refs](#generate_info_refs)
    - [generate_objects_info_packs](#generate_objects_info_packs)
    - [main](#main)
    - [serve_command](#serve_command)
    - [update_server_info](#update_server_info)

For more detailed implementation on the network protocol, see the
Documentation/technical directory in the cgit distribution, and in particular:

* Documentation/technical/protocol-capabilities.txt
* Documentation/technical/pack-protocol.txt

Currently supported capabilities:

* include-tag
* thin-pack
* multi_ack_detailed
* multi_ack
* side-band-64k
* ofs-delta
* no-progress
* report-status
* delete-refs
* shallow
* symref

#### Attributes

- `DEFAULT_HANDLERS` - Default handler classes for git services.: `{b'git-upload-pack': UploadPackHandler, b'git-r...`

## Backend

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L125)

```python
class Backend(object):
```

A backend for the Git smart server implementation.

### Backend().open_repository

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L128)

```python
def open_repository(path):
```

Open the repository at a path.

#### Arguments

- `path` - Path to the repository

#### Raises

  - `NotGitRepository` - no git repository was found at path
- `Returns` - Instance of BackendRepo

## BackendRepo

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L140)

```python
class BackendRepo(object):
```

Repository abstraction used by the Git server.

The methods required here are a subset of those provided by
dulwich.repo.Repo.

### BackendRepo().fetch_objects

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L170)

```python
def fetch_objects(determine_wants, graph_walker, progress, get_tagged=None):
```

Yield the objects required for a list of commits.

#### Arguments

- `progress` - is a callback to send progress messages to the client
- `get_tagged` - Function that returns a dict of pointed-to sha ->
  tag sha for including tags.

### BackendRepo().get_peeled

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L158)

```python
def get_peeled(name: bytes) -> Optional[bytes]:
```

Return the cached peeled value of a ref, if available.

#### Arguments

  - `name` - Name of the ref to peel
- `Returns` - The peeled value of the ref. If the ref is known not point to
    a tag, this will be the SHA the ref refers to. If no cached
    information about a tag is available, this method may return None,
    but it should attempt to peel the tag if possible.

### BackendRepo().get_refs

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L150)

```python
def get_refs() -> Dict[bytes, bytes]:
```

Get all the refs in the repository

Returns: dict of name -> sha

## DictBackend

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L184)

```python
class DictBackend(Backend):
    def __init__(repos):
```

Trivial backend that looks up Git repositories in a dictionary.

#### See also

- [Backend](#backend)

### DictBackend().open_repository

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L190)

```python
def open_repository(path: str) -> BaseRepo:
```

#### See also

- [BaseRepo](repo.md#baserepo)

## FileSystemBackend

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L200)

```python
class FileSystemBackend(Backend):
    def __init__(root=os.sep):
```

Simple backend looking up Git repositories in the local file system.

#### See also

- [Backend](#backend)

### FileSystemBackend().open_repository

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L209)

```python
def open_repository(path):
```

## Handler

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L221)

```python
class Handler(object):
    def __init__(backend, proto, stateless_rpc=None):
```

Smart protocol command handler base class.

### Handler().handle

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L229)

```python
def handle():
```

## MultiAckDetailedGraphWalkerImpl

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L876)

```python
class MultiAckDetailedGraphWalkerImpl(object):
    def __init__(walker):
```

Graph walker implementation speaking the multi-ack-detailed protocol.

### MultiAckDetailedGraphWalkerImpl().ack

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L883)

```python
def ack(have_ref):
```

### MultiAckDetailedGraphWalkerImpl().handle_done

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L917)

```python
def handle_done(done_required, done_received):
```

### MultiAckDetailedGraphWalkerImpl().next

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L888)

```python
def next():
```

## MultiAckGraphWalkerImpl

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L817)

```python
class MultiAckGraphWalkerImpl(object):
    def __init__(walker):
```

Graph walker implementation that speaks the multi-ack protocol.

### MultiAckGraphWalkerImpl().ack

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L825)

```python
def ack(have_ref):
```

### MultiAckGraphWalkerImpl().handle_done

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L852)

```python
def handle_done(done_required, done_received):
```

### MultiAckGraphWalkerImpl().next

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L833)

```python
def next():
```

## PackHandler

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L233)

```python
class PackHandler(Handler):
    def __init__(backend, proto, stateless_rpc=None):
```

Protocol handler for packs.

#### See also

- [Handler](#handler)

### PackHandler.capabilities

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L247)

```python
@classmethod
def capabilities() -> Iterable[bytes]:
```

### PackHandler.capability_line

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L242)

```python
@classmethod
def capability_line(capabilities):
```

### PackHandler().has_capability

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L285)

```python
def has_capability(cap: bytes) -> bool:
```

### PackHandler.innocuous_capabilities

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L251)

```python
@classmethod
def innocuous_capabilities() -> Iterable[bytes]:
```

### PackHandler().notify_done

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L293)

```python
def notify_done() -> None:
```

### PackHandler.required_capabilities

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L261)

```python
@classmethod
def required_capabilities() -> Iterable[bytes]:
```

Return a list of capabilities that we require the client to have.

### PackHandler().set_client_capabilities

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L266)

```python
def set_client_capabilities(caps: Iterable[bytes]) -> None:
```

## ReceivePackHandler

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L941)

```python
class ReceivePackHandler(PackHandler):
    def __init__(
        backend,
        args,
        proto,
        stateless_rpc=None,
        advertise_refs=False,
    ):
```

Protocol handler for downloading a pack from the client.

#### See also

- [PackHandler](#packhandler)

### ReceivePackHandler.capabilities

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L953)

```python
@classmethod
def capabilities() -> Iterable[bytes]:
```

### ReceivePackHandler().handle

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L1066)

```python
def handle() -> None:
```

## SingleAckGraphWalkerImpl

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L773)

```python
class SingleAckGraphWalkerImpl(object):
    def __init__(walker):
```

Graph walker implementation that speaks the single-ack protocol.

### SingleAckGraphWalkerImpl().ack

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L780)

```python
def ack(have_ref):
```

### SingleAckGraphWalkerImpl().handle_done

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L796)

```python
def handle_done(done_required, done_received):
```

### SingleAckGraphWalkerImpl().next

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L785)

```python
def next():
```

## TCPGitRequestHandler

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L1167)

```python
class TCPGitRequestHandler(socketserver.StreamRequestHandler):
    def __init__(handlers, *args, **kwargs):
```

### TCPGitRequestHandler().handle

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L1172)

```python
def handle():
```

## TCPGitServer

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L1184)

```python
class TCPGitServer(socketserver.TCPServer):
    def __init__(backend, listen_addr, port=TCP_GIT_PORT, handlers=None):
```

#### See also

- [TCP_GIT_PORT](protocol.md#tcp_git_port)

### TCPGitServer().handle_error

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L1208)

```python
def handle_error(request, client_address):
```

### TCPGitServer().verify_request

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L1204)

```python
def verify_request(request, client_address):
```

## UploadArchiveHandler

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L1117)

```python
class UploadArchiveHandler(Handler):
    def __init__(backend, args, proto, stateless_rpc=None):
```

#### See also

- [Handler](#handler)

### UploadArchiveHandler().handle

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L1124)

```python
def handle():
```

## UploadPackHandler

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L297)

```python
class UploadPackHandler(PackHandler):
    def __init__(
        backend,
        args,
        proto,
        stateless_rpc=None,
        advertise_refs=False,
    ):
```

Protocol handler for uploading a pack to the client.

#### See also

- [PackHandler](#packhandler)

### UploadPackHandler.capabilities

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L314)

```python
@classmethod
def capabilities():
```

### UploadPackHandler().get_tagged

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L344)

```python
def get_tagged(refs=None, repo=None):
```

Get a dict of peeled values of tags to their original tag shas.

#### Arguments

  - `refs` - dict of refname -> sha of possible tags; defaults to all
    of the backend's refs.
  - `repo` - optional Repo instance for getting peeled refs; defaults
    to the backend's repo, if available
- `Returns` - dict of peeled_sha -> tag_sha, where tag_sha is the sha of a
    tag whose peeled value is peeled_sha.

### UploadPackHandler().handle

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L376)

```python
def handle():
```

### UploadPackHandler().progress

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L336)

```python
def progress(message):
```

### UploadPackHandler.required_capabilities

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L328)

```python
@classmethod
def required_capabilities():
```

## generate_info_refs

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L1278)

```python
def generate_info_refs(repo):
```

Generate an info refs file.

## generate_objects_info_packs

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L1284)

```python
def generate_objects_info_packs(repo):
```

Generate an index for for packs.

## main

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L1215)

```python
def main(argv=sys.argv):
```

Entry point for starting a TCP git server.

## serve_command

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L1248)

```python
def serve_command(
    handler_cls,
    argv=sys.argv,
    backend=None,
    inf=sys.stdin,
    outf=sys.stdout,
):
```

Serve a single command.

This is mostly useful for the implementation of commands used by e.g.
git+ssh.

#### Arguments

  - `handler_cls` - [Handler](#handler) class to use for the request
  - `argv` - execv-style command-line arguments. Defaults to sys.argv.
  - `backend` - [Backend](#backend) to use
  - `inf` - File-like object to read from, defaults to standard input.
  - `outf` - File-like object to write to, defaults to standard output.
- `Returns` - Exit code for use with sys.exit. 0 on success, 1 on failure.

## update_server_info

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/server.py#L1290)

```python
def update_server_info(repo):
```

Generate server info for dumb file access.

This generates info/refs and objects/info/packs,
similar to "git update-server-info".
