# 共用的工具类

import functools
from flask import current_app
from flask import g
from flask import session

from info.models import User


def do_index_class(index):


    if index == 0:
        return 'first'

    elif index == 1:
        return 'second'

    elif index == 2:
        return 'third'

    return ''

def user_login_data(f):

    @functools.wraps(f)

    def wrapper(*args,**kwargs):

        user_id = session.get("user_id", None)

        user = None

        if user_id:
            try:
                user = User.query.get(user_id)
            except Exception as e:
                current_app.logger.error(e)
        g.user = user
        return f(*args,**kwargs)

    return wrapper

# def query_user_data():
#
#     user_id = session.get("user_id", None)
#
#     user = None
#
#     if user_id:
#         try:
#             user = User.query.get(user_id)
#         except Exception as e:
#             current_app.logger.error(e)
#         return user
#     return None