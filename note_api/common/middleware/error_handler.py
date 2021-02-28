from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from note_api.common.errors.biz_error import BizError

class ExceptionMiddleware(MiddlewareMixin):
    """全局异常处理中间件"""

    def process_exception(self, request, exception):
        """捕获处理"""

        if isinstance(exception, BizError):
            """自定义类异常拥有属性code和msg，按照业务异常抛错返回"""
            return self.fail(exception.code, exception.msg)

    def fail(self, code=-1, msg=''):
        """失败返回函数"""
        result = {
            'code': code,
            'msg': msg,
            'data': None,
        }
        return JsonResponse(result)