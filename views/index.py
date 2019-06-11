#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/6/6 17:17
# @Author: Arenas
# @Blog  : www.zccie.com

from django.shortcuts import render_to_response

def index(request):
	return render_to_response('index.html')