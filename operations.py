import peewee
from models import *


def add_message(dis_id, message, author):
    row = Messages(
        dis_id_str="{}".format(dis_id),
        message=message.strip()+"qwe",
        user=author
    )
    row.save()


def find_message(dis_id):
    return Messages.get("{}".format(dis_id)==Messages.dis_id_str)
