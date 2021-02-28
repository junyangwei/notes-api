"""
自定义业务异常类
示例:
from note_api.common.errors.biz_error import BizError
from note_api.common.errors.biz_status import biz_status as BizStatus

raise BizError(BizStatus['FAIL']) #打印 {"code":-1,"msg":"失败","data":null}
raise BizError(msg='测试')        #打印 {"code":-1,"msg":"测试","data":null}
"""
class BizError(Exception):
    """业务异常类"""
    def __init__(self, biz_status={}, msg=None):
        """初始化异常类默认属性"""
        self.code = -1
        self.msg = msg

        # 如果存在code和msg属性，则直接赋值
        if 'code' in biz_status:
            self.code = biz_status['code']
        if 'msg' in biz_status:
            self.msg = biz_status['msg']