# Python CI example

A minimal Python package whose tests run automatically in GitHub Actions on
every push and pull request.

## Run locally

Create a virtual environment and install the project:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
python -m pytest
```

The workflow in `.github/workflows/ci.yml` runs the same test command on
Python 3.10 through 3.13.
