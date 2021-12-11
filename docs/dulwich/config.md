# Config

> Auto-generated documentation for [dulwich.config](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/config.py) module.

Reading and writing Git configuration files.

- [Addons-update-tool](../README.md#addons-update-tool) / [Modules](../MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / Config
    - [CaseInsensitiveDict](#caseinsensitivedict)
        - [CaseInsensitiveDict().get](#caseinsensitivedictget)
        - [CaseInsensitiveDict.make](#caseinsensitivedictmake)
        - [CaseInsensitiveDict().setdefault](#caseinsensitivedictsetdefault)
    - [Config](#config)
        - [Config().get](#configget)
        - [Config().get_boolean](#configget_boolean)
        - [Config().has_section](#confighas_section)
        - [Config().iteritems](#configiteritems)
        - [Config().itersections](#configitersections)
        - [Config().set](#configset)
    - [ConfigDict](#configdict)
        - [ConfigDict().get](#configdictget)
        - [ConfigDict().iteritems](#configdictiteritems)
        - [ConfigDict().itersections](#configdictitersections)
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

## CaseInsensitiveDict

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/config.py#L65)

```python
class CaseInsensitiveDict(OrderedDict):
```

### CaseInsensitiveDict().get

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/config.py#L95)

```python
def get(key, default=SENTINAL):
```

#### See also

- [SENTINAL](#sentinal)

### CaseInsensitiveDict.make

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/config.py#L66)

```python
@classmethod
def make(dict_in=None):
```

### CaseInsensitiveDict().setdefault

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/config.py#L106)

```python
def setdefault(key, default=SENTINAL):
```

#### See also

- [SENTINAL](#sentinal)

## Config

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/config.py#L115)

```python
class Config(object):
```

A Git configuration.

### Config().get

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/config.py#L118)

```python
def get(section, name):
```

Retrieve the contents of a configuration setting.

#### Arguments

- `section` - Tuple with section name and optional subsection namee
- `subsection` - Subsection name

#### Returns

Contents of the setting

#### Raises

- `KeyError` - if the value is not set

### Config().get_boolean

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/config.py#L131)

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

### Config().has_section

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/config.py#L181)

```python
def has_section(name):
```

Check if a specified section exists.

#### Arguments

- `name` - Name of section to check for

#### Returns

boolean indicating whether the section exists

### Config().iteritems

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/config.py#L164)

```python
def iteritems(section):
```

Iterate over the configuration pairs for a specific section.

#### Arguments

- `section` - Tuple with section name and optional subsection namee

#### Returns

Iterator over (name, value) pairs

### Config().itersections

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/config.py#L174)

```python
def itersections():
```

Iterate over the sections.

Returns: Iterator over section tuples

### Config().set

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/config.py#L153)

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

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/config.py#L192)

```python
class ConfigDict(Config, MutableMapping):
    def __init__(values=None, encoding=None):
```

Git configuration stored in a dictionary.

#### See also

- [Config](#config)

### ConfigDict().get

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/config.py#L249)

```python
def get(section, name):
```

### ConfigDict().iteritems

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/config.py#L268)

```python
def iteritems(section):
```

### ConfigDict().itersections

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/config.py#L271)

```python
def itersections():
```

### ConfigDict().set

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/config.py#L260)

```python
def set(section, name, value):
```

## ConfigFile

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/config.py#L383)

```python
class ConfigFile(ConfigDict):
    def __init__(values=None, encoding=None):
```

A Git configuration file, like .git/config or ~/.gitconfig.

#### See also

- [ConfigDict](#configdict)

### ConfigFile.from_file

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/config.py#L390)

```python
@classmethod
def from_file(f: BinaryIO) -> 'ConfigFile':
```

Read configuration from a file-like object.

### ConfigFile.from_path

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/config.py#L458)

```python
@classmethod
def from_path(path) -> 'ConfigFile':
```

Read configuration from a file on disk.

### ConfigFile().write_to_file

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/config.py#L473)

```python
def write_to_file(f: BinaryIO) -> None:
```

Write configuration to a file-like object.

### ConfigFile().write_to_path

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/config.py#L466)

```python
def write_to_path(path=None) -> None:
```

Write configuration to a file on disk.

## StackedConfig

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/config.py#L551)

```python
class StackedConfig(Config):
    def __init__(backends, writable=None):
```

Configuration which reads from multiple config files..

#### See also

- [Config](#config)

### StackedConfig.default

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/config.py#L561)

```python
@classmethod
def default():
```

### StackedConfig.default_backends

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/config.py#L565)

```python
@classmethod
def default_backends():
```

Retrieve the default configuration.

See git-config(1) for details on the files searched.

### StackedConfig().get

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/config.py#L589)

```python
def get(section, name):
```

### StackedConfig().set

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/config.py#L599)

```python
def set(section, name, value):
```

## get_win_system_paths

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/config.py#L541)

```python
def get_win_system_paths():
```

## get_xdg_config_home_path

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/config.py#L495)

```python
def get_xdg_config_home_path(*path_segments):
```

## lower_key

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/config.py#L55)

```python
def lower_key(key):
```

## parse_submodules

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/config.py#L605)

```python
def parse_submodules(config):
```

Parse a gitmodules GitConfig file, returning submodules.

#### Arguments

- `config` - A [ConfigFile](#configfile)

#### Returns

list of tuples (submodule path, url, name),
  where name is quoted part of the section's name.
