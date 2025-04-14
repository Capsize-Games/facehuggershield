# FacehuggerShield

FacehuggerShield automatically locks down operations
for specific modules. It was designed to non-destructively restrict access
to HuggingFace libraries, but can be used with any library.

---

![img.png](img.png)

[![Upload Python Package](https://github.com/Capsize-Games/facehuggershield/actions/workflows/python-publish.yml/badge.svg)](https://github.com/Capsize-Games/facehuggershield/actions/workflows/python-publish.yml)

---

## Usage

FacehuggerShield was specifically designed to override HuggingFace libraries, so the following examples show how to do that.


Install with HuggingFace libraries (or any other library you want to restrict).

```bash
pip install facehuggershield
```

Import in your application's main entry file (e.g. `main.py`), import `facehuggershield` before importing
any other libraries.

```python
from facehuggershield.huggingface import activate

activate()
```

Now you can use HuggingFace libraries without worrying about telemetry, networking or file writes.

---

## Settings

See the `activate` function in the [huggingface/__init__.py](https://github.com/Capsize-Games/facehuggershield/blob/master/src/facehuggershield/huggingface/__init__.py) file.

---

## How it works

FacehuggerShield uses [nullscream](https://github.com/Capsize-Games/nullscream) to intercept blacklisted modules and return Noop modules in their place.
The noop modules are empty classes with functions that return Magic noop classes.
The magic class functions in turn respond with Magic classes.

This allows anything on the blacklist to be importable, but not executable.

By overriding certain functions in HuggingFace libraries, FacehuggerShield is able to prevent the use of HuggingFace Hub.

FacehuggerShield also makes use of [darklock](https://github.com/Capsize-Games/darklock) to lock down network services, and [shadowlogger](https://github.com/Capsize-Games/shadowlogger) to intercept and reroute logs.

These libraries are combined under [defendatron](https://github.com/Capsize-Games/defendatron), a simple coordinator library.

FacehuggerShield contains all of the required settings for defendatron, as well as the best HuggingFace Library settings for privacy.

Although FacehuggerShield was specifically created to contain or nuke certain portions of the HuggingFace libraries, it can be configured to work with any library as it is simply a configuration wrapper around the previously mentioned modules which do the real work.

---

## How to add support for other libraries

If you want to add support for other libraries

1. Copy and paste the `huggingface` directory, name it after the library you're creating a configuration for
2. Modify all of the files in the new directory to fit your needs using the HuggingFace settings as your example
