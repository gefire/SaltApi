# SaltApi
salt http api 类

# 使用示例
```
# -*- coding: utf-8 -*-
from SaltApi.SaltApi import SaltApi
import pprint

salt_host="https://localhost:8080"
salt_user="salt"
salt_passwd="salt"
api = SaltApi(salt_host, salt_user, salt_passwd)
print(api.run("test.ping", "*"))
```
