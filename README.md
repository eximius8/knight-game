# Игра "Герой и чудовища"

## Проверки качества кода

flake8

```
flake8 --max-line-length=120 main.py
```

pep257

```
pep257 main.py
```
mypy

```
mypy main.py --disallow-untyped-calls --disallow-untyped-defs --disallow-incomplete-defs --check-untyped-defs  --disallow-untyped-decorators --ignore-missing-imports --pretty
```

