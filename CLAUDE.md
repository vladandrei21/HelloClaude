# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Environment

- Python 3.9, virtual environment at `.venv/`
- Activate with `source .venv/bin/activate`

## Running scripts

```bash
python main.py
python sum.py
python factorial.py
```

## Project structure

Small Python learning/utility project with standalone scripts:

- `main.py` — PyCharm-generated entry point with a `print_hi` function
- `sum.py` — `calculate_sum(numbers)` utility; runs with a hardcoded list when executed directly
- `factorial.py` — recursive `factorial(n)` with user input prompt; raises `ValueError` for negative inputs