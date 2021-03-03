"""返回业务码及信息定义"""

biz_status = {
    # 成功返回码及信息
    'SUCCESS': { 'code': 0, 'msg': '成功' },

    # 常规类错误码及错误信息
    'FAIL': { 'code': -1, 'msg': '失败' },
    'PARAM_EMPTY': { 'code': -2, 'msg': '数据为空' },
    'PARAM_ERROR': { 'code': -3, 'msg': '参数错误' },

    # 业务类错误信息
    'USER_PASSWORD_ERROR': {
        'code': 1001, 'msg': '用户不存在，或账号密码错误，请确认后再尝试'}
}
