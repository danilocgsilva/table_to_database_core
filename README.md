# Table to database

Convert a database file.

Packages required:

* pyexcel_ods
* ods
* pandas
* pymysql
* mysql-connector-python
* sqlalchemy

This packages uses the `pyexcel_ods` package to create ods files por testing.

Check the package usage: [docs/USAGE_GUIDE.md](docs/USAGE_GUIDE.md)

## Testing

The unit tests (actually, integration tests) uses real databse connection. It is expected that variables like

* `TEST_DB_USER`
* `TEST_DB_PASSWORD`
* `TEST_DB_HOST`

exists in the environment, and corresponds to a real database.

## What could be worth seeing happen?

The test `table_to_database_core/tests/test_SqlWritterFromExcel.py`, with method `test_create_two_tables` shows how to use the `pyexcel_ods` package to create an ods file with several spreadsheets.

File `table_to_database_core/table_to_database/SqlWritterFromExcel.py`, with the `write` method shows how to deal with an spreadhseet file with several spreadheets within.

