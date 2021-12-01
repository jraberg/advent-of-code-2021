from pathlib import Path


def read_data(filename: str) -> str:
    file = Path(__file__).parent.parent.absolute() / 'input' / filename
    with open(file, encoding="utf-8") as f:
        return f.read()
