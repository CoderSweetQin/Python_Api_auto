#获取base url
def get_base_url(case):
    if case=="user":
        base_url="http://user.api.com"
    if case=="tx":
        base_url="http://tx.api.com"
    if case=="gateway":
        base_url="https://gateway.api.com"
    return base_url

##登录url
login_url="/api/user/login"