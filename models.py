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


class Messages(BaseModel):
    id = pw.PrimaryKeyField(null=False)
    message = pw.CharField(max_length=100)
    user = pw.CharField(max_length=100)
    #dis_id = pw.IntegerField(default=123)
    dis_id_str = pw.CharField(max_length=100)

    created_at = pw.DateTimeField(default=pw.datetime.datetime.now())
    updated_at = pw.DateTimeField(default=pw.datetime.datetime.now())


