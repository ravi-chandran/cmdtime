# cmdtime

[![Build Status](https://travis-ci.org/ravi-chandran/cmdtime.svg?branch=master)](https://travis-ci.org/ravi-chandran/cmdtime)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

- Similar to the Linux `time` utility for measuring how long a command takes to run
- Useful for the Windows 10 Command Prompt which doesn't natively have this feature
- Shows measurement as: `Elapsed Time: hh:mm:ss`
- Uses pure Python
- No need to install Cygwin, or other older binaries of unclear origin
- No point using this under Linux (but tested via Travis CI anyway)

![](img/cmdtimedemo.gif)

# Installation
- Requires Python 3.5+.
- Install from PyPi:

```bat
python -m pip install cmdtime
```

# Usage Examples
- Timing demonstration using Windows `timeout` command for 5 seconds:

```
cmdtime timeout /t 5

Waiting for 0 seconds, press a key to continue ...
Elapsed Time: 00:00:05
```

- Time anything else, e.g. a Python script

```bat
cmdtime python whateverscript.py
```


# Developer Notes
## Why Bother With This?
For some machine learning projects, I use the Windows command prompt to execute scripts. I use Windows so that Tensorflow can access my PC's NVIDIA GPU. (Unfortunately, using Linux under VirtualBox can't access GPUs.)

In addition, there is no built-in equivalent of the Linux `time` utility in the Windows 10 command prompt. Yes, there are other options such as those discussed [here](https://stackoverflow.com/questions/673523/how-do-i-measure-execution-time-of-a-command-on-the-windows-command-line) and [here](https://www.raymond.cc/blog/measure-time-taken-to-complete-a-batch-file-or-command-line-execution/). But they either require installing old binaries that I'd rather avoid, or involve more cumbersome approaches. I wanted something where I can just prefix the command I want to run similar to the Linux `time` utility.

Hence the creation of this really trivial but useful Linux `time`-like utility which I'm calling `cmdtime`. And it's pure Python.

Probably someone else has already created such a utility under PyPi, but I couldn't find it.


## PyPI Notes
- Generate `tar.gz` that will be uploaded with `twine`:
```bat
python setup.py sdist
```

- [Work in development mode](https://packaging.python.org/guides/distributing-packages-using-setuptools/#working-in-development-mode):
```bat
python -m pip install --editable .
```

- Push to TestPyPI
```bat
python -m twine upload --repository testpypi dist/*
```

- Push to PyPI
```bat
python -m twine upload dist/*
```

## `pytest` Notes
Tests are written to support both Windows and Linux, although this utility is not really needed in Linux.

- Install `pytest`:
```bat
python -m pip install --upgrade pytest
```

- Local testing:
```bat
pytest -v
```

- Travis CI:
  - The tests only work on Python 3.7 or later as the `subprocess.run()` had significant changes in parameters (`capture_output`, `text`) not available in earlier versions. While it's possible to create version-specific test code to be compatible with earlier versions, it's not worth the effort...
  - Right now, Travis CI doesn't support Python on Windows. But using the method in this [gist](https://gist.github.com/shaypal5/7fd766933fb265af6f71a88cb91dd08c), we can install Python on Windows via Chocolatey. At present, I could only find Python 3.7.x and 3.8.x via [Chocolatey](https://chocolatey.org/packages/python3#versionhistory), so only those are tested.

## `terminalizer` Notes
The `gif` is rendered using [Terminalizer](https://terminalizer.com/) - great tool!.

Notes on configuration changes in [`cmdtimedemo.yml`](img/cmdtimedemo.yml) to adjust the rendered `gif`:
- Change `command` option from `null` to `cmd.exe` so that PowerShell is not used under Windows.
- Change `type` to `solid`. (`null` doesn't look good, and the other options make it look like a Mac.)
- Change `title` under `frameBox` to `null` to avoid seeing `Terminalizer` as the window heading in the resulting gif.
