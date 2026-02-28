# Vibe Mini

A mini version of the vibe project implementing Rock-Paper-Scissors.

## Installation

Install the project in editable mode with its dependencies:

```bash
pip install -e .
```

## Running Tests

Run the project's tests using `pytest`:

```bash
pytest
```

## Running the Demo

You can run the Rock-Paper-Scissors game demo from the command line:

```bash
python -m vibe_mini.cli rock scissors
```

Other move combinations:

```bash
python -m vibe_mini.cli paper rock
python -m vibe_mini.cli scissors paper
python -m vibe_mini.cli rock rock
```

The only valid moves are `rock`, `paper`, and `scissors`.
