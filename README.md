# rankings

Algorithms for matching Mentors to Mentees.

## Running

[Currently](#TODO), this expects a data file in `data/testdata9.xlsx`, and to be run from `src`:

```
cd src/
pipenv install
pipenv run python -m stable_mentor
```

## Testing

Run these from the repo root (where this README is):

```
pipenv install --dev
pipenv run pytest tests
```

## TODO
* [*] Remove global vars
* [*] Add test framework
* [ ] Add tests
* [ ] add CI
* [ ] Add license
* [ ] Take data path at command line
