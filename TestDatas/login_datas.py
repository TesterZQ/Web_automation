

#登录成功数据

succ_data = {"user":"18684720553","password":"python"}


#登录异常数据、密码为空，用户名为空，用户名不规范
datas=[
    {"user":"18684720553","password":"","check":"请输入密码"},
    {"user":" ","password":"python","check":"请输入手机号"},
    {"user":"186847","password":"python","check":"请输入正确的手机号"}
]


#异常用例：从未注册过的账户/密码错误
wrong_datas = [
    {"user":"18684720553","password":"123","check":""},
    {"user":"18600000000","password":"python","check":"xxxx"},
]
