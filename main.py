# ------------------------------------------------------------------------------
# Copyright © 2017 Daniil Nepryahin
# contacts: <nervoidaz@yandex.ru>
# License: https://opensource.org/licenses/cpl1.0.php
# ------------------------------------------------------------------------------


# Neuralturer game
# Main file
from AdFuncFile import *
# start game
Hero, Inventory, Params = MainMenu()
# show City menu (Hero and Inventory exist)
PlaceMenu(Hero, Inventory, Params)
# It's all :D
