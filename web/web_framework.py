import socket
"""
HTTP
四大特性
1.基于请求响应
2.应用层协议
3.无状态
4.短/无链接

数据格式
请求：
请求行
请求头

请求体

响应：
一样

响应状态码
1xx
2xx 200请求成功
3xx 302请求重定向
4xx 404请求收到，但数据不存在
5xx 500请求收到，服务器内部错误


b'GET / HTTP/1.1\r\n
Host: 127.0.0.1:8081\r\n
Connection: keep-alive\r\n
sec-ch-ua: "Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"\r\n
sec-ch-ua-mobile: ?0\r\n
Upgrade-Insecure-Requests: 1\r\n
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36\r\n
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n
Sec-Fetch-Site: none\r\n
Sec-Fetch-Mode: navigate\r\n
Sec-Fetch-User: ?1\r\n
Sec-Fetch-Dest: document\r\n
Accept-Encoding: gzip, deflate, br\r\n
Accept-Language: zh-CN,zh;q=0.9\r\n
\r\n'

"""

server = socket.socket()  # TCP 三次握手四次挥手
server.bind(('127.0.0.1', 8081))  # IP 以太网协议
server.listen(5)  # 池

while True:
    conn, addr = server.accept()
    data = conn.recv(1024)
    print(data)  # 请求信息
    path = data.decode().split(' ')[1]

    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    if path == '/index':
        with open('templates/index.html', 'rb') as f:
            conn.send(f.read())
    elif path == '/login':
        pass

    conn.close()

