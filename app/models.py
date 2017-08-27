# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from distribution.db import TimestampedModel

# Create your models here.


class Products(TimestampedModel):
    name = models.CharField(u'名称', max_length=128, blank=True, null=True)
    remark = models.CharField(u'描述', max_length=512, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Area(TimestampedModel):
    name = models.CharField(u'名称', max_length=128, blank=True, null=True)
    remark = models.CharField(u'描述', max_length=512, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Sales(TimestampedModel):
    """ 销售信息
    """
    name = models.CharField(u'销售名称', max_length=128, blank=True, null=True)
    address = models.CharField(u'地址', max_length=256, blank=True, null=True)
    email = models.CharField(u'邮件地址', max_length=128, blank=True, null=True)
    phone = models.CharField(u'联系电话', max_length=256, blank=True, null=True)
    # 
    remark = models.CharField(u'描述', max_length=512, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Custom(TimestampedModel):
    """ 客户表信息
    """
    name = models.CharField(u'客户名称', max_length=128, blank=True, null=True)
    address = models.CharField(u'地址', max_length=256, blank=True, null=True)
    email = models.CharField(u'邮件地址', max_length=128, blank=True, null=True)
    phone = models.CharField(u'联系电话', max_length=256, blank=True, null=True)
    # 
    remark = models.CharField(u'描述', max_length=512, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Engineer(TimestampedModel):
    """ 工程师信息
    """
    GENDER = (
        (0, u'女士'),
        (1, u'男士'),
    )
    # 
    name = models.CharField(u'姓名', max_length=128, blank=True, null=True)
    phone = models.CharField(u'手机', max_length=128, blank=True, null=True)
    email = models.CharField(u'邮件地址', max_length=128, blank=True, null=True)
    rank = models.CharField(u'职级', max_length=128, blank=True, null=True)
    gender = models.IntegerField(u'性别', choices=GENDER, null=True)
    cum_score = models.FloatField(u'累计积分', default=0, null=True)
    cur_score = models.FloatField(u'当前积分', default=0, null=True)
    # 
    remark = models.CharField(u'描述', max_length=512, blank=True, null=True)

    def __unicode__(self):
        return self.name


class TicketTemplate(TimestampedModel):
    """ 工单模板
    """
    TLEVEL = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    )
    # 
    type_1 = models.CharField(u'分类I', max_length=128, blank=True, null=True)
    type_2 = models.CharField(u'分类II', max_length=128, blank=True, null=True)
    type_3 = models.CharField(u'分类III', max_length=128, blank=True, null=True)
    type_4 = models.CharField(u'分类VI', max_length=128, blank=True, null=True)
    score = models.FloatField(u'分值', default=0, null=True)
    level = models.CharField(u'工单级别', max_length=8, choices=TLEVEL, null=True)
    # 
    remark = models.CharField(u'描述', max_length=512, blank=True, null=True)

    def __unicode__(self):
        return self.type_4


class Ticket(TimestampedModel):
    """ 工单表信息
    """
    TSTATUS = (
        (0, u'已设计'),
        (1, u'已分派'),
        (2, u'处理中'),
        (3, u'已完成'),
        (4, u'已关闭'),
        (5, u'已取消'),
    )
    # 
    ticket_id = models.CharField(u'工单号', max_length=32, unique=True)
    pro_name = models.CharField(u'项目名称', max_length=128, blank=True, null=True)
    engineer = models.ForeignKey(Engineer, null=True)
    sale = models.ForeignKey(Sales, null=True)
    custom = models.ForeignKey(Custom, null=True)
    ticket_temp = models.ForeignKey(TicketTemplate, null=True)
    products = models.ForeignKey(Products, null=True)
    areas = models.ForeignKey(Area, null=True)
    status = models.SmallIntegerField(u'工单状态', choices=TSTATUS, default=0)
    score = models.FloatField(u'分值', default=0, null=True)
    report = models.CharField(u'服务内容', max_length=1024, blank=True, null=True)
    trouble_report = models.CharField(u'故障报告', max_length=128, blank=True, null=True)
    knowledge_report = models.CharField(u'知识库', max_length=128, blank=True, null=True)
    # 
    service_start = models.DateField(u'服务开始时间', blank=True, null=True)
    service_end = models.DateField(u'服务结束时间', blank=True, null=True)
    # 
    remark = models.CharField(u'描述', max_length=512, blank=True, null=True)

    def __unicode__(self):
        return self.ticket_id