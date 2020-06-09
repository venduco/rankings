# rankings

Algorithms for matching Mentors to Mentees.

## Running

Install runtime dependencies:

```
pipenv install
```

To process a data file (there is an example data file in `data/testdata9.xlsx`):

```
pipenv run python -m stable_mentor data/testdata9.xlsx
```

## Testing

Install dev dependencies (including all the runtime dependencies and pytest):

```
pipenv install --dev
```

Run the tests from the repo root (where this README is):

```
pipenv run pytest tests
```

It should report the number passed, and (if all is working) not report failures.

## TODO
* [*] Remove global vars
* [*] Add test framework
* [ ] Add tests
* [ ] add CI
* [ ] Add license
* [*] Take data path at command line
