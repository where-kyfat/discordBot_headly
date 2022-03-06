"""Models template file

Contains db models information

"""

import peewee as pw
from configs.config import DB


# Database cursor
db = pw.PostgresqlDatabase(DB)


# Abstract database model
class BaseModel(pw.Model):
    class Meta:
        database = db
