# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 01:25:08 2021

@author: alishayzadag
"""

import glassdoor_scrapper22 as gs
import pandas as pd

path = "C:/Users/alishayzadag/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist', 5, False, path, 15)

