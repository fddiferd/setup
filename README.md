## Env Setup

### reate virtual environment
```bash
python3 -m venv .venv && source .venv/bin/activate
```

### install requirements
```bash
pip install -r requirements.txt
```

### copy .env.example
```bash
cp .env.example .env
```

## Package Dist
### setup.py
```python
from setuptools import setup, find_packages
setup(
    name="my_project",          # Replace with your project name
    version="0.1.0",
    packages=find_packages(),   # Automatically includes packages (like `src`)
    install_requires=[],        # Add project dependencies here
)
````
### install package locally
```bash
pip install -e .
```

## GitHub
### force a reconcile merge
```bash
git push origin main --force
```
### clone repo
```bash
git clone https://github.com/fddiferd/setup.git
```
