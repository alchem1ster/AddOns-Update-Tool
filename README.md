# AddOns Update Tool
 Tool to update World of Warcraft AddOns hosted on GitHub

![](https://img.shields.io/github/issues/alchem1ster/AddOns-Update-Tool) ![](https://img.shields.io/github/stars/alchem1ster/AddOns-Update-Tool) ![](https://img.shields.io/github/forks/alchem1ster/AddOns-Update-Tool) ![](https://img.shields.io/github/v/release/alchem1ster/AddOns-Update-Tool) ![](https://img.shields.io/codefactor/grade/github/alchem1ster/AddOns-Update-Tool)

### Features
- [x] Almost pure Python: only [Dulwich](https://github.com/dulwich/dulwich "Dulwich") and [Colorlog](https://github.com/borntyping/python-colorlog "Colorlog")
- [x] Multithreaded tasks
- [x] Manual and automatic modes
- [x] Able to start the game after an updates
- [x] Automatic backup of updatable AddOns (up to the last 5)
- [x] Automatic detection of AddOn directories (aka modules)

<br>

<img src="./_res/runtime_record.gif" width="70%"/>

<br>

## Usage
Before running this script for the first time, I STRONGLY RECOMMEND making a backup of your `Interface` folder: something bad is unlikely to happen, but just in case

### Configuration file
Before using this script, you need to configure the list of repositories (AddOns) for updating.
Just see how this is done in the `config_example.json` file.  In general terms, it is a simple [JSON](https://en.wikipedia.org/wiki/JSON "JSON") file, where you need to specify the repository URL and the branch you want to clone (usually it will be `master` or `main`):
```json
{
	"URL1" : "master",
	"URL2" : "master"
}
```
Note that curly brackets, quotation marks, colons, and commas are mandatory characters in JSON structure
### Help page
When you run the script from the release version or the source code with the `-h` parameter, the help page will be displayed:

###### optional arguments
| Argument | Abbrev | Description | Example |
| ------------ | ------------ | ------------ | ------------ |
| \--help | -h |  show help message and exit | -h |
| \--start | -s | start Wow.exe after update | -s |
| \--verbose |  | verbose debug output | \--verbose |
###### required arguments
| Argument | Abbrev | Description | Example |
| ------------ | ------------ | ------------ | ------------ |
| \--vault | -v |  new or existing Vault name | -v github |
| \--wow | -w | path to Wow.exe | -w "G:\World of Warcraft 3.3.5a HD\Wow.exe" |
| \--config | -c | path to json config file | -c ".\config_335a.json" |

### Launching from RELEASE version
1. Download [latest release](https://github.com/alchem1ster/AddOns-Update-Tool//releases/latest)
2. Unpack to any folder
3. Copy and edit `config.json` as you need (see [Configuration](https://github.com/alchem1ster/AddOns-Update-Tool#configuration-file) paragraph)
4. Run app with the `-h` parameter via `cmd` or `powershell` to read the help
5. As an example, use one of the following commands:  
`    .\app.exe -v github -w ..\wow\Wow.exe -c .\config.json -s --verbose`
`    .\AddOnsUpdateTool.exe -v github -w ..\wow\Wow.exe -c .\config.json -s --verbose`
or the next one if you put `AddOnsUpdateTool.exe` and `config.json` in the game folder:
`    .\AddOnsUpdateTool.exe -v github -w -c -s --verbose`
or even just start `AddOnsUpdateTool.exe` inside game folder
6. If you want, you can create a shortcut to start with the necessary arguments and place it on the desktop or start menu

### Launching from SOURCE code
Running the script from source code will require some knowledge of both Git and Cmd/Powershell

#### Requirements
- Install Python 3.8 (recommended)
- Install Pipenv package via `pip install -U pipenv`

#### Prepare
- Clone this repository
- Run `pipenv install` inside repository directory
- If successful, you can use `pipenv shell` to open Pipenv Venv Shell inside

#### Launch
- Use `python .\app.py -h` inside Pipenv Venv Shell to see the help page

<br>

## Dev dependencies
If you want to change something in the code, I strongly recommend that you set the PEP-8 code formatter `black` and `pyinstaller` via `pipenv install --dev` command. Dont forget to re-format code after changes to keep it within the PEP-8.

## Creating an EXE
To package a set of scripts into a standalone distributable directory, or a single EXE file, use the `pyinstaller` module:
- `pipenv run pyinstaller --onefile .\app.py` -- for single EXE file (smaller size, but slower runtime due to the temp cache)
- `pipenv run pyinstaller .\AddonsUpdateTool_dir.spec` -- for standalone directory (larger whole folder size, but fast runtime)

## Additional information
In addition to `app.py` I also provide scripts to manually update the Vault DB and the Game DB: `vault_updater.py` and `game_updater.py`. You can also use the `-h` argument to view the help page
