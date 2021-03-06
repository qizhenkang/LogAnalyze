#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
 Create On: November 01, 2016
    Author: corvo
"""

from sqlalchemy import Column, Integer, Boolean, VARCHAR, DateTime, ForeignKey
from databases.db import Base


class DayLogAnalyze(Base):
    """
    每日日志重要信息记录
    """
    __tablename__     = "DayLogAnalyze"
    id                = Column(Integer        , nullable = False                            , primary_key = True)
    date              = Column(VARCHAR(32)    , nullable = False) # 表项名称access_api.log-date
    api_order         = Column(VARCHAR(10800) , nullable = False) # 该日Api请求数目(保留前20)
    ip_order          = Column(VARCHAR(10800) , nullable = False) # 该日ip请求数目(保留前30)
    every_hour_count  = Column(VARCHAR(1024)  , nullable = False) # 该日每小时访问量
    device_distribute = Column(VARCHAR(10800) , nullable = False) # 该日发送请求的设备分布
    call_count        = Column(Integer        , nullable = False) # 该日请求次数
    ip_count          = Column(Integer        , nullable = False) # 该日请求ip数
    ios_version       = Column(VARCHAR(10800) , nullable = True)  # ios设备版本分布
    android_version   = Column(VARCHAR(10800) , nullable = True)  # android设备版本分布



