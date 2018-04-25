import random
import re
from datetime import datetime

from flask import abort, jsonify
from flask import current_app
from flask import make_response
from flask import request
from flask import session

from info import constants, db
from info import redis_store
from info.libs.yuntongxun.sms import CCP
from info.models import User
from info.utils.response_code import RET
from . import passport_blu
from  info.utils.captcha.captcha import captcha

@passport_blu.route('/logout')
def logout():

    session.pop('user_id', None)
    session.pop('mobile', None)
    session.pop('nick_name', None)

    return jsonify(errno=RET.OK,errmsg='退出登录')


@passport_blu.route('/login',methods=['POST'])
def login():
    # 获取参数
    params_dict = request.json
    mobile = params_dict.get('mobile')
    passport = params_dict.get('passport')

    # 校验参数
    if not all([mobile,passport]):
        return jsonify(errno=RET.PARAMERR,errmsg='参数错误')
    if not re.match('1[35678]\\d{9}',mobile):
        return jsonify(errno=RET.PARAMERR,errmsg='手机号格式不正确')

    # 校验密码是否正确
    try:
        user = User.query.filter(User.mobile ==mobile).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR,errmsg='数据查询错误')
    if not user:
        return jsonify(errno=RET.NODATA,errmsg='用户不存在')
    if not user.check_password(passport):
        return jsonify(errno=RET.PWDERR,errmsg='用户名或密码错误')


    session['user_id'] = user.id
    session['mobile'] = user.mobile
    session['nick_name'] = user.nick_name

    return jsonify(errno=RET.OK,errmsg='登录成功')

@passport_blu.route('/register',methods = ['POST'])
def register():
    param_dict = request.json
    # 获取参数
    mobile = param_dict.get('mobile')
    smscode = param_dict.get('smscode')
    password = param_dict.get('password')
    #校验参数
    if not all([mobile,smscode,password]):
        return jsonify(errno=RET.PARAMERR,errmsg='手机好歌是不对')
#     取到服务器保存的真实的验证码
    try:
        real_sms_code = redis_store.get('SMS_' + mobile)

    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.NODATA,errmsg='数据查询失效')
    if not real_sms_code:
        return jsonify(errno=RET.NODATA,errmsg='验证码已过期')

    if real_sms_code != smscode:
        return jsonify(errno=RET.DATAERR,errmsg='验证码输入错误')

    user = User()
    user.mobile = mobile
    user.nick_name = mobile
    user.last_login = datetime.now()

#     对密码做处理
    user.password = password


    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        return jsonify(errno=RET.DBERR,errmsg='数据保存失败')

    session['user_id'] = user.id
    session['mobile'] = user.mobile
    session['nick_name'] = user.nick_name

    # 设置当前最后一次登录时间
    user.last_login = datetime.now()

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)

    return jsonify(errno=RET.OK,errmsg='注册成功')

@passport_blu.route('/sms_code',methods = ['POST'])
def send_sms_code():
    # 获取参数,手机号,等内容
    params_dict = request.json
    mobile = params_dict.get('mobile')
    image_code = params_dict.get('image_code')
    image_code_id = params_dict.get('image_code_id')
    # 效验参数
    # 判断参数是否有值
    if not all([mobile,image_code,image_code_id]):
        return jsonify(errno=RET.PARAMERR,errmsg = '参数err')
    #校验手机号是否正确
    if not re.match('1[35678]\\d{9}',mobile):
        return jsonify(errno=RET.PARAMERR,errmsg='手机格式不对')
    # 从redis中取出真正的验证码内容
    try:
        real_image_code = redis_store.get('ImageCodeId_'+image_code_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR,errmsg='数据查询失败')

    if not real_image_code:
        return jsonify(errno = RET.NODATA,errmsg='图片验证已过期')

    if real_image_code.upper() != image_code.upper():
        return jsonify(errno=RET.DATAERR,errmsg='验证码输入错误')
    # 如果一致,生成短信验证内容
    sms_code_str = '%06d' % random.randint(0,99999)
    current_app.logger.debug('短信验证内容是: %s' % sms_code_str)
    # 发送短信验证码
    result = CCP().send_template_sms(mobile,[sms_code_str,constants.SMS_CODE_REDIS_EXPIRES / 5],'1')
    if result != 0:
        # 代表发送不成功
        return jsonify(errno=RET.THIRDERR,errmsg='短信发送失效')
    # 保存验证码内容到redis
    try:
        redis_store.set('SMS_'+mobile,sms_code_str)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR,errmsg='数据保存失败')
    #     告知发送结果
    return jsonify(errno=RET.OK,errmsg='发送成功')

@passport_blu.route('/image_code')
def get_image_code():
    # 1.取到参数
    image_code_id = request.args.get('imageCodeId')
    # 2.判断参数是否有值
    if not image_code_id:
        return abort(403)
    # 3.生成图片代码
    name,text,image = captcha.generate_captcha()

    current_app.logger.debug('图片验证内容是: %s ' %  text)

    try:
        redis_store.set('ImageCodeId_'+image_code_id,text,constants.IMAGE_CODE_REDIS_EXPIRES)
    except Exception as e:
        current_app.logger.error(e)
        abort(500)
    # 返回验证码图片
    response = make_response(image)
    response.headers['Content-Type'] = 'image/jpg'
    return response