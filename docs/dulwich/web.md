# Web

> Auto-generated documentation for [dulwich.web](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py) module.

HTTP server for dulwich that implements the git smart HTTP protocol.

- [AddOns-Update-Tool](../README.md#addons-update-tool-index) / [Modules](../MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / Web
    - [GunzipFilter](#gunzipfilter)
    - [HTTPGitApplication](#httpgitapplication)
    - [HTTPGitRequest](#httpgitrequest)
        - [HTTPGitRequest().add_header](#httpgitrequestadd_header)
        - [HTTPGitRequest().cache_forever](#httpgitrequestcache_forever)
        - [HTTPGitRequest().error](#httpgitrequesterror)
        - [HTTPGitRequest().forbidden](#httpgitrequestforbidden)
        - [HTTPGitRequest().nocache](#httpgitrequestnocache)
        - [HTTPGitRequest().not_found](#httpgitrequestnot_found)
        - [HTTPGitRequest().respond](#httpgitrequestrespond)
    - [LimitedInputFilter](#limitedinputfilter)
    - [ServerHandlerLogger](#serverhandlerlogger)
        - [ServerHandlerLogger().log_error](#serverhandlerloggerlog_error)
        - [ServerHandlerLogger().log_exception](#serverhandlerloggerlog_exception)
        - [ServerHandlerLogger().log_message](#serverhandlerloggerlog_message)
    - [WSGIRequestHandlerLogger](#wsgirequesthandlerlogger)
        - [WSGIRequestHandlerLogger().handle](#wsgirequesthandlerloggerhandle)
        - [WSGIRequestHandlerLogger().log_error](#wsgirequesthandlerloggerlog_error)
        - [WSGIRequestHandlerLogger().log_exception](#wsgirequesthandlerloggerlog_exception)
        - [WSGIRequestHandlerLogger().log_message](#wsgirequesthandlerloggerlog_message)
    - [WSGIServerLogger](#wsgiserverlogger)
        - [WSGIServerLogger().handle_error](#wsgiserverloggerhandle_error)
    - [date_time_string](#date_time_string)
    - [get_idx_file](#get_idx_file)
    - [get_info_packs](#get_info_packs)
    - [get_info_refs](#get_info_refs)
    - [get_loose_object](#get_loose_object)
    - [get_pack_file](#get_pack_file)
    - [get_repo](#get_repo)
    - [get_text_file](#get_text_file)
    - [handle_service_request](#handle_service_request)
    - [main](#main)
    - [make_wsgi_chain](#make_wsgi_chain)
    - [send_file](#send_file)
    - [url_prefix](#url_prefix)

#### Attributes

- `HTTP_OK` - HTTP error strings: `'200 OK'`

## GunzipFilter

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L429)

```python
class GunzipFilter(object):
    def __init__(application):
```

WSGI middleware that unzips gzip-encoded requests before
passing on to the underlying application.

## HTTPGitApplication

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L366)

```python
class HTTPGitApplication(object):
    def __init__(
        backend,
        dumb: bool = False,
        handlers=None,
        fallback_app=None,
    ):
```

Class encapsulating the state of a git WSGI application.

:ivar backend: the Backend object backing this application

## HTTPGitRequest

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L292)

```python
class HTTPGitRequest(object):
    def __init__(environ, start_response, dumb: bool = False, handlers=None):
```

Class encapsulating the state of a single git HTTP request.

:ivar environ: the WSGI environment for the request.

### HTTPGitRequest().add_header

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L308)

```python
def add_header(name, value):
```

Add a header to the response.

### HTTPGitRequest().cache_forever

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L356)

```python
def cache_forever() -> None:
```

Set the response to be cached forever by the client.

### HTTPGitRequest().error

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L341)

```python
def error(message: str) -> bytes:
```

Begin a HTTP 500 response and return the text of a message.

### HTTPGitRequest().forbidden

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L334)

```python
def forbidden(message: str) -> bytes:
```

Begin a HTTP 403 response and return the text of a message.

### HTTPGitRequest().nocache

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L348)

```python
def nocache() -> None:
```

Set the response to never be cached by the client.

### HTTPGitRequest().not_found

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L327)

```python
def not_found(message: str) -> bytes:
```

Begin a HTTP 404 response and return the text of a message.

### HTTPGitRequest().respond

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L312)

```python
def respond(
    status: str = HTTP_OK,
    content_type: Optional[str] = None,
    headers: Optional[List[Tuple[str, str]]] = None,
):
```

Begin a response with the given status and other headers.

#### See also

- [HTTP_OK](#http_ok)

## LimitedInputFilter

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L461)

```python
class LimitedInputFilter(object):
    def __init__(application):
```

WSGI middleware that limits the input length of a request to that
specified in Content-Length.

## ServerHandlerLogger

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L491)

```python
class ServerHandlerLogger(ServerHandler):
```

ServerHandler that uses dulwich's logger for logging exceptions.

### ServerHandlerLogger().log_error

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L503)

```python
def log_error(*args):
```

### ServerHandlerLogger().log_exception

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L494)

```python
def log_exception(exc_info):
```

### ServerHandlerLogger().log_message

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L500)

```python
def log_message(format, *args):
```

## WSGIRequestHandlerLogger

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L507)

```python
class WSGIRequestHandlerLogger(WSGIRequestHandler):
```

WSGIRequestHandler that uses dulwich's logger for logging exceptions.

### WSGIRequestHandlerLogger().handle

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L522)

```python
def handle():
```

Handle a single HTTP request

### WSGIRequestHandlerLogger().log_error

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L519)

```python
def log_error(*args):
```

### WSGIRequestHandlerLogger().log_exception

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L510)

```python
def log_exception(exc_info):
```

### WSGIRequestHandlerLogger().log_message

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L516)

```python
def log_message(format, *args):
```

## WSGIServerLogger

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L536)

```python
class WSGIServerLogger(WSGIServer):
```

### WSGIServerLogger().handle_error

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L537)

```python
def handle_error(request, client_address):
```

Handle an error.

## date_time_string

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L70)

```python
def date_time_string(timestamp: Optional[float] = None) -> str:
```

## get_idx_file

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L190)

```python
def get_idx_file(req, backend, mat):
```

## get_info_packs

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L241)

```python
def get_info_packs(req, backend, mat):
```

## get_info_refs

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L201)

```python
def get_info_refs(req, backend, mat):
```

## get_loose_object

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L162)

```python
def get_loose_object(req, backend, mat):
```

## get_pack_file

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L179)

```python
def get_pack_file(req, backend, mat):
```

## get_repo

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L119)

```python
def get_repo(backend, mat) -> BaseRepo:
```

Get a Repo instance for the given backend and URL regex match.

#### See also

- [BaseRepo](repo.md#baserepo)

## get_text_file

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L153)

```python
def get_text_file(req, backend, mat):
```

## handle_service_request

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L271)

```python
def handle_service_request(req, backend, mat):
```

## main

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L545)

```python
def main(argv=sys.argv):
```

Entry point for starting an HTTP git server.

## make_wsgi_chain

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L482)

```python
def make_wsgi_chain(*args, **kwargs):
```

Factory function to create an instance of HTTPGitApplication,
correctly wrapped with needed middleware.

## send_file

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L124)

```python
def send_file(req, f, content_type):
```

Send a file-like object to the request output.

#### Arguments

  - `req` - The HTTPGitRequest object to send output to.
  - `f` - An open file-like object to send; will be closed.
  - `content_type` - The MIME type for the file.
- `Returns` - Iterator over the contents of the file, as chunks.

## url_prefix

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/web.py#L107)

```python
def url_prefix(mat) -> str:
```

Extract the URL prefix from a regex match.

#### Arguments

  - `mat` - A regex match object.
- `Returns` - The URL prefix, defined as the text before the match in the
    original string. Normalized to start with one leading slash and end
    with zero.
