"""
Year 1 Programming 1 Final Project
Script for player 2
Jack Pearson
"""
# Imports all scripts and modules used for the game

import importlib.util
import sys
spec = importlib.util.spec_from_file_location("pygame", "Scripts/pygame")
foo = importlib.util.module_from_spec(spec)
sys.modules["module.name"] = foo
spec.loader.exec_module(foo)

import character_script
import player_1_script
import player_2_script
import scene_script

foo.init()