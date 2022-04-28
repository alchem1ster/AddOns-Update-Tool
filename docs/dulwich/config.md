# Config

> Auto-generated documentation for [dulwich.config](../../dulwich/config.py) module.

Reading and writing Git configuration files.

- [AddOns-Update-Tool](../README.md#addons-update-tool-index) / [Modules](../MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / Config
    - [CaseInsensitiveOrderedMultiDict](#caseinsensitiveorderedmultidict)
        - [CaseInsensitiveOrderedMultiDict().get](#caseinsensitiveorderedmultidictget)
        - [CaseInsensitiveOrderedMultiDict().get_all](#caseinsensitiveorderedmultidictget_all)
        - [CaseInsensitiveOrderedMultiDict().items](#caseinsensitiveorderedmultidictitems)
        - [CaseInsensitiveOrderedMultiDict().keys](#caseinsensitiveorderedmultidictkeys)
        - [CaseInsensitiveOrderedMultiDict.make](#caseinsensitiveorderedmultidictmake)
        - [CaseInsensitiveOrderedMultiDict().setdefault](#caseinsensitiveorderedmultidictsetdefault)
        - [CaseInsensitiveOrderedMultiDict().values](#caseinsensitiveorderedmultidictvalues)
    - [Config](#config)
        - [Config().get](#configget)
        - [Config().get_boolean](#configget_boolean)
        - [Config().get_multivar](#configget_multivar)
        - [Config().has_section](#confighas_section)
        - [Config().items](#configitems)
        - [Config().iteritems](#configiteritems)
        - [Config().itersections](#configitersections)
        - [Config().sections](#configsections)
        - [Config().set](#configset)
    - [ConfigDict](#configdict)
        - [ConfigDict().get](#configdictget)
        - [ConfigDict().get_multivar](#configdictget_multivar)
        - [ConfigDict().items](#configdictitems)
        - [ConfigDict().sections](#configdictsections)
        - [ConfigDict().set](#configdictset)
    - [ConfigFile](#configfile)
        - [ConfigFile.from_file](#configfilefrom_file)
        - [ConfigFile.from_path](#configfilefrom_path)
        - [ConfigFile().write_to_file](#configfilewrite_to_file)
        - [ConfigFile().write_to_path](#configfilewrite_to_path)
    - [StackedConfig](#stackedconfig)
        - [StackedConfig.default](#stackedconfigdefault)
        - [StackedConfig.default_backends](#stackedconfigdefault_backends)
        - [StackedConfig().get](#stackedconfigget)
        - [StackedConfig().set](#stackedconfigset)
    - [get_win_system_paths](#get_win_system_paths)
    - [get_xdg_config_home_path](#get_xdg_config_home_path)
    - [lower_key](#lower_key)
    - [parse_submodules](#parse_submodules)

TODO:
 * preserve formatting when updating configuration files
 * treat subsection names as case-insensitive for [branch.foo] style
   subsections

## CaseInsensitiveOrderedMultiDict

[[find in source code]](../../dulwich/config.py#L62)

```python
class CaseInsensitiveOrderedMultiDict(MutableMapping):
    def __init__():
```

### CaseInsensitiveOrderedMultiDict().get

[[find in source code]](../../dulwich/config.py#L115)

```python
def get(key, default=SENTINAL):
```

#### See also

- [SENTINAL](#sentinal)

### CaseInsensitiveOrderedMultiDict().get_all

[[find in source code]](../../dulwich/config.py#L126)

```python
def get_all(key):
```

### CaseInsensitiveOrderedMultiDict().items

[[find in source code]](../../dulwich/config.py#L92)

```python
def items():
```

### CaseInsensitiveOrderedMultiDict().keys

[[find in source code]](../../dulwich/config.py#L89)

```python
def keys():
```

### CaseInsensitiveOrderedMultiDict.make

[[find in source code]](../../dulwich/config.py#L67)

```python
@classmethod
def make(dict_in=None):
```

### CaseInsensitiveOrderedMultiDict().setdefault

[[find in source code]](../../dulwich/config.py#L132)

```python
def setdefault(key, default=SENTINAL):
```

#### See also

- [SENTINAL](#sentinal)

### CaseInsensitiveOrderedMultiDict().values

[[find in source code]](../../dulwich/config.py#L98)

```python
def values():
```

## Config

[[find in source code]](../../dulwich/config.py#L141)

```python
class Config(object):
```

A Git configuration.

### Config().get

[[find in source code]](../../dulwich/config.py#L144)

```python
def get(section, name):
```

Retrieve the contents of a configuration setting.

#### Arguments

- `section` - Tuple with section name and optional subsection namee
- `name` - Variable name

#### Returns

Contents of the setting

#### Raises

- `KeyError` - if the value is not set

### Config().get_boolean

[[find in source code]](../../dulwich/config.py#L170)

```python
def get_boolean(section, name, default=None):
```

Retrieve a configuration setting as boolean.

#### Arguments

- `section` - Tuple with section name and optional subsection name
- `name` - Name of the setting, including section and possible
  subsection.

#### Returns

Contents of the setting

#### Raises

- `KeyError` - if the value is not set

### Config().get_multivar

[[find in source code]](../../dulwich/config.py#L157)

```python
def get_multivar(section, name):
```

Retrieve the contents of a multivar configuration setting.

#### Arguments

- `section` - Tuple with section name and optional subsection namee
- `name` - Variable name

#### Returns

Contents of the setting as iterable

#### Raises

- `KeyError` - if the value is not set

### Config().has_section

[[find in source code]](../../dulwich/config.py#L243)

```python
def has_section(name):
```

Check if a specified section exists.

#### Arguments

- `name` - Name of section to check for

#### Returns

boolean indicating whether the section exists

### Config().items

[[find in source code]](../../dulwich/config.py#L203)

```python
def items(section):
```

Iterate over the configuration pairs for a specific section.

#### Arguments

- `section` - Tuple with section name and optional subsection namee

#### Returns

Iterator over (name, value) pairs

### Config().iteritems

[[find in source code]](../../dulwich/config.py#L213)

```python
def iteritems(section):
```

Iterate over the configuration pairs for a specific section.

#### Arguments

- `section` - Tuple with section name and optional subsection namee

#### Returns

Iterator over (name, value) pairs

### Config().itersections

[[find in source code]](../../dulwich/config.py#L228)

```python
def itersections():
```

### Config().sections

[[find in source code]](../../dulwich/config.py#L236)

```python
def sections():
```

Iterate over the sections.

Returns: Iterator over section tuples

### Config().set

[[find in source code]](../../dulwich/config.py#L192)

```python
def set(section, name, value):
```

Set a configuration value.

#### Arguments

- `section` - Tuple with section name and optional subsection namee
- `name` - Name of the configuration value, including section
  and optional subsection
- `value` - value of the setting

## ConfigDict

[[find in source code]](../../dulwich/config.py#L254)

```python
class ConfigDict(Config, MutableMapping):
    def __init__(values=None, encoding=None):
```

Git configuration stored in a dictionary.

#### See also

- [Config](#config)

### ConfigDict().get

[[find in source code]](../../dulwich/config.py#L324)

```python
def get(section, name):
```

### ConfigDict().get_multivar

[[find in source code]](../../dulwich/config.py#L313)

```python
def get_multivar(section, name):
```

### ConfigDict().items

[[find in source code]](../../dulwich/config.py#L343)

```python
def items(section):
```

### ConfigDict().sections

[[find in source code]](../../dulwich/config.py#L346)

```python
def sections():
```

### ConfigDict().set

[[find in source code]](../../dulwich/config.py#L335)

```python
def set(section, name, value):
```

## ConfigFile

[[find in source code]](../../dulwich/config.py#L459)

```python
class ConfigFile(ConfigDict):
    def __init__(values=None, encoding=None):
```

A Git configuration file, like .git/config or ~/.gitconfig.

#### See also

- [ConfigDict](#configdict)

### ConfigFile.from_file

[[find in source code]](../../dulwich/config.py#L466)

```python
@classmethod
def from_file(f: BinaryIO) -> 'ConfigFile':
```

Read configuration from a file-like object.

### ConfigFile.from_path

[[find in source code]](../../dulwich/config.py#L538)

```python
@classmethod
def from_path(path) -> 'ConfigFile':
```

Read configuration from a file on disk.

### ConfigFile().write_to_file

[[find in source code]](../../dulwich/config.py#L553)

```python
def write_to_file(f: BinaryIO) -> None:
```

Write configuration to a file-like object.

### ConfigFile().write_to_path

[[find in source code]](../../dulwich/config.py#L546)

```python
def write_to_path(path=None) -> None:
```

Write configuration to a file on disk.

## StackedConfig

[[find in source code]](../../dulwich/config.py#L635)

```python
class StackedConfig(Config):
    def __init__(backends, writable=None):
```

Configuration which reads from multiple config files..

#### See also

- [Config](#config)

### StackedConfig.default

[[find in source code]](../../dulwich/config.py#L645)

```python
@classmethod
def default():
```

### StackedConfig.default_backends

[[find in source code]](../../dulwich/config.py#L649)

```python
@classmethod
def default_backends():
```

Retrieve the default configuration.

See git-config(1) for details on the files searched.

### StackedConfig().get

[[find in source code]](../../dulwich/config.py#L673)

```python
def get(section, name):
```

### StackedConfig().set

[[find in source code]](../../dulwich/config.py#L683)

```python
def set(section, name, value):
```

## get_win_system_paths

[[find in source code]](../../dulwich/config.py#L625)

```python
def get_win_system_paths():
```

## get_xdg_config_home_path

[[find in source code]](../../dulwich/config.py#L577)

```python
def get_xdg_config_home_path(*path_segments):
```

## lower_key

[[find in source code]](../../dulwich/config.py#L52)

```python
def lower_key(key):
```

## parse_submodules

[[find in source code]](../../dulwich/config.py#L689)

```python
def parse_submodules(config):
```

Parse a gitmodules GitConfig file, returning submodules.

#### Arguments

- `config` - A [ConfigFile](#configfile)

#### Returns

list of tuples (submodule path, url, name),
  where name is quoted part of the section's name.
