#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore import client
from aliyunsdkrds.request.v20140815 import CreateBackupRequest

clt = client.AcsClient('id','key','cn-hangzhou')

# 设置参数
request = CreateBackupRequest.CreateBackupRequest()
request.set_accept_format('json')

request.add_query_param('DBInstanceId', 'rm-2ze00tnh50cxx6387')
request.add_query_param('DBName', 'cepingdb')
request.add_query_param('BackupRetentionPeriod', '7')

# 发起请求
response = clt.do_action(request)

# 输出结果
print response
