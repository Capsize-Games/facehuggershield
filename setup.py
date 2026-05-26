from pathlib import Path

from setuptools import find_packages, setup


README = Path("README.md").read_text(encoding="utf-8")
VERSION = "1.0.0"


setup(
    name="facehuggershield",
    version=VERSION,
    author="Capsize LLC",
    description=(
        "Standalone privacy and sandbox controls for Hugging Face "
        "and related Python runtimes"
    ),
    long_description=README,
    long_description_content_type="text/markdown",
    keywords=(
        "privacy, security, huggingface, sandbox, darklock, "
        "nullscream, shadowlogger"
    ),
    license="GPL-3.0",
    author_email="contact@capsizegames.com",
    url="https://github.com/Capsize-Games/facehuggershield",
    package_dir={"": "src"},
    packages=find_packages("src"),
    python_requires=">=3.10",
    install_requires=[],
)
