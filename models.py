import peewee as pw


db = pw.PostgresqlDatabase(
    'postgres',
    user='postgres',
    password='postgres',
    host='db',
    port='5432'
)


class BaseModel(pw.Model):
    class Meta:
        database = db
