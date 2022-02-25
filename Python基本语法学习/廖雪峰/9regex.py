#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

print('Test: 010-12345')
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(1), m.group(2))

t = '19:05:30'
print('Test:', t)
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())


urls = re.findall('.*VID_[0-9]{8}_[0-9]{6}', 'VID_20200727_142136_00_062.mp4')
#urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', 'https://www.yiibai.com/python_text_processing/python_extract_url_from_text.html')
print(urls)
if len(urls) == 0:
  print('error')

print(urls[0])
