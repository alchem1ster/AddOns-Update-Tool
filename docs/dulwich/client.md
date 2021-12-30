# Client

> Auto-generated documentation for [dulwich.client](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py) module.

Client side support for the Git protocol.

- [Addons-update-tool](../README.md#addons-update-tool) / [Modules](../MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / Client
    - [AbstractHttpGitClient](#abstracthttpgitclient)
        - [AbstractHttpGitClient().fetch_pack](#abstracthttpgitclientfetch_pack)
        - [AbstractHttpGitClient.from_parsedurl](#abstracthttpgitclientfrom_parsedurl)
        - [AbstractHttpGitClient().get_refs](#abstracthttpgitclientget_refs)
        - [AbstractHttpGitClient().get_url](#abstracthttpgitclientget_url)
        - [AbstractHttpGitClient().send_pack](#abstracthttpgitclientsend_pack)
    - [FetchPackResult](#fetchpackresult)
    - [GitClient](#gitclient)
        - [GitClient().fetch](#gitclientfetch)
        - [GitClient().fetch_pack](#gitclientfetch_pack)
        - [GitClient.from_parsedurl](#gitclientfrom_parsedurl)
        - [GitClient().get_refs](#gitclientget_refs)
        - [GitClient().get_url](#gitclientget_url)
        - [GitClient().send_pack](#gitclientsend_pack)
    - [HTTPProxyUnauthorized](#httpproxyunauthorized)
    - [HTTPUnauthorized](#httpunauthorized)
    - [InvalidWants](#invalidwants)
    - [LocalGitClient](#localgitclient)
        - [LocalGitClient().fetch](#localgitclientfetch)
        - [LocalGitClient().fetch_pack](#localgitclientfetch_pack)
        - [LocalGitClient.from_parsedurl](#localgitclientfrom_parsedurl)
        - [LocalGitClient().get_refs](#localgitclientget_refs)
        - [LocalGitClient().get_url](#localgitclientget_url)
        - [LocalGitClient().send_pack](#localgitclientsend_pack)
    - [PLinkSSHVendor](#plinksshvendor)
        - [PLinkSSHVendor().run_command](#plinksshvendorrun_command)
    - [ReportStatusParser](#reportstatusparser)
        - [ReportStatusParser().check](#reportstatusparsercheck)
        - [ReportStatusParser().handle_packet](#reportstatusparserhandle_packet)
    - [SSHGitClient](#sshgitclient)
        - [SSHGitClient.from_parsedurl](#sshgitclientfrom_parsedurl)
        - [SSHGitClient().get_url](#sshgitclientget_url)
    - [SSHVendor](#sshvendor)
        - [SSHVendor().connect_ssh](#sshvendorconnect_ssh)
        - [SSHVendor().run_command](#sshvendorrun_command)
    - [SendPackResult](#sendpackresult)
    - [StrangeHostname](#strangehostname)
    - [SubprocessGitClient](#subprocessgitclient)
        - [SubprocessGitClient.from_parsedurl](#subprocessgitclientfrom_parsedurl)
    - [SubprocessSSHVendor](#subprocesssshvendor)
        - [SubprocessSSHVendor().run_command](#subprocesssshvendorrun_command)
    - [SubprocessWrapper](#subprocesswrapper)
        - [SubprocessWrapper().can_read](#subprocesswrappercan_read)
        - [SubprocessWrapper().close](#subprocesswrapperclose)
        - [SubprocessWrapper().stderr](#subprocesswrapperstderr)
    - [TCPGitClient](#tcpgitclient)
        - [TCPGitClient.from_parsedurl](#tcpgitclientfrom_parsedurl)
        - [TCPGitClient().get_url](#tcpgitclientget_url)
    - [TraditionalGitClient](#traditionalgitclient)
        - [TraditionalGitClient().archive](#traditionalgitclientarchive)
        - [TraditionalGitClient().fetch_pack](#traditionalgitclientfetch_pack)
        - [TraditionalGitClient().get_refs](#traditionalgitclientget_refs)
        - [TraditionalGitClient().send_pack](#traditionalgitclientsend_pack)
    - [Urllib3HttpGitClient](#urllib3httpgitclient)
    - [ParamikoSSHVendor](#paramikosshvendor)
    - [check_wants](#check_wants)
    - [default_urllib3_manager](#default_urllib3_manager)
    - [default_user_agent_string](#default_user_agent_string)
    - [find_git_command](#find_git_command)
    - [get_credentials_from_store](#get_credentials_from_store)
    - [get_transport_and_path](#get_transport_and_path)
    - [get_transport_and_path_from_url](#get_transport_and_path_from_url)
    - [parse_rsync_url](#parse_rsync_url)
    - [read_pkt_refs](#read_pkt_refs)

The Dulwich client supports the following capabilities:

* thin-pack
* multi_ack_detailed
* multi_ack
* side-band-64k
* ofs-delta
* quiet
* report-status
* delete-refs
* shallow

Known capabilities that are not supported:

* no-progress
* include-tag

#### Attributes

- `default_local_git_client_cls` - What Git client to use for local access: `LocalGitClient`
- `get_ssh_vendor` - Can be overridden by users: `SubprocessSSHVendor`

## AbstractHttpGitClient

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1799)

```python
class AbstractHttpGitClient(GitClient):
    def __init__(base_url, dumb=False, **kwargs):
```

Abstract base class for HTTP Git Clients.

This is agonistic of the actual HTTP implementation.

Subclasses should provide an implementation of the
_http_request method.

#### See also

- [GitClient](#gitclient)

### AbstractHttpGitClient().fetch_pack

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1954)

```python
def fetch_pack(
    path,
    determine_wants,
    graph_walker,
    pack_data,
    progress=None,
    depth=None,
):
```

Retrieve a pack from a git smart server.

#### Arguments

- `path` - Path to fetch from
- `determine_wants` - Callback that returns list of commits to fetch
- `graph_walker` - Object with next() and ack().
- `pack_data` - Callback called for each bit of data in the pack
- `progress` - Callback for progress reports (strings)
- `depth` - Depth for request

#### Returns

FetchPackResult object

### AbstractHttpGitClient.from_parsedurl

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L2036)

```python
@classmethod
def from_parsedurl(parsedurl, **kwargs):
```

### AbstractHttpGitClient().get_refs

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L2024)

```python
def get_refs(path):
```

Retrieve the current refs from a git smart server.

### AbstractHttpGitClient().get_url

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L2030)

```python
def get_url(path):
```

### AbstractHttpGitClient().send_pack

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1890)

```python
def send_pack(path, update_refs, generate_pack_data, progress=None):
```

Upload a pack to a remote repository.

#### Arguments

- `path` - Repository path (as bytestring)
- `update_refs` - Function to determine changes to remote refs.
  Receives dict with existing remote refs, returns dict with
  changed refs (name -> sha, where sha=ZERO_SHA for deletions)
- `generate_pack_data` - Function that can return a tuple
  with number of elements and pack data to upload.
- `progress` - Optional progress function

#### Returns

SendPackResult

#### Raises

- `SendPackError` - if server rejects the pack data

## FetchPackResult

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L248)

```python
class FetchPackResult(object):
    def __init__(refs, symrefs, agent, new_shallow=None, new_unshallow=None):
```

Result of a fetch-pack operation.

#### Attributes

- `refs` - Dictionary with all remote refs
- `symrefs` - Dictionary with remote symrefs
- `agent` - User agent string

## GitClient

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L421)

```python
class GitClient(object):
    def __init__(
        thin_packs=True,
        report_activity=None,
        quiet=False,
        include_tags=False,
    ):
```

Git smart server client.

### GitClient().fetch

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L498)

```python
def fetch(path, target, determine_wants=None, progress=None, depth=None):
```

Fetch into a target repository.

#### Arguments

- `path` - Path to fetch from (as bytestring)
- `target` - Target repository to fetch into
- `determine_wants` - Optional function to determine what refs to fetch.
  Receives dictionary of name->sha, should return
  list of shas to fetch. Defaults to all shas.
- `progress` - Optional progress function
- `depth` - Depth to fetch at

#### Returns

Dictionary with all remote refs (not just those fetched)

### GitClient().fetch_pack

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L548)

```python
def fetch_pack(
    path,
    determine_wants,
    graph_walker,
    pack_data,
    progress=None,
    depth=None,
):
```

Retrieve a pack from a git smart server.

#### Arguments

- `path` - Remote path to fetch from
- `determine_wants` - Function determine what refs
  to fetch. Receives dictionary of name->sha, should return
  list of shas to fetch.
- `graph_walker` - Object with next() and ack().
- `pack_data` - Callback called for each bit of data in the pack
- `progress` - Callback for progress reports (strings)
- `depth` - Shallow fetch depth

#### Returns

FetchPackResult object

### GitClient.from_parsedurl

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L465)

```python
@classmethod
def from_parsedurl(parsedurl, **kwargs):
```

Create an instance of this client from a urlparse.parsed object.

#### Arguments

- `parsedurl` - Result of urlparse()

#### Returns

A [GitClient](#gitclient) object

### GitClient().get_refs

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L575)

```python
def get_refs(path):
```

Retrieve the current refs from a git smart server.

#### Arguments

- `path` - Path to the repo to fetch from. (as bytestring)

### GitClient().get_url

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L453)

```python
def get_url(path):
```

Retrieves full url to given path.

#### Arguments

- `path` - Repository path (as string)

#### Returns

Url to path (as string)

### GitClient().send_pack

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L477)

```python
def send_pack(path, update_refs, generate_pack_data, progress=None):
```

Upload a pack to a remote repository.

#### Arguments

- `path` - Repository path (as bytestring)
- `update_refs` - Function to determine changes to remote refs. Receive
  dict with existing remote refs, returns dict with
  changed refs (name -> sha, where sha=ZERO_SHA for deletions)
- `generate_pack_data` - Function that can return a tuple
  with number of objects and list of pack data to include
- `progress` - Optional progress function

#### Returns

SendPackResult object

#### Raises

- `SendPackError` - if server rejects the pack data

## HTTPProxyUnauthorized

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L137)

```python
class HTTPProxyUnauthorized(Exception):
    def __init__(proxy_authenticate, url):
```

Raised when proxy authentication fails.

## HTTPUnauthorized

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L128)

```python
class HTTPUnauthorized(Exception):
    def __init__(www_authenticate, url):
```

Raised when authentication fails.

## InvalidWants

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L119)

```python
class InvalidWants(Exception):
    def __init__(wants):
```

Invalid wants.

## LocalGitClient

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1270)

```python
class LocalGitClient(GitClient):
    def __init__(thin_packs=True, report_activity=None, config=None):
```

Git Client that just uses a local Repo.

#### See also

- [GitClient](#gitclient)

### LocalGitClient().fetch

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1359)

```python
def fetch(path, target, determine_wants=None, progress=None, depth=None):
```

Fetch into a target repository.

#### Arguments

- `path` - Path to fetch from (as bytestring)
- `target` - Target repository to fetch into
- `determine_wants` - Optional function determine what refs
  to fetch. Receives dictionary of name->sha, should return
  list of shas to fetch. Defaults to all shas.
- `progress` - Optional progress function
- `depth` - Shallow fetch depth

#### Returns

FetchPackResult object

### LocalGitClient().fetch_pack

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1384)

```python
def fetch_pack(
    path,
    determine_wants,
    graph_walker,
    pack_data,
    progress=None,
    depth=None,
):
```

Retrieve a pack from a git smart server.

#### Arguments

- `path` - Remote path to fetch from
- `determine_wants` - Function determine what refs
  to fetch. Receives dictionary of name->sha, should return
  list of shas to fetch.
- `graph_walker` - Object with next() and ack().
- `pack_data` - Callback called for each bit of data in the pack
- `progress` - Callback for progress reports (strings)
- `depth` - Shallow fetch depth

#### Returns

FetchPackResult object

### LocalGitClient.from_parsedurl

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1287)

```python
@classmethod
def from_parsedurl(parsedurl, **kwargs):
```

### LocalGitClient().get_refs

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1424)

```python
def get_refs(path):
```

Retrieve the current refs from a git smart server.

### LocalGitClient().get_url

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1284)

```python
def get_url(path):
```

### LocalGitClient().send_pack

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1299)

```python
def send_pack(path, update_refs, generate_pack_data, progress=None):
```

Upload a pack to a remote repository.

#### Arguments

- `path` - Repository path (as bytestring)
- `update_refs` - Function to determine changes to remote refs.
  Receive dict with existing remote refs, returns dict with
  changed refs (name -> sha, where sha=ZERO_SHA for deletions)
  with number of items and pack data to upload.
- `progress` - Optional progress function

#### Returns

SendPackResult

#### Raises

- `SendPackError` - if server rejects the pack data

## PLinkSSHVendor

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1546)

```python
class PLinkSSHVendor(SSHVendor):
```

SSH vendor that shells out to the local 'plink' command.

#### See also

- [SSHVendor](#sshvendor)

### PLinkSSHVendor().run_command

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1549)

```python
def run_command(
    host,
    command,
    username=None,
    port=None,
    password=None,
    key_filename=None,
    ssh_command=None,
):
```

## ReportStatusParser

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L178)

```python
class ReportStatusParser(object):
    def __init__():
```

Handle status as reported by servers with 'report-status' capability.

### ReportStatusParser().check

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L186)

```python
def check():
```

Check if there were any errors and, if so, raise exceptions.

#### Raises

- `SendPackError` - Raised when the server could not unpack

#### Returns

iterator over refs

### ReportStatusParser().handle_packet

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L210)

```python
def handle_packet(pkt):
```

Handle a packet.

#### Raises

- `GitProtocolError` - Raised when packets are received after a flush
packet.

## SSHGitClient

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1614)

```python
class SSHGitClient(TraditionalGitClient):
    def __init__(
        host,
        port=None,
        username=None,
        vendor=None,
        config=None,
        password=None,
        key_filename=None,
        ssh_command=None,
        **kwargs,
    ):
```

#### See also

- [TraditionalGitClient](#traditionalgitclient)

### SSHGitClient.from_parsedurl

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1652)

```python
@classmethod
def from_parsedurl(parsedurl, **kwargs):
```

### SSHGitClient().get_url

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1642)

```python
def get_url(path):
```

## SSHVendor

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1435)

```python
class SSHVendor(object):
```

A client side SSH implementation.

### SSHVendor().connect_ssh

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1438)

```python
def connect_ssh(
    host,
    command,
    username=None,
    port=None,
    password=None,
    key_filename=None,
):
```

### SSHVendor().run_command

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1463)

```python
def run_command(
    host,
    command,
    username=None,
    port=None,
    password=None,
    key_filename=None,
    ssh_command=None,
):
```

Connect to an SSH server.

Run a command remotely and return a file-like object for interaction
with the remote command.

#### Arguments

- `host` - Host name
- `command` - Command to run (as argv array)
- `username` - Optional ame of user to log in as
- `port` - Optional SSH port to use
- `password` - Optional ssh password for login or private key
- `key_filename` - Optional path to private keyfile
- `ssh_command` - Optional SSH command

## SendPackResult

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L331)

```python
class SendPackResult(object):
    def __init__(refs, agent=None, ref_status=None):
```

Result of a upload-pack operation.

#### Attributes

- `refs` - Dictionary with all remote refs
- `agent` - User agent string
- `ref_status` - Optional dictionary mapping ref name to error message (if it
  failed to update), or None if it was updated successfully

## StrangeHostname

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1493)

```python
class StrangeHostname(Exception):
    def __init__(hostname):
```

Refusing to connect to strange SSH hostname.

## SubprocessGitClient

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1233)

```python
class SubprocessGitClient(TraditionalGitClient):
```

Git client that talks to a server using a subprocess.

#### See also

- [TraditionalGitClient](#traditionalgitclient)

### SubprocessGitClient.from_parsedurl

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1236)

```python
@classmethod
def from_parsedurl(parsedurl, **kwargs):
```

## SubprocessSSHVendor

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1500)

```python
class SubprocessSSHVendor(SSHVendor):
```

SSH vendor that shells out to the local 'ssh' command.

#### See also

- [SSHVendor](#sshvendor)

### SubprocessSSHVendor().run_command

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1503)

```python
def run_command(
    host,
    command,
    username=None,
    port=None,
    password=None,
    key_filename=None,
    ssh_command=None,
):
```

## SubprocessWrapper

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1190)

```python
class SubprocessWrapper(object):
    def __init__(proc):
```

A socket-like object that talks to a subprocess via pipes.

### SubprocessWrapper().can_read

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1202)

```python
def can_read():
```

### SubprocessWrapper().close

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1211)

```python
def close():
```

### SubprocessWrapper().stderr

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1198)

```python
@property
def stderr():
```

## TCPGitClient

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1124)

```python
class TCPGitClient(TraditionalGitClient):
    def __init__(host, port=None, **kwargs):
```

A Git Client that works over TCP directly (i.e. git://).

#### See also

- [TraditionalGitClient](#traditionalgitclient)

### TCPGitClient.from_parsedurl

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1134)

```python
@classmethod
def from_parsedurl(parsedurl, **kwargs):
```

### TCPGitClient().get_url

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1138)

```python
def get_url(path):
```

## TraditionalGitClient

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L884)

```python
class TraditionalGitClient(GitClient):
    def __init__(path_encoding=DEFAULT_ENCODING, **kwargs):
```

Traditional Git client.

#### See also

- [GitClient](#gitclient)

### TraditionalGitClient().archive

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1077)

```python
def archive(
    path,
    committish,
    write_data,
    progress=None,
    write_error=None,
    format=None,
    subdirs=None,
    prefix=None,
):
```

### TraditionalGitClient().fetch_pack

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L994)

```python
def fetch_pack(
    path,
    determine_wants,
    graph_walker,
    pack_data,
    progress=None,
    depth=None,
):
```

Retrieve a pack from a git smart server.

#### Arguments

- `path` - Remote path to fetch from
- `determine_wants` - Function determine what refs
  to fetch. Receives dictionary of name->sha, should return
  list of shas to fetch.
- `graph_walker` - Object with next() and ack().
- `pack_data` - Callback called for each bit of data in the pack
- `progress` - Callback for progress reports (strings)
- `depth` - Shallow fetch depth

#### Returns

FetchPackResult object

### TraditionalGitClient().get_refs

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1065)

```python
def get_refs(path):
```

Retrieve the current refs from a git smart server.

### TraditionalGitClient().send_pack

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L908)

```python
def send_pack(path, update_refs, generate_pack_data, progress=None):
```

Upload a pack to a remote repository.

#### Arguments

- `path` - Repository path (as bytestring)
- `update_refs` - Function to determine changes to remote refs.
  Receive dict with existing remote refs, returns dict with
  changed refs (name -> sha, where sha=ZERO_SHA for deletions)
- `generate_pack_data` - Function that can return a tuple with
  number of objects and pack data to upload.
- `progress` - Optional callback called with progress updates

#### Returns

SendPackResult

#### Raises

- `SendPackError` - if server rejects the pack data

## Urllib3HttpGitClient

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L2060)

```python
class Urllib3HttpGitClient(AbstractHttpGitClient):
    def __init__(
        base_url,
        dumb=None,
        pool_manager=None,
        config=None,
        username=None,
        password=None,
        **kwargs,
    ):
```

#### See also

- [AbstractHttpGitClient](#abstracthttpgitclient)

## ParamikoSSHVendor

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1598)

```python
def ParamikoSSHVendor(**kwargs):
```

## check_wants

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L857)

```python
def check_wants(wants, refs):
```

Check that a set of wants is valid.

#### Arguments

- `wants` - Set of object SHAs to fetch
- `refs` - Refs dictionary to check against

## default_urllib3_manager

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1708)

```python
def default_urllib3_manager(
    config,
    pool_manager_cls=None,
    proxy_manager_cls=None,
    **override_kwargs,
):
```

Return `urllib3` connection pool manager.

Honour detected proxy configurations.

#### Arguments

- `config` - dulwich.config.ConfigDict` instance with Git configuration.
- `kwargs` - Additional arguments for urllib3.ProxyManager

#### Returns

`pool_manager_cls` (defaults to `urllib3.ProxyManager`) instance for
proxy configurations, `proxy_manager_cls` (defaults to
`urllib3.PoolManager`) instance otherwise.

## default_user_agent_string

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1702)

```python
def default_user_agent_string():
```

## find_git_command

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L1219)

```python
def find_git_command():
```

Find command to run for system Git (usually C Git).

## get_credentials_from_store

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L2240)

```python
def get_credentials_from_store(
    scheme,
    hostname,
    username=None,
    fnames=DEFAULT_GIT_CREDENTIALS_PATHS,
):
```

#### See also

- [DEFAULT_GIT_CREDENTIALS_PATHS](#default_git_credentials_paths)

## get_transport_and_path

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L2201)

```python
def get_transport_and_path(location, **kwargs):
```

Obtain a git client from a URL.

#### Arguments

- `location` - URL or path (a string)
- `config` - Optional config object
- `thin_packs` - Whether or not thin packs should be retrieved
- `report_activity` - Optional callback for reporting transport
  activity.

#### Returns

Tuple with client instance and relative path.

## get_transport_and_path_from_url

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L2149)

```python
def get_transport_and_path_from_url(url, config=None, **kwargs):
```

Obtain a git client from a URL.

#### Arguments

- `url` - URL to open (a unicode string)
- `config` - Optional config object
- `thin_packs` - Whether or not thin packs should be retrieved
- `report_activity` - Optional callback for reporting transport
  activity.

#### Returns

Tuple with client instance and relative path.

## parse_rsync_url

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L2182)

```python
def parse_rsync_url(location):
```

Parse a rsync-style URL.

## read_pkt_refs

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/client.py#L229)

```python
def read_pkt_refs(proto):
```