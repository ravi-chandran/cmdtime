# cmdtime
Similar to the Linux `time` utility useful for the Windows Command Prompt using pure Python.

# Installation
Requires Python 3.
`python -m pip install cmdtime`

# Usage Examples
- Time a Python script
```
cmdtime python whateverscript.py
```

- Time anything else
```
cmdtime dir
```

# Notes
For some machine learning projects, I use the Windows command prompt to execute scripts. (I use Windows so that I can set Tensorflow up to use the NVIDIA GPU. Unfortunately, VirtualBox doesn't have a way to access GPUs, so running the scripts under Linux is slower for me.)

Unfortunately, there is no built-in equivalent of the Linux `time` utility in the Windows 10 command prompt. Yes, there are other options such as those discussed [here](https://stackoverflow.com/questions/673523/how-do-i-measure-execution-time-of-a-command-on-the-windows-command-line) and [here](https://www.raymond.cc/blog/measure-time-taken-to-complete-a-batch-file-or-command-line-execution/). But they either require installing old binaries that I'd rather avoid, or involve more cumbersome approaches. I wanted something where I can just prefix the command I want to run with the equivalent of `time`.

Hence the creation of this really trivial but useful equivalent of Linux `time` which I'm calling `cmdtime`. And it's pure Python.

(Try finding a unique, meaningful name in PyPi... Probably someone else has already created such a utility under PyPi, but I couldn't find it.)


# Developer Notes
```bat
python setup.py sdist

```
- [Work in development mode](https://packaging.python.org/guides/distributing-packages-using-setuptools/#working-in-development-mode):
```bat
python -m pip install -e .
```