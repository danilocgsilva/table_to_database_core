import os
from table_to_database.Utils import Utils

class TearDownMethods:
    def _tearDown(self):
        if self.generatedOds and os.path.exists(self.generatedOds):
            os.remove(self.generatedOds)
        if self.generatedDatabase:
            Utils.drop_database(self.generatedDatabase, self.mySqlDriver)
