# import socket
#
# EOL1 = b'\n\n'
# EOl2 = b'\n\r\n'
# body = """Hello, world! <h1> from the5fire 《Django企业开发实战》</h1>。"""
# response_params = [
#     'HTTP/1.0 200 OK',
#     'Date: Sun, 27 may 2018 01:01:01 GMT',
#     'Content-Type: text/plain; charset=utf-8',
#     'Content-Length: {}\r\n'.format(len(body.encode())),
#     body,
# ]
#
# response = '\r\n'.join(response_params)
#
# def handle_connection(conn, addr):
#     request = b""
#     while EOL1 not in request and EOl2 not in request:
#         request += conn.recv(1024)
#     print(request)
#     conn.send(response.encode())
#     conn.close()
#
# def main():
#     serversocker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     serversocker.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     serversocker.bind(('127.0.0.1', 8000))
#     serversocker.listen(5)
#     print('http://127.0.0.1:8000')
#
#     try:
#         while True:
#             conn, address = serversocker.accept()
#             handle_connection(conn, address)
#     finally:
#         serversocker.close()
#
# if __name__ == '__main__':
#     main()


# def simple_app(environ, start_response):
#     status = '200 OK'
#     response_headers = [('Content-type', 'text/plain')]
#     start_response(status, response_headers)
#     return [b'Hello, world!']
#
# from django.contrib.admin.models import LogEntry, CHANGE
# from django.contrib.admin.options import get_content_type_for_model
# from typeidea.typeideaed.blog.models import Post
#
# post = Post.objects.get(id=1)
# log_entries = LogEntry.objects.filter(
#     content_type_id=get_content_type_for_model(post).pk,
#     object_id=post.id,
# )
# print(log_entries)

# import logging

# import time
# import functools
#
# CACHE = {}
#
# def cache_it(func):
#     @functools.wraps(func)
#     def inner(*args, **kwargs):
#         key = repr(*args, **kwargs)
#         print('key', key)
#         try:
#             result = CACHE[key]
#         except KeyError:
#             result = func(*args, **kwargs)
#             CACHE[key] = result
#         return result
#     return inner
#
# @cache_it
# def query(sql):
#
#     time.sleep(1)
#     result = 'execute %s' % sql
#     return result
#
#
# if __name__ == '__main__':
#     start = time.time()
#     query('SELECT * FROM blog_post')
#     print(time.time() - start)
#
#     start = time.time()
#     query('SELECT * FROM blog_post')
#     print(time.time() - start)



# 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
# https://github.com/wuxinpy/self-study