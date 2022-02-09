# -*- encoding=utf8 -*-
__author__ = "OS"

from airtest.core.api import *
from poco.drivers.cocosjs import CocosJsPoco
poco = CocosJsPoco()
auto_setup(__file__)
# a = poco("ebCheatGold").click()
touch(Template(r"tpl1632747563641.png", record_pos=(0.001, 0.15), resolution=(1600, 900)))

