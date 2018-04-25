from flask import abort
from flask import current_app
from flask import g
from flask import render_template
from flask import session

from info import constants
from info.models import News, User
from info.modules.news import news_blu
from info.utils.common import user_login_data

#
# @news_blu.route('/comment/<int:news_id>')
# @user_login_data
# def comment_news(news_id):
#     pass

@news_blu.route('/<int:news_id>')
@user_login_data
def news_detail(news_id):

    user = g.user

    news_list = []
    try:
        news_list = News.query.order_by(News.clicks.desc()).limit(constants.CLICK_RANK_MAX_NEWS)
    except Exception as e:
        current_app.logger.error(e)

    news_dict_li = []

    for news in news_list:
        news_dict_li.append(news.to_basic_dict())

    news = None

    try:
        news = News.query.get(news_id)

    except Exception as e:

        current_app.logger.error(e)

    if not news:
        abort(404)
    # 更新新闻点击次数
    news.clicks += 1

    data = {
        "user":user.to_dict() if user else None,
        "news_dict_li":news_dict_li,
        "news": news.to_dict()
    }

    return render_template('news/detail.html',data=data)