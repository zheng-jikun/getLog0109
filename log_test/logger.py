#!/usr/bin/env python
# -*- coding: utf-8 -*-

from getLogger import get_logger

import os, sys
sys.path.append(os.path.dirname(__file__))

logger = get_logger('store_data.log')
logger.info(f"\n----------------数据写入成功，正常退出------------------------")