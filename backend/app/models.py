from peewee import CharField, IntegerField, MySQLDatabase, Model, ForeignKeyField

MYSQL_DB = 'homework'
MYSQL_HOST = 'db'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASS = 'root'

db = MySQLDatabase(MYSQL_DB, host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASS)
db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    class Meta:
        db_table = 'user'

    id = IntegerField()
    username = CharField()
    password = CharField()


class Blog(BaseModel):
    class Meta:
        db_table = 'blog'

    id = IntegerField()
    name = CharField()
    category = CharField()
    status = IntegerField()
    content = CharField()
    author_id = ForeignKeyField(User, field='id')
