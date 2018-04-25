# 所有的视图函数
from _warnings import filters

from flask import current_app, jsonify
from flask import render_template
from flask import request
from flask import session

from info import constants
from info.models import User, News, Category
from info.utils.response_code import RET
from . import index_blu
from info import redis_store

@index_blu.route('/news_list')
def news_list():

    cid = request.args.get('cid','1')
    page = request.args.get('page','1')
    per_page = request.args.get('per_page','10')

    try:
        page = int(page)
        cid = int(cid)
        per_page = int(per_page)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR,errmsg='参数')

    filters = []
    if cid != 1:
        filters.append(News.category_id == cid)
    try:
        paginate = News.query.filter(*filters).order_by(News.create_time.desc()).paginate(page,per_page,False)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR,errmsg='数据查询错误')

    news_list = paginate.items

    total_page = paginate.pages

    current_page = paginate.pages

    news_dict_li = []
    for news in news_list:
        news_dict_li.append(news.to_basic_dict())

    data = {
        "total_page":total_page,
        "current_page":current_page,
        "news_dict_li":news_dict_li
    }
    return jsonify(errno=RET.OK,errmsg='OK',data = data)


@index_blu.route('/')
def index():
    user_id = session.get('user_id',None)
    user = None
    if user_id:
        try:
            user = User.query.get(user_id)
        except Exception as e:
            current_app.logger.error(e)

    news_list = []
    try:
        news_list = News.query.order_by(News.clicks.desc()).limit(constants.CLICK_RANK_MAX_NEWS)
    except Exception as e:
        current_app.logger.error(e)

    news_dict_li = []

    for news in news_list:
        news_dict_li.append(news.to_basic_dict())

    categories = Category.query.all()

    category_li = []

    for category in categories:

        category_li.append(category.to_dict())

    data = {
        'user': user.to_dict() if user else None,
        'news_dict_li':news_dict_li,
        "categories":category_li
    }
    # session["name"] = "wanghaowei"
    # logging.debug('查看看debug')
    # logging.warning('查看看warning')
    # logging.error('查看看error')
    # logging.fatal('查看看fatal')
    # current_app.logger.error('查看看debug')
    # redis_store.set('name','wanghaowei')
    return render_template('news/index.html',data=data)

    # return 'index'
# 打开网页,默认打开根路径+favicon.ico加小图标
@index_blu.route('/favicon.ico')
def favicon():
    return current_app.send_static_file('news/favicon.ico')
