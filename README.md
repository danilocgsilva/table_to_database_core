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

## Testing

The unit tests (actually, integration tests) uses real databse connection. It is expected that variables like

* `TEST_DB_USER`
* `TEST_DB_PASSWORD`
* `TEST_DB_HOST`

exists in the environment, and corresponds to a real database.
