## Env Setup

### reate virtual environment
```bash
python3 -m venv .nosync/venv && source .nosync/venv/bin/activate
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
### install package locally
```bash
pip install .
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