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

### Environment variables

Copy .env.example to .env for configuration variables.

- Get your arduino port with the following command: `python -m serial.tools.list_ports`

## Run

```sh
.venv ❯ python main.py
```
