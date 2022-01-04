# Cli

> Auto-generated documentation for [dulwich.cli](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py) module.

Simple command-line interface to Dulwich>

- [AddOns-Update-Tool](../README.md#addons-update-tool-index) / [Modules](../MODULES.md#addons-update-tool-modules) / [Dulwich](index.md#dulwich) / Cli
    - [Command](#command)
        - [Command().run](#commandrun)
    - [SuperCommand](#supercommand)
        - [SuperCommand().run](#supercommandrun)
    - [cmd_add](#cmd_add)
        - [cmd_add().run](#cmd_addrun)
    - [cmd_archive](#cmd_archive)
        - [cmd_archive().run](#cmd_archiverun)
    - [cmd_check_ignore](#cmd_check_ignore)
        - [cmd_check_ignore().run](#cmd_check_ignorerun)
    - [cmd_check_mailmap](#cmd_check_mailmap)
        - [cmd_check_mailmap().run](#cmd_check_mailmaprun)
    - [cmd_clone](#cmd_clone)
        - [cmd_clone().run](#cmd_clonerun)
    - [cmd_commit](#cmd_commit)
        - [cmd_commit().run](#cmd_commitrun)
    - [cmd_commit_tree](#cmd_commit_tree)
        - [cmd_commit_tree().run](#cmd_commit_treerun)
    - [cmd_daemon](#cmd_daemon)
        - [cmd_daemon().run](#cmd_daemonrun)
    - [cmd_describe](#cmd_describe)
        - [cmd_describe().run](#cmd_describerun)
    - [cmd_diff](#cmd_diff)
        - [cmd_diff().run](#cmd_diffrun)
    - [cmd_diff_tree](#cmd_diff_tree)
        - [cmd_diff_tree().run](#cmd_diff_treerun)
    - [cmd_dump_index](#cmd_dump_index)
        - [cmd_dump_index().run](#cmd_dump_indexrun)
    - [cmd_dump_pack](#cmd_dump_pack)
        - [cmd_dump_pack().run](#cmd_dump_packrun)
    - [cmd_fetch](#cmd_fetch)
        - [cmd_fetch().run](#cmd_fetchrun)
    - [cmd_fetch_pack](#cmd_fetch_pack)
        - [cmd_fetch_pack().run](#cmd_fetch_packrun)
    - [cmd_fsck](#cmd_fsck)
        - [cmd_fsck().run](#cmd_fsckrun)
    - [cmd_help](#cmd_help)
        - [cmd_help().run](#cmd_helprun)
    - [cmd_init](#cmd_init)
        - [cmd_init().run](#cmd_initrun)
    - [cmd_log](#cmd_log)
        - [cmd_log().run](#cmd_logrun)
    - [cmd_ls_files](#cmd_ls_files)
        - [cmd_ls_files().run](#cmd_ls_filesrun)
    - [cmd_ls_remote](#cmd_ls_remote)
        - [cmd_ls_remote().run](#cmd_ls_remoterun)
    - [cmd_ls_tree](#cmd_ls_tree)
        - [cmd_ls_tree().run](#cmd_ls_treerun)
    - [cmd_pack_objects](#cmd_pack_objects)
        - [cmd_pack_objects().run](#cmd_pack_objectsrun)
    - [cmd_pull](#cmd_pull)
        - [cmd_pull().run](#cmd_pullrun)
    - [cmd_push](#cmd_push)
        - [cmd_push().run](#cmd_pushrun)
    - [cmd_receive_pack](#cmd_receive_pack)
        - [cmd_receive_pack().run](#cmd_receive_packrun)
    - [cmd_remote](#cmd_remote)
    - [cmd_remote_add](#cmd_remote_add)
        - [cmd_remote_add().run](#cmd_remote_addrun)
    - [cmd_repack](#cmd_repack)
        - [cmd_repack().run](#cmd_repackrun)
    - [cmd_reset](#cmd_reset)
        - [cmd_reset().run](#cmd_resetrun)
    - [cmd_rev_list](#cmd_rev_list)
        - [cmd_rev_list().run](#cmd_rev_listrun)
    - [cmd_rm](#cmd_rm)
        - [cmd_rm().run](#cmd_rmrun)
    - [cmd_show](#cmd_show)
        - [cmd_show().run](#cmd_showrun)
    - [cmd_stash](#cmd_stash)
    - [cmd_stash_list](#cmd_stash_list)
        - [cmd_stash_list().run](#cmd_stash_listrun)
    - [cmd_stash_pop](#cmd_stash_pop)
        - [cmd_stash_pop().run](#cmd_stash_poprun)
    - [cmd_stash_push](#cmd_stash_push)
        - [cmd_stash_push().run](#cmd_stash_pushrun)
    - [cmd_status](#cmd_status)
        - [cmd_status().run](#cmd_statusrun)
    - [cmd_symbolic_ref](#cmd_symbolic_ref)
        - [cmd_symbolic_ref().run](#cmd_symbolic_refrun)
    - [cmd_tag](#cmd_tag)
        - [cmd_tag().run](#cmd_tagrun)
    - [cmd_update_server_info](#cmd_update_server_info)
        - [cmd_update_server_info().run](#cmd_update_server_inforun)
    - [cmd_upload_pack](#cmd_upload_pack)
        - [cmd_upload_pack().run](#cmd_upload_packrun)
    - [cmd_web_daemon](#cmd_web_daemon)
        - [cmd_web_daemon().run](#cmd_web_daemonrun)
    - [cmd_write_tree](#cmd_write_tree)
        - [cmd_write_tree().run](#cmd_write_treerun)
    - [main](#main)
    - [signal_int](#signal_int)
    - [signal_quit](#signal_quit)

This is a very simple command-line wrapper for Dulwich. It is by
no means intended to be a full-blown Git command-line interface but just
a way to test Dulwich.

## Command

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L58)

```python
class Command(object):
```

A Dulwich subcommand.

### Command().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L61)

```python
def run(args):
```

Run the command.

## SuperCommand

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L581)

```python
class SuperCommand(Command):
```

#### See also

- [Command](#command)

### SuperCommand().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L585)

```python
def run(args):
```

## cmd_add

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L93)

```python
class cmd_add(Command):
```

#### See also

- [Command](#command)

### cmd_add().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L94)

```python
def run(argv):
```

## cmd_archive

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L66)

```python
class cmd_archive(Command):
```

#### See also

- [Command](#command)

### cmd_archive().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L67)

```python
def run(args):
```

## cmd_check_ignore

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L608)

```python
class cmd_check_ignore(Command):
```

#### See also

- [Command](#command)

### cmd_check_ignore().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L609)

```python
def run(args):
```

## cmd_check_mailmap

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L619)

```python
class cmd_check_mailmap(Command):
```

#### See also

- [Command](#command)

### cmd_check_mailmap().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L620)

```python
def run(args):
```

## cmd_clone

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L242)

```python
class cmd_clone(Command):
```

#### See also

- [Command](#command)

### cmd_clone().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L243)

```python
def run(args):
```

## cmd_commit

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L269)

```python
class cmd_commit(Command):
```

#### See also

- [Command](#command)

### cmd_commit().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L270)

```python
def run(args):
```

## cmd_commit_tree

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L276)

```python
class cmd_commit_tree(Command):
```

#### See also

- [Command](#command)

### cmd_commit_tree().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L277)

```python
def run(args):
```

## cmd_daemon

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L367)

```python
class cmd_daemon(Command):
```

#### See also

- [Command](#command)

### cmd_daemon().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L368)

```python
def run(args):
```

## cmd_describe

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L669)

```python
class cmd_describe(Command):
```

#### See also

- [Command](#command)

### cmd_describe().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L670)

```python
def run(args):
```

## cmd_diff

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L173)

```python
class cmd_diff(Command):
```

#### See also

- [Command](#command)

### cmd_diff().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L174)

```python
def run(args):
```

## cmd_diff_tree

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L310)

```python
class cmd_diff_tree(Command):
```

#### See also

- [Command](#command)

### cmd_diff_tree().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L311)

```python
def run(args):
```

## cmd_dump_index

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L214)

```python
class cmd_dump_index(Command):
```

#### See also

- [Command](#command)

### cmd_dump_index().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L215)

```python
def run(args):
```

## cmd_dump_pack

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L190)

```python
class cmd_dump_pack(Command):
```

#### See also

- [Command](#command)

### cmd_dump_pack().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L191)

```python
def run(args):
```

## cmd_fetch

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L127)

```python
class cmd_fetch(Command):
```

#### See also

- [Command](#command)

### cmd_fetch().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L128)

```python
def run(args):
```

## cmd_fetch_pack

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L109)

```python
class cmd_fetch_pack(Command):
```

#### See also

- [Command](#command)

### cmd_fetch_pack().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L110)

```python
def run(argv):
```

## cmd_fsck

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L139)

```python
class cmd_fsck(Command):
```

#### See also

- [Command](#command)

### cmd_fsck().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L140)

```python
def run(args):
```

## cmd_help

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L676)

```python
class cmd_help(Command):
```

#### See also

- [Command](#command)

### cmd_help().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L677)

```python
def run(args):
```

## cmd_init

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L229)

```python
class cmd_init(Command):
```

#### See also

- [Command](#command)

### cmd_init().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L230)

```python
def run(args):
```

## cmd_log

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L147)

```python
class cmd_log(Command):
```

#### See also

- [Command](#command)

### cmd_log().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L148)

```python
def run(args):
```

## cmd_ls_files

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L661)

```python
class cmd_ls_files(Command):
```

#### See also

- [Command](#command)

### cmd_ls_files().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L662)

```python
def run(args):
```

## cmd_ls_remote

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L495)

```python
class cmd_ls_remote(Command):
```

#### See also

- [Command](#command)

### cmd_ls_remote().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L496)

```python
def run(args):
```

## cmd_ls_tree

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L506)

```python
class cmd_ls_tree(Command):
```

#### See also

- [Command](#command)

### cmd_ls_tree().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L507)

```python
def run(args):
```

## cmd_pack_objects

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L532)

```python
class cmd_pack_objects(Command):
```

#### See also

- [Command](#command)

### cmd_pack_objects().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L533)

```python
def run(args):
```

## cmd_pull

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L554)

```python
class cmd_pull(Command):
```

#### See also

- [Command](#command)

### cmd_pull().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L555)

```python
def run(args):
```

## cmd_push

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L565)

```python
class cmd_push(Command):
```

#### See also

- [Command](#command)

### cmd_push().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L566)

```python
def run(argv):
```

## cmd_receive_pack

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L441)

```python
class cmd_receive_pack(Command):
```

#### See also

- [Command](#command)

### cmd_receive_pack().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L442)

```python
def run(args):
```

## cmd_remote

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L601)

```python
class cmd_remote(SuperCommand):
```

#### See also

- [SuperCommand](#supercommand)

## cmd_remote_add

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L574)

```python
class cmd_remote_add(Command):
```

#### See also

- [Command](#command)

### cmd_remote_add().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L575)

```python
def run(args):
```

## cmd_repack

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L346)

```python
class cmd_repack(Command):
```

#### See also

- [Command](#command)

### cmd_repack().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L347)

```python
def run(args):
```

## cmd_reset

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L353)

```python
class cmd_reset(Command):
```

#### See also

- [Command](#command)

### cmd_reset().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L354)

```python
def run(args):
```

## cmd_rev_list

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L319)

```python
class cmd_rev_list(Command):
```

#### See also

- [Command](#command)

### cmd_rev_list().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L320)

```python
def run(args):
```

## cmd_rm

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L101)

```python
class cmd_rm(Command):
```

#### See also

- [Command](#command)

### cmd_rm().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L102)

```python
def run(argv):
```

## cmd_show

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L302)

```python
class cmd_show(Command):
```

#### See also

- [Command](#command)

### cmd_show().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L303)

```python
def run(argv):
```

## cmd_stash

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L652)

```python
class cmd_stash(SuperCommand):
```

#### See also

- [SuperCommand](#supercommand)

## cmd_stash_list

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L628)

```python
class cmd_stash_list(Command):
```

#### See also

- [Command](#command)

### cmd_stash_list().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L629)

```python
def run(args):
```

## cmd_stash_pop

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L644)

```python
class cmd_stash_pop(Command):
```

#### See also

- [Command](#command)

### cmd_stash_pop().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L645)

```python
def run(args):
```

## cmd_stash_push

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L636)

```python
class cmd_stash_push(Command):
```

#### See also

- [Command](#command)

### cmd_stash_push().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L637)

```python
def run(args):
```

## cmd_status

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L463)

```python
class cmd_status(Command):
```

#### See also

- [Command](#command)

### cmd_status().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L464)

```python
def run(args):
```

## cmd_symbolic_ref

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L291)

```python
class cmd_symbolic_ref(Command):
```

#### See also

- [Command](#command)

### cmd_symbolic_ref().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L292)

```python
def run(args):
```

## cmd_tag

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L328)

```python
class cmd_tag(Command):
```

#### See also

- [Command](#command)

### cmd_tag().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L329)

```python
def run(args):
```

## cmd_update_server_info

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L286)

```python
class cmd_update_server_info(Command):
```

#### See also

- [Command](#command)

### cmd_update_server_info().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L287)

```python
def run(args):
```

## cmd_upload_pack

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L452)

```python
class cmd_upload_pack(Command):
```

#### See also

- [Command](#command)

### cmd_upload_pack().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L453)

```python
def run(args):
```

## cmd_web_daemon

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L401)

```python
class cmd_web_daemon(Command):
```

#### See also

- [Command](#command)

### cmd_web_daemon().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L402)

```python
def run(args):
```

## cmd_write_tree

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L434)

```python
class cmd_write_tree(Command):
```

#### See also

- [Command](#command)

### cmd_write_tree().run

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L435)

```python
def run(args):
```

## main

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L747)

```python
def main(argv=None):
```

## signal_int

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L48)

```python
def signal_int(signal, frame):
```

## signal_quit

[[find in source code]](https://github.com/alchem1ster/AddOns-Update-Tool/blob/main/dulwich/cli.py#L52)

```python
def signal_quit(signal, frame):
```
