# -*- coding: utf-8 -*-
__author__ = "hank"

import unittest
import sys
sys.path.append("../")
from lib.analysis_data import AnalysisData
from lib.read_config import ReadConfig

body_json = ReadConfig().read_json("code_list.json")
first_dict = body_json["first_team"]
second_dict = body_json["second_team"]
first_dict.update(second_dict)
print(first_dict)

class TestMA250WithValues(unittest.TestCase):
    def test_ma250_with_values(self):
        pass