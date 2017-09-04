#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore import client
from aliyunsdkrds.request.v20140815 import DescribeBackupPolicyRequest

clt = client.AcsClient('<accessKeyId>','<accessSecret>','cn-hangzhou')

# 设置参数
request = DescribeBackupPolicyRequest.DescribeBackupPolicyRequest()
request.set_accept_format('json')

request.add_query_param('DBInstanceId', 'rm-2ze00tnh50cxx6387')

# 发起请求
response = clt.do_action(request)

# 输出结果
print response
