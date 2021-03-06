#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: timeline.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2016-12-13 15:41:50 (CST)
# Last Update: Tuesday 2018-11-06 13:52:22 (CST)
#          By:
# Description:
# **************************************************************************
from .views import AdminView
from maple.model import TimeLine
from maple.extension import db


class TimeLineView(AdminView):
    column_editable_list = ['is_hidden', 'user']
    column_filters = ['created_at', 'user']
    form_widget_args = {'content': {'rows': 10}}


def init_admin(admin):
    admin.add_view(
        TimeLineView(
            TimeLine,
            db.session,
            name='管理时间轴',
            endpoint='admin_timeline',
            category='管理博客'))
