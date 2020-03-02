from django.db.models import Model, CharField, DateTimeField, IntegerField,ForeignKey


class InvitationCode(Model):
    id = IntegerField(primary_key=True)  # 唯一标识符
    from_uid=ForeignKey()