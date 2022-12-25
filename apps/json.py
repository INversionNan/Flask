from flask import jsonify, Response
from activate import app

class JSONResponse(Response):

    @classmethod
    def force_type(cls, response, environ=None):
        """
        这个方法只有视图函数返回非字符、非元祖、非Response对象才会调用
        :param response:是视图函数的返回值
        :param environ:
        :return:
        """
        print(response)
        print(type(response))
        if isinstance(response, (list, dict)):
         # jsonify除了将字典转换成json对象，还将对象包装成了一个Response对象
        response = jsonify(response)
        return super(JSONResponse, cls).force_type(response, environ)

app.response_class = JSONResponse