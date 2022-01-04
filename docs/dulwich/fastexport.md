# Fastexport

> Auto-generated documentation for [dulwich.fastexport](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/fastexport.py) module.

Fast export/import functionality.

- [AddOns-Update-Tool](../README.md#addons-update-tool-index) / [Modules](../MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / Fastexport
    - [GitFastExporter](#gitfastexporter)
        - [GitFastExporter().emit_blob](#gitfastexporteremit_blob)
        - [GitFastExporter().emit_commit](#gitfastexporteremit_commit)
        - [GitFastExporter().print_cmd](#gitfastexporterprint_cmd)
    - [GitImportProcessor](#gitimportprocessor)
        - [GitImportProcessor().blob_handler](#gitimportprocessorblob_handler)
        - [GitImportProcessor().checkpoint_handler](#gitimportprocessorcheckpoint_handler)
        - [GitImportProcessor().commit_handler](#gitimportprocessorcommit_handler)
        - [GitImportProcessor().feature_handler](#gitimportprocessorfeature_handler)
        - [GitImportProcessor().import_stream](#gitimportprocessorimport_stream)
        - [GitImportProcessor().lookup_object](#gitimportprocessorlookup_object)
        - [GitImportProcessor().progress_handler](#gitimportprocessorprogress_handler)
        - [GitImportProcessor().reset_handler](#gitimportprocessorreset_handler)
        - [GitImportProcessor().tag_handler](#gitimportprocessortag_handler)
    - [split_email](#split_email)

## GitFastExporter

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/fastexport.py#L48)

```python
class GitFastExporter(object):
    def __init__(outf, store):
```

Generate a fast-export output stream for Git objects.

### GitFastExporter().emit_blob

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/fastexport.py#L69)

```python
def emit_blob(blob):
```

### GitFastExporter().emit_commit

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/fastexport.py#L122)

```python
def emit_commit(commit, ref, base_tree=None):
```

### GitFastExporter().print_cmd

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/fastexport.py#L57)

```python
def print_cmd(cmd):
```

## GitImportProcessor

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/fastexport.py#L128)

```python
class GitImportProcessor(processor.ImportProcessor):
    def __init__(repo, params=None, verbose=False, outf=None):
```

An import processor that imports into a Git repository using Dulwich.

### GitImportProcessor().blob_handler

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/fastexport.py#L150)

```python
def blob_handler(cmd):
```

Process a BlobCommand.

### GitImportProcessor().checkpoint_handler

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/fastexport.py#L157)

```python
def checkpoint_handler(cmd):
```

Process a CheckpointCommand.

### GitImportProcessor().commit_handler

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/fastexport.py#L161)

```python
def commit_handler(cmd):
```

Process a CommitCommand.

### GitImportProcessor().feature_handler

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/fastexport.py#L263)

```python
def feature_handler(cmd):
```

Process a FeatureCommand.

### GitImportProcessor().import_stream

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/fastexport.py#L145)

```python
def import_stream(stream):
```

### GitImportProcessor().lookup_object

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/fastexport.py#L140)

```python
def lookup_object(objectish):
```

### GitImportProcessor().progress_handler

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/fastexport.py#L227)

```python
def progress_handler(cmd):
```

Process a ProgressCommand.

### GitImportProcessor().reset_handler

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/fastexport.py#L245)

```python
def reset_handler(cmd):
```

Process a ResetCommand.

### GitImportProcessor().tag_handler

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/fastexport.py#L254)

```python
def tag_handler(cmd):
```

Process a TagCommand.

## split_email

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/fastexport.py#L43)

```python
def split_email(text):
```
