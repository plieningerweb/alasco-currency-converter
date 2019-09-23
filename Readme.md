# Flask Currency Converter

Convert currency between Euro, USD and Yen.

## Install & Run

```bash
pip install -r requirements.txt
# edit environment config (change secret key!)
cp .env.example .env

# run linter and tests
flake8
pytest

# run app
flask run
```

# Todo

- Split requirements into dev and prod
- No assumtion made about environment management, e.g. conda or pipenv
- Combine setup, test and other commands into flask command
- Export requirements again into txt file
- Extend form to validate more, add tests
- Add ability to generate docs