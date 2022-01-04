# Updater

> Auto-generated documentation for [utils.updater](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/utils/updater.py) module.

Ingame AddOns update and caching logic

- [AddOns-Update-Tool](../README.md#addons-update-tool-index) / [Modules](../MODULES.md#addons-update-tool-modules) / [Utils](index.md#utils) / Updater
    - [AddOnsUpdater](#addonsupdater)
        - [AddOnsUpdater().install](#addonsupdaterinstall)

## AddOnsUpdater

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/utils/updater.py#L19)

```python
class AddOnsUpdater():
    def __init__(path_to_addons_folder: Path, vault: Vault):
```

The base class of AddOns updating service

#### See also

- [Vault](vault.md#vault)

### AddOnsUpdater().install

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/utils/updater.py#L143)

```python
def install() -> None:
```

Backup and Install/Update AddOns

#### Arguments

- `vault` *Vault* - Vault instance
