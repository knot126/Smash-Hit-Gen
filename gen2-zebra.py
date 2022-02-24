"""
Smash Hit Room Generator v2

Codename Zebra

This generator is based on a lite-weight, non-conditional set of rules about
where objects should be placed. Prefab-like elements start as being placed in
spots in the level where they are allowed to be, then they are actually built.

List of possible rules for mid segments:

  1. All segments must contain one obstacle and/or one or two crystal obstacles.
     a. If the segment contains obstacles, they must be within CollisionAccuracy 
        radius of the player's centre point (which is always [0.0 1.0 -z]). 
     b. If a segment contains crystals, they must be within the LevelLimits.
     c. If a segment contains crystals AND it contains an obstacle, then the
        crystals shall not appear in the CollisionAccuracy radius.
  
  2. All segments must have zero or more stone walls outside LevelLimits.
     a. If a segment has walls, they must be well aligned to the boundaries and
        may be decorated like walls in Smash Hit.
  
  3. All segment must have decorative stone and possibily decals outside of the
     CollisionAccuracy radius from the player centre.
     a. If a segment contains more than one decoration, then it must not
        intersect another decoration.
     b. For any decoration, it should be true that it does not intersect with
        any other entities.
     I. Decorations shall be created only in empty space to avoid violation of
        rules 3a and 3b.
""" 

from smashhitbuilder import *
import random
import typing

class Top: pass
class Bottom: pass
class Left: pass
class Right: pass

class LevelStructure:
	"""
	A collection of variables controling the structure and properties of a
	level.
	"""
	
	def __init__(self):
		pass

def main():
	pass

if (__name__ == "__main__"):
	main()
