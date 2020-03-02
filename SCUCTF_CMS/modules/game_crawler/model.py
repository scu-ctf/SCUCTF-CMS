from django.db.models import Model, TextField, IntegerField, DateField


# Use class Model to manage database

class GameInformation(Model):
    id = IntegerField(primary_key=True)  # 标识符
    name = TextField(null=False)  # 比赛名称
    type = TextField(null=False)  # 比赛类型
    hyperlink = TextField()  # 报名链接
    date = DateField(null=False)
    pic_addr = TextField(null=False)
    location = TextField(null=False)
