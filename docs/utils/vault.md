# Vault

> Auto-generated documentation for [utils.vault](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/utils/vault.py) module.

Vault fetch and caching logic

- [Addons-update-tool](../README.md#addons-update-tool) / [Modules](../MODULES.md#addons-update-tool-modules) / [Utils](index.md#utils) / Vault
    - [Repository](#repository)
        - [Repository().check_remote_refs](#repositorycheck_remote_refs)
        - [Repository().checkout](#repositorycheckout)
        - [Repository().download](#repositorydownload)
        - [Repository().remove](#repositoryremove)
    - [Vault](#vault)
        - [Vault().new_or_update](#vaultnew_or_update)
        - [Vault().refresh](#vaultrefresh)

## Repository

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/utils/vault.py#L21)

```python
class Repository():
    def __init__(url: str, branch: str, basedir: Path):
```

The base class of Repository in Vault

### Repository().check_remote_refs

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/utils/vault.py#L89)

```python
def check_remote_refs() -> bool:
```

Check branch existence on GitHub

#### Returns

- `True` - branch found
- `False` - branch not found

### Repository().checkout

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/utils/vault.py#L163)

```python
def checkout(old_branch: str) -> bool:
```

Change branch of Repository

#### Arguments

- `old_branch` *str* - name of cached branch

#### Returns

- `True` - branch changed
- `False` - checkout fail

### Repository().download

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/utils/vault.py#L111)

```python
def download() -> 'bool | int':
```

Download Repository if not exist or update if exist

#### Returns

- `True` - downloaded
- `-1` - already exist and has been successfully updated
- `False` - fail

### Repository().remove

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/utils/vault.py#L144)

```python
def remove() -> bool:
```

Remove Repository from Vault

#### Returns

- `True` - success
- `False` - fail

## Vault

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/utils/vault.py#L194)

```python
class Vault():
    def __init__(name: str) -> None:
```

The base class of repositories Vault

### Vault().new_or_update

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/utils/vault.py#L240)

```python
@threaded
def new_or_update(url: str, branch: str) -> None:
```

Create new Repository in Vault (or update exist in child function)

#### Arguments

- `url` *str* - link to github repository
- `branch` *str* - branch of github repository to download/update

#### See also

- [threaded](threads.md#threaded)

### Vault().refresh

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/utils/vault.py#L270)

```python
def refresh() -> None:
```

Refresh Vault database
