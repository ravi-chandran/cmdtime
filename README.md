[![Build Status](https://travis-ci.org/ravi-chandran/cmdtime.svg?branch=master)](https://travis-ci.org/ravi-chandran/cmdtime)

# cmdtime
- Similar to the Linux `time` utility for measuring how long a command takes to run
- Useful for the Windows Command Prompt using pure Python.
- No point using this under Linux.
- No need to install Cygwin.

# Installation
- Requires Python 3.5+.
- Install from PyPi:

```bat
python -m pip install cmdtime
```

# Usage Examples
- Time a Python script

```bat
cmdtime python whateverscript.py
```

- Time anything else

```bat
cmdtime dir
```

# Notes
For some machine learning projects, I use the Windows command prompt to execute scripts. I use Windows so that Tensorflow can access my PC's NVIDIA GPU. Unfortunately, using Linux under VirtualBox can't access GPUs.

Unfortunately, there is no built-in equivalent of the Linux `time` utility in the Windows 10 command prompt. Yes, there are other options such as those discussed [here](https://stackoverflow.com/questions/673523/how-do-i-measure-execution-time-of-a-command-on-the-windows-command-line) and [here](https://www.raymond.cc/blog/measure-time-taken-to-complete-a-batch-file-or-command-line-execution/). But they either require installing old binaries that I'd rather avoid, or involve more cumbersome approaches. I wanted something where I can just prefix the command I want to run with the equivalent of `time`.

Hence the creation of this really trivial but useful Linux `time`-like utility which I'm calling `cmdtime`. And it's pure Python.

Probably someone else has already created such a utility under PyPi, but I couldn't find it.


## Developer Notes
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

## Testing Notes
```bat
python -m pip install --upgrade pytest
pytest -v
```