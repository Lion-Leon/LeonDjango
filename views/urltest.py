#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/6/6 17:17
# @Author: Arenas
# @Blog  : www.zccie.com

from django.shortcuts import render_to_response

def urltest(request):
	return render_to_response('urltest.html')