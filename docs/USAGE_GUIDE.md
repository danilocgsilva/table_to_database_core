# ToDatabase Usage Guide

## Quick Start

### 1. Setup
```python
from table_to_database.Facade.ToDatabase import ToDatabase
from table_to_database.ToDatabaseCore import ToDatabaseCore
from table_to_database.MySqlConfiguration import MySqlConfiguration

# Create ToDatabase instance
toDatabase = ToDatabase(ToDatabaseCore())
```

### 2. Configure Database Connection
```python
# Set up database configuration
database_configuration = MySqlConfiguration()
database_configuration.user = "your_db_user"
database_configuration.password = "your_db_password" 
database_configuration.host = "your_db_host"

# Apply configuration
toDatabase.set_database_configuration(database_configuration)
```

### 3. Import Data
```python
# Import ODS file to database
ods_file_path = "your_file.ods"
database_name = "your_database_name"

results = toDatabase.to_database(ods_file_path, database_name)
```

## Complete Example
```python
from table_to_database.Facade.ToDatabase import ToDatabase
from table_to_database.ToDatabaseCore import ToDatabaseCore
from table_to_database.MySqlConfiguration import MySqlConfiguration

# Initialize
toDatabase = ToDatabase(ToDatabaseCore())

# Configure database
config = MySqlConfiguration()
config.user = "myuser"
config.password = "mypassword"
config.host = "localhost"
toDatabase.set_database_configuration(config)

# Import data
results = toDatabase.to_database("data.ods", "my_database")
print(f"Created database: {results.database_created}")
```

For further ways to use the ToDatabase, you can check the testing file: `tests/test_ToDatabase.py`.
