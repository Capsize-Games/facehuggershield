# FacehuggerShield

FacehuggerShield is a standalone Python package for locking down
Hugging Face and similar runtimes before they can phone home,
download arbitrary code, or write outside approved paths.

Version `1.0.0` is the first standalone release extracted from
AIRunner. It includes the bundled `darklock`, `defendatron`,
`nullscream`, and `shadowlogger` modules that AIRunner previously
carried as vendored code.

![img.png](img.png)

[![Upload Python Package](https://github.com/Capsize-Games/facehuggershield/actions/workflows/python-publish.yml/badge.svg)](https://github.com/Capsize-Games/facehuggershield/actions/workflows/python-publish.yml)

## Install

Install the tagged release directly from GitHub:

```bash
pip install \
	"facehuggershield @ https://github.com/Capsize-Games/facehuggershield/archive/refs/tags/v1.0.0.tar.gz"
```

## Usage

Activate FacehuggerShield before importing the libraries you want to
contain:

```python
from facehuggershield.huggingface import activate

activate(
		activate_shadowlogger=True,
		darklock_os_allow_network=False,
)
```

The default Hugging Face settings disable telemetry, prefer offline
operation, and route cache data to a user-scoped FacehuggerShield
cache directory.

## What ships in this repo

- `facehuggershield.huggingface`: Hugging Face-specific activation and environment controls.
- `facehuggershield.darklock`: Filesystem and network restriction helpers.
- `facehuggershield.nullscream`: No-op module replacement for blocked imports.
- `facehuggershield.shadowlogger`: Log interception and shadow logging.
- `facehuggershield.defendatron`: Coordinator that wires the subsystems together.

## Extending to other libraries

To create a policy pack for another runtime, copy the
`facehuggershield/huggingface` package as a starting point and replace
its environment and blacklist settings with the rules your target
library needs.
