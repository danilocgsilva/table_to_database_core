import unittest
import xmlrunner
from table_to_database.Utils import Utils

if __name__ == "__main__":
    suite = unittest.TestLoader().discover("tests")
    xmlrunner.XMLTestRunner(output=f"reports/{Utils.generate_friendly_date_string()}").run(suite)

