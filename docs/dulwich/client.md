# Client

> Auto-generated documentation for [dulwich.client](../../dulwich/client.py) module.

Client side support for the Git protocol.

- [AddOns-Update-Tool](../README.md#addons-update-tool-index) / [Modules](../MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / Client
    - [AbstractHttpGitClient](#abstracthttpgitclient)
        - [AbstractHttpGitClient().fetch_pack](#abstracthttpgitclientfetch_pack)
        - [AbstractHttpGitClient.from_parsedurl](#abstracthttpgitclientfrom_parsedurl)
        - [AbstractHttpGitClient().get_refs](#abstracthttpgitclientget_refs)
        - [AbstractHttpGitClient().get_url](#abstracthttpgitclientget_url)
        - [AbstractHttpGitClient().send_pack](#abstracthttpgitclientsend_pack)
    - [FetchPackResult](#fetchpackresult)
    - [GitClient](#gitclient)
        - [GitClient().clone](#gitclientclone)
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

[[find in source code]](../../dulwich/client.py#L1925)

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

[[find in source code]](../../dulwich/client.py#L2084)

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

[[find in source code]](../../dulwich/client.py#L2170)

```python
@classmethod
def from_parsedurl(parsedurl, **kwargs):
```

### AbstractHttpGitClient().get_refs

[[find in source code]](../../dulwich/client.py#L2158)

```python
def get_refs(path):
```

Retrieve the current refs from a git smart server.

### AbstractHttpGitClient().get_url

[[find in source code]](../../dulwich/client.py#L2164)

```python
def get_url(path):
```

### AbstractHttpGitClient().send_pack

[[find in source code]](../../dulwich/client.py#L2020)

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

[[find in source code]](../../dulwich/client.py#L249)

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

[[find in source code]](../../dulwich/client.py#L424)

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

### GitClient().clone

[[find in source code]](../../dulwich/client.py#L501)

```python
def clone(
    path,
    target_path,
    mkdir: bool = True,
    bare=False,
    origin='origin',
    checkout=None,
    branch=None,
    progress=None,
    depth=None,
):
```

Clone a repository.

### GitClient().fetch

[[find in source code]](../../dulwich/client.py#L589)

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

[[find in source code]](../../dulwich/client.py#L641)

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

[[find in source code]](../../dulwich/client.py#L468)

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

[[find in source code]](../../dulwich/client.py#L668)

```python
def get_refs(path):
```

Retrieve the current refs from a git smart server.

#### Arguments

- `path` - Path to the repo to fetch from. (as bytestring)

### GitClient().get_url

[[find in source code]](../../dulwich/client.py#L456)

```python
def get_url(path):
```

Retrieves full url to given path.

#### Arguments

- `path` - Repository path (as string)

#### Returns

Url to path (as string)

### GitClient().send_pack

[[find in source code]](../../dulwich/client.py#L480)

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

[[find in source code]](../../dulwich/client.py#L138)

```python
class HTTPProxyUnauthorized(Exception):
    def __init__(proxy_authenticate, url):
```

Raised when proxy authentication fails.

## HTTPUnauthorized

[[find in source code]](../../dulwich/client.py#L129)

```python
class HTTPUnauthorized(Exception):
    def __init__(www_authenticate, url):
```

Raised when authentication fails.

## InvalidWants

[[find in source code]](../../dulwich/client.py#L120)

```python
class InvalidWants(Exception):
    def __init__(wants):
```

Invalid wants.

## LocalGitClient

[[find in source code]](../../dulwich/client.py#L1390)

```python
class LocalGitClient(GitClient):
    def __init__(thin_packs=True, report_activity=None, config=None):
```

Git Client that just uses a local Repo.

#### See also

- [GitClient](#gitclient)

### LocalGitClient().fetch

[[find in source code]](../../dulwich/client.py#L1483)

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

[[find in source code]](../../dulwich/client.py#L1510)

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

[[find in source code]](../../dulwich/client.py#L1407)

```python
@classmethod
def from_parsedurl(parsedurl, **kwargs):
```

### LocalGitClient().get_refs

[[find in source code]](../../dulwich/client.py#L1550)

```python
def get_refs(path):
```

Retrieve the current refs from a git smart server.

### LocalGitClient().get_url

[[find in source code]](../../dulwich/client.py#L1404)

```python
def get_url(path):
```

### LocalGitClient().send_pack

[[find in source code]](../../dulwich/client.py#L1419)

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

[[find in source code]](../../dulwich/client.py#L1672)

```python
class PLinkSSHVendor(SSHVendor):
```

SSH vendor that shells out to the local 'plink' command.

#### See also

- [SSHVendor](#sshvendor)

### PLinkSSHVendor().run_command

[[find in source code]](../../dulwich/client.py#L1675)

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

[[find in source code]](../../dulwich/client.py#L179)

```python
class ReportStatusParser(object):
    def __init__():
```

Handle status as reported by servers with 'report-status' capability.

### ReportStatusParser().check

[[find in source code]](../../dulwich/client.py#L187)

```python
def check():
```

Check if there were any errors and, if so, raise exceptions.

#### Raises

- `SendPackError` - Raised when the server could not unpack

#### Returns

iterator over refs

### ReportStatusParser().handle_packet

[[find in source code]](../../dulwich/client.py#L211)

```python
def handle_packet(pkt):
```

Handle a packet.

#### Raises

- `GitProtocolError` - Raised when packets are received after a flush
packet.

## SSHGitClient

[[find in source code]](../../dulwich/client.py#L1740)

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

[[find in source code]](../../dulwich/client.py#L1778)

```python
@classmethod
def from_parsedurl(parsedurl, **kwargs):
```

### SSHGitClient().get_url

[[find in source code]](../../dulwich/client.py#L1768)

```python
def get_url(path):
```

## SSHVendor

[[find in source code]](../../dulwich/client.py#L1561)

```python
class SSHVendor(object):
```

A client side SSH implementation.

### SSHVendor().connect_ssh

[[find in source code]](../../dulwich/client.py#L1564)

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

[[find in source code]](../../dulwich/client.py#L1589)

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

[[find in source code]](../../dulwich/client.py#L334)

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

[[find in source code]](../../dulwich/client.py#L1619)

```python
class StrangeHostname(Exception):
    def __init__(hostname):
```

Refusing to connect to strange SSH hostname.

## SubprocessGitClient

[[find in source code]](../../dulwich/client.py#L1353)

```python
class SubprocessGitClient(TraditionalGitClient):
```

Git client that talks to a server using a subprocess.

#### See also

- [TraditionalGitClient](#traditionalgitclient)

### SubprocessGitClient.from_parsedurl

[[find in source code]](../../dulwich/client.py#L1356)

```python
@classmethod
def from_parsedurl(parsedurl, **kwargs):
```

## SubprocessSSHVendor

[[find in source code]](../../dulwich/client.py#L1626)

```python
class SubprocessSSHVendor(SSHVendor):
```

SSH vendor that shells out to the local 'ssh' command.

#### See also

- [SSHVendor](#sshvendor)

### SubprocessSSHVendor().run_command

[[find in source code]](../../dulwich/client.py#L1629)

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

[[find in source code]](../../dulwich/client.py#L1310)

```python
class SubprocessWrapper(object):
    def __init__(proc):
```

A socket-like object that talks to a subprocess via pipes.

### SubprocessWrapper().can_read

[[find in source code]](../../dulwich/client.py#L1322)

```python
def can_read():
```

### SubprocessWrapper().close

[[find in source code]](../../dulwich/client.py#L1331)

```python
def close():
```

### SubprocessWrapper().stderr

[[find in source code]](../../dulwich/client.py#L1318)

```python
@property
def stderr():
```

## TCPGitClient

[[find in source code]](../../dulwich/client.py#L1242)

```python
class TCPGitClient(TraditionalGitClient):
    def __init__(host, port=None, **kwargs):
```

A Git Client that works over TCP directly (i.e. git://).

#### See also

- [TraditionalGitClient](#traditionalgitclient)

### TCPGitClient.from_parsedurl

[[find in source code]](../../dulwich/client.py#L1252)

```python
@classmethod
def from_parsedurl(parsedurl, **kwargs):
```

### TCPGitClient().get_url

[[find in source code]](../../dulwich/client.py#L1256)

```python
def get_url(path):
```

## TraditionalGitClient

[[find in source code]](../../dulwich/client.py#L994)

```python
class TraditionalGitClient(GitClient):
    def __init__(path_encoding=DEFAULT_ENCODING, **kwargs):
```

Traditional Git client.

#### See also

- [GitClient](#gitclient)

### TraditionalGitClient().archive

[[find in source code]](../../dulwich/client.py#L1193)

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

[[find in source code]](../../dulwich/client.py#L1108)

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

[[find in source code]](../../dulwich/client.py#L1181)

```python
def get_refs(path):
```

Retrieve the current refs from a git smart server.

### TraditionalGitClient().send_pack

[[find in source code]](../../dulwich/client.py#L1018)

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

[[find in source code]](../../dulwich/client.py#L2194)

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

[[find in source code]](../../dulwich/client.py#L1724)

```python
def ParamikoSSHVendor(**kwargs):
```

## check_wants

[[find in source code]](../../dulwich/client.py#L965)

```python
def check_wants(wants, refs):
```

Check that a set of wants is valid.

#### Arguments

- `wants` - Set of object SHAs to fetch
- `refs` - Refs dictionary to check against

## default_urllib3_manager

[[find in source code]](../../dulwich/client.py#L1834)

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

- `config` - [ConfigDict](config.md#configdict) instance with Git configuration.
- `override_kwargs` - Additional arguments for `urllib3.ProxyManager`

#### Returns

`pool_manager_cls` (defaults to `urllib3.ProxyManager`) instance for
proxy configurations, `proxy_manager_cls` (defaults to
`urllib3.PoolManager`) instance otherwise.

## default_user_agent_string

[[find in source code]](../../dulwich/client.py#L1828)

```python
def default_user_agent_string():
```

## find_git_command

[[find in source code]](../../dulwich/client.py#L1339)

```python
def find_git_command():
```

Find command to run for system Git (usually C Git).

## get_credentials_from_store

[[find in source code]](../../dulwich/client.py#L2384)

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

[[find in source code]](../../dulwich/client.py#L2341)

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

[[find in source code]](../../dulwich/client.py#L2289)

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

[[find in source code]](../../dulwich/client.py#L2322)

```python
def parse_rsync_url(location):
```

Parse a rsync-style URL.

## read_pkt_refs

[[find in source code]](../../dulwich/client.py#L230)

```python
def read_pkt_refs(proto):
```
