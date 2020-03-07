# -*- coding: utf-8 -*-
# author：yaoyao time:2020/3/6

import redis

try:

    #1. 连接数据
    client = redis.StrictRedis(
        host='127.0.0.1',
        port=6379
    )
    # 2.增删改查 string
    data_key = 'strkey'
    result = client.set(data_key,'张三')
    print(result)

    check_data = client.get(data_key)
    print(check_data)

    delete_data = client.delete(data_key)
    print(delete_data)


    pass
except Exception as e:
    print(e)
    pass




