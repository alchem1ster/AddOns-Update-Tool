# Hooks

> Auto-generated documentation for [dulwich.hooks](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/hooks.py) module.

Access to hooks.

- [Addons-update-tool](../README.md#addons-update-tool) / [Modules](../MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / Hooks
    - [CommitMsgShellHook](#commitmsgshellhook)
    - [Hook](#hook)
        - [Hook().execute](#hookexecute)
    - [PostCommitShellHook](#postcommitshellhook)
    - [PostReceiveShellHook](#postreceiveshellhook)
        - [PostReceiveShellHook().execute](#postreceiveshellhookexecute)
    - [PreCommitShellHook](#precommitshellhook)
    - [ShellHook](#shellhook)
        - [ShellHook().execute](#shellhookexecute)

## CommitMsgShellHook

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/hooks.py#L135)

```python
class CommitMsgShellHook(ShellHook):
    def __init__(controldir):
```

commit-msg shell hook

#### Arguments

- `args[0]` - commit message

#### Returns

new commit message or None

#### See also

- [ShellHook](#shellhook)

## Hook

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/hooks.py#L31)

```python
class Hook(object):
```

Generic hook object.

### Hook().execute

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/hooks.py#L34)

```python
def execute(*args):
```

Execute the hook with the given args

#### Arguments

- `args` - argument list to hook

#### Raises

- `HookError` - hook execution failure

#### Returns

a hook may return a useful value

## PostCommitShellHook

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/hooks.py#L126)

```python
class PostCommitShellHook(ShellHook):
    def __init__(controldir):
```

post-commit shell hook

#### See also

- [ShellHook](#shellhook)

## PostReceiveShellHook

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/hooks.py#L170)

```python
class PostReceiveShellHook(ShellHook):
    def __init__(controldir):
```

post-receive shell hook

#### See also

- [ShellHook](#shellhook)

### PostReceiveShellHook().execute

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/hooks.py#L178)

```python
def execute(client_refs):
```

## PreCommitShellHook

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/hooks.py#L117)

```python
class PreCommitShellHook(ShellHook):
    def __init__(controldir):
```

pre-commit shell hook

#### See also

- [ShellHook](#shellhook)

## ShellHook

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/hooks.py#L47)

```python
class ShellHook(Hook):
    def __init__(
        name,
        path,
        numparam,
        pre_exec_callback=None,
        post_exec_callback=None,
        cwd=None,
    ):
```

Hook by executable file

Implements standard githooks(5) [0]:

[0] http://www.kernel.org/pub/software/scm/git/docs/githooks.html

#### See also

- [Hook](#hook)

### ShellHook().execute

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/hooks.py#L89)

```python
def execute(*args):
```

Execute the hook with given args
