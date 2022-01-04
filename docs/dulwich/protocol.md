# Protocol

> Auto-generated documentation for [dulwich.protocol](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py) module.

Generic functions for talking the git smart server protocol.

- [AddOns-Update-Tool](../README.md#addons-update-tool-index) / [Modules](../MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / Protocol
    - [BufferedPktLineWriter](#bufferedpktlinewriter)
        - [BufferedPktLineWriter().flush](#bufferedpktlinewriterflush)
        - [BufferedPktLineWriter().write](#bufferedpktlinewriterwrite)
    - [PktLineParser](#pktlineparser)
        - [PktLineParser().get_tail](#pktlineparserget_tail)
        - [PktLineParser().parse](#pktlineparserparse)
    - [Protocol](#protocol)
        - [Protocol().close](#protocolclose)
        - [Protocol().eof](#protocoleof)
        - [Protocol().read_cmd](#protocolread_cmd)
        - [Protocol().read_pkt_line](#protocolread_pkt_line)
        - [Protocol().read_pkt_seq](#protocolread_pkt_seq)
        - [Protocol().send_cmd](#protocolsend_cmd)
        - [Protocol().unread_pkt_line](#protocolunread_pkt_line)
        - [Protocol().write_file](#protocolwrite_file)
        - [Protocol().write_pkt_line](#protocolwrite_pkt_line)
        - [Protocol().write_sideband](#protocolwrite_sideband)
    - [ProtocolFile](#protocolfile)
        - [ProtocolFile().close](#protocolfileclose)
        - [ProtocolFile().tell](#protocolfiletell)
    - [ReceivableProtocol](#receivableprotocol)
        - [ReceivableProtocol().read](#receivableprotocolread)
        - [ReceivableProtocol().recv](#receivableprotocolrecv)
    - [ack_type](#ack_type)
    - [agent_string](#agent_string)
    - [capability_agent](#capability_agent)
    - [capability_symref](#capability_symref)
    - [extract_capabilities](#extract_capabilities)
    - [extract_capability_names](#extract_capability_names)
    - [extract_want_line_capabilities](#extract_want_line_capabilities)
    - [format_cmd_pkt](#format_cmd_pkt)
    - [parse_capability](#parse_capability)
    - [parse_cmd_pkt](#parse_cmd_pkt)
    - [pkt_line](#pkt_line)
    - [symref_capabilities](#symref_capabilities)

#### Attributes

- `SIDE_BAND_CHANNEL_DATA` - pack data: `1`
- `SIDE_BAND_CHANNEL_PROGRESS` - progress messages: `2`
- `SIDE_BAND_CHANNEL_FATAL` - fatal error message just before stream aborts: `3`
- `CAPABILITIES_REF` - Magic ref that is used to attach capabilities to when
  there are no refs. Should always be ste to ZERO_SHA.: `b'capabilities^{}'`

## BufferedPktLineWriter

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L513)

```python
class BufferedPktLineWriter(object):
    def __init__(write, bufsize=65515):
```

Writer that wraps its data in pkt-lines and has an independent buffer.

Consecutive calls to write() wrap the data in a pkt-line and then buffers
it until enough lines have been written such that their total length
(including length prefix) reach the buffer size.

### BufferedPktLineWriter().flush

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L548)

```python
def flush():
```

Flush all data from the buffer.

### BufferedPktLineWriter().write

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L533)

```python
def write(data):
```

Write data, wrapping it in a pkt-line.

## PktLineParser

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L557)

```python
class PktLineParser(object):
    def __init__(handle_pkt):
```

Packet line parser that hands completed packets off to a callback.

### PktLineParser().get_tail

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L583)

```python
def get_tail():
```

Read back any unused data.

### PktLineParser().parse

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L564)

```python
def parse(data):
```

Parse a fragment of data and call back for any completed packets.

## Protocol

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L186)

```python
class Protocol(object):
    def __init__(read, write, close=None, report_activity=None):
```

Class for interacting with a remote git process over the wire.

Parts of the git wire protocol use 'pkt-lines' to communicate. A pkt-line
consists of the length of the line as a 4-byte hex string, followed by the
payload data. The length includes the 4-byte header. The special line
'0000' indicates the end of a section of input and is called a 'flush-pkt'.

For details on the pkt-line format, see the cgit distribution:
    Documentation/technical/protocol-common.txt

### Protocol().close

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L205)

```python
def close():
```

### Protocol().eof

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L251)

```python
def eof():
```

Test whether the protocol stream has reached EOF.

Note that this refers to the actual stream EOF and not just a
flush-pkt.

Returns: True if the stream is at EOF, False otherwise.

### Protocol().read_cmd

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L352)

```python
def read_cmd():
```

Read a command and some arguments from the git client

Only used for the TCP git protocol (git://).

Returns: A tuple of (command, [list of arguments]).

### Protocol().read_pkt_line

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L215)

```python
def read_pkt_line():
```

Reads a pkt-line from the remote git process.

This method may read from the readahead buffer; see unread_pkt_line.

Returns: The next string from the stream, without the length prefix, or
    None for a flush-pkt ('0000').

### Protocol().read_pkt_seq

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L281)

```python
def read_pkt_seq():
```

Read a sequence of pkt-lines from the remote git process.

Returns: Yields each line of data up to but not including the next
    flush-pkt.

### Protocol().send_cmd

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L341)

```python
def send_cmd(cmd, *args):
```

Send a command and some arguments to a git server.

Only used for the TCP git protocol (git://).

#### Arguments

- `cmd` - The remote service to access.
- `args` - List of arguments to send to remove service.

### Protocol().unread_pkt_line

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L266)

```python
def unread_pkt_line(data):
```

Unread a single line of data into the readahead buffer.

This method can be used to unread a single pkt-line into a fixed
readahead buffer.

#### Arguments

- `data` - The data to unread, without the length prefix.

#### Raises

- `ValueError` - If more than one pkt-line is unread.

### Protocol().write_file

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L307)

```python
def write_file():
```

Return a writable file-like object for this protocol.

### Protocol().write_pkt_line

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L292)

```python
def write_pkt_line(line):
```

Sends a pkt-line to the remote git process.

#### Arguments

- `line` - A string containing the data to send, without the length
  prefix.

### Protocol().write_sideband

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L327)

```python
def write_sideband(channel, blob):
```

Write multiplexed data to the sideband.

#### Arguments

- `channel` - An int specifying the channel to write to.
- `blob` - A blob of data (as a string) to send on this channel.

## ProtocolFile

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L148)

```python
class ProtocolFile(object):
    def __init__(read, write):
```

A dummy file for network ops that expect file-like objects.

### ProtocolFile().close

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L158)

```python
def close():
```

### ProtocolFile().tell

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L155)

```python
def tell():
```

## ReceivableProtocol

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L366)

```python
class ReceivableProtocol(Protocol):
    def __init__(
        recv,
        write,
        close=None,
        report_activity=None,
        rbufsize=_RBUFSIZE,
    ):
```

Variant of Protocol that allows reading up to a size without blocking.

This class has a recv() method that behaves like socket.recv() in addition
to a read() method.

If you want to read n bytes from the wire and block until exactly n bytes
(or EOF) are read, use read(n). If you want to read at most n bytes from
the wire but don't care if you get less, use recv(n). Note that recv(n)
will still block until at least one byte is read.

#### See also

- [Protocol](#protocol)

### ReceivableProtocol().read

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L388)

```python
def read(size):
```

### ReceivableProtocol().recv

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L449)

```python
def recv(size):
```

## ack_type

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L504)

```python
def ack_type(capabilities):
```

Extract the ack type from a capabilities list.

## agent_string

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L113)

```python
def agent_string():
```

## capability_agent

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L117)

```python
def capability_agent():
```

## capability_symref

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L121)

```python
def capability_symref(from_ref, to_ref):
```

## extract_capabilities

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L473)

```python
def extract_capabilities(text):
```

Extract a capabilities list from a string, if present.

#### Arguments

  - `text` - String to extract from
- `Returns` - Tuple with text with capabilities removed and list of capabilities

## extract_capability_names

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L125)

```python
def extract_capability_names(capabilities):
```

## extract_want_line_capabilities

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L486)

```python
def extract_want_line_capabilities(text):
```

Extract a capabilities list from a want line, if present.

Note that want lines have capabilities separated from the rest of the line
by a space instead of a null byte. Thus want lines have the form:

want obj-id cap1 cap2 ...

#### Arguments

  - `text` - Want line to extract from
- `Returns` - Tuple with text with capabilities removed and list of capabilities

## format_cmd_pkt

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L162)

```python
def format_cmd_pkt(cmd, *args):
```

## parse_capability

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L129)

```python
def parse_capability(capability):
```

## parse_cmd_pkt

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L166)

```python
def parse_cmd_pkt(line):
```

## pkt_line

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L173)

```python
def pkt_line(data):
```

Wrap data in a pkt-line.

#### Arguments

  - `data` - The data to wrap, as a str or None.
- `Returns` - The data prefixed with its length in pkt-line format; if data was
    None, returns the flush-pkt ('0000').

## symref_capabilities

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/protocol.py#L136)

```python
def symref_capabilities(symrefs):
```
