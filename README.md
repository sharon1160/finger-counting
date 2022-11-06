## Get ready!

Use a virtual environment.

```sh
❯ python3 -m venv .venv
❯ source .venv/bin/activate
```

Install packages.

```sh
.venv ❯ pip install -r requirements.txt
```

## Run

```sh
.venv ❯ python main.py
```

## Help

List serial devices

```sh
.venv ❯ python -m serial.tools.list_ports
```
