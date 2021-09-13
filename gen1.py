#!/usr/bin/bash

import smashhitbuilder as sh
import random

Vec3 = sh.Vec3

integer = random.randint

def real():
	return ((2.0 * random.random()) - 1.0)

def ureal():
	return random.random()

def randbool():
	return random.choice([True, False])

def randtri():
	return random.choice([True, False, None])

TEMPLATE = "orange"
SEGMENT_TYPES = ["empty", "obstacle", "crystal", "powerup"]
ROOM_SEG_WALLS = Vec3(random.choice([3.5, 4.0, 5.0, 5.5, 6.0]), 4.0, random.choice([8.0, 12.0, 16.0]))
ROOM_SEG_SIZE = ROOM_SEG_WALLS * 2
ROOM_LENGTH = 140.0 + (ROOM_SEG_WALLS.z * 10.0)

# If the rooms should have walls or not (True or False) or if this should be per
# segment (None)
ROOM_SEG_WALL_TOP = randtri()
ROOM_SEG_WALL_BOTTOM = randtri()
ROOM_SEG_WALL_LEFT = randtri()
ROOM_SEG_WALL_RIGHT = randtri()

def Add_Walls(s, dem = Vec3(4.0, 8.0, 8.0)):
	# Walls
	# left
	if ((ROOM_SEG_WALL_LEFT == None and randbool()) or ROOM_SEG_WALL_LEFT):
		s.add(sh.Box(
			pos = Vec3(-dem.x + 0.5, 0.0, -dem.z),
			size = Vec3(0.5, dem.y, dem.z),
			template = TEMPLATE))
	
	# right
	if ((ROOM_SEG_WALL_RIGHT == None and randbool()) or ROOM_SEG_WALL_RIGHT):
		s.add(sh.Box(
			pos = Vec3(dem.x - 0.5, 0.0, -dem.z),
			size = Vec3(0.5, dem.y, dem.z),
			template = TEMPLATE))
	
	# top
	if ((ROOM_SEG_WALL_TOP == None and randbool()) or ROOM_SEG_WALL_TOP):
		s.add(sh.Box(
			pos = Vec3(0.0, dem.y - 0.5, -dem.z),
			size = Vec3(dem.x, 0.5, dem.z),
			template = TEMPLATE))
	
	# bottom
	if ((ROOM_SEG_WALL_BOTTOM == None and randbool()) or ROOM_SEG_WALL_BOTTOM):
		s.add(sh.Box(
			pos = Vec3(0.0, -dem.y / 2, -dem.z),
			size = Vec3(dem.x, 0.5, dem.z),
			template = TEMPLATE))

def Build_Crystal_Columns(s, count):
	for p in range(0, count + 1):
		x = ((p - (count / 2.0)) / count) * ROOM_SEG_WALLS.x
		
		pos = Vec3(x, -(ROOM_SEG_WALLS.y / 2.0), -s.size.z / 2.0)
		b = sh.Box(pos = pos, size = Vec3(0.5, (ROOM_SEG_WALLS.y / 2.0), 0.5), template = TEMPLATE)
		c = sh.Obstacle(pos = Vec3(x, 0.0, -s.size.z / 2.0), type = "scoretop", template = TEMPLATE)
		s.add(b)
		s.add(c)

def Build_Obstacle(s, type = "bar"):
	if (type == "bar"):
		pos = Vec3(0.0, 1.0, -s.size.z / 2.0)
		params = {}
		
		if (random.choice([True, False, False, False])):
			params["move"] = str(ureal())
			params["speed"] = str(ureal() * 0.5)
		
		if (random.choice([True, False])):
			params["blocker"] = "true"
		
		o = sh.Obstacle(pos = pos, type = "bar", template = TEMPLATE)
		
		s.add(o)
	
	elif (type == "beatmill"):
		pos = Vec3(0.0, 1.0, -s.size.z / 2.0)
		params = {}
		
		if (random.choice([True, False])):
			params["reverse"] = "true"
		
		o = sh.Obstacle(pos = pos, type = "beatmill", template = TEMPLATE)
		
		s.add(o)

def Generate_Segment(name):
	print(f"segment {name} {{")
	
	s = sh.Segment(name = name, size = ROOM_SEG_SIZE)
	print("\t", s)
	
	# Crystal stands
	r = integer(0, 1)
	
	if (r == 0):
		Build_Crystal_Columns(s, integer(1, 4))
	elif (r == 1):
		Build_Obstacle(s, random.choice(["bar", "beatmill"]))
	
	Add_Walls(s, ROOM_SEG_WALLS)
	
	print("}")
	
	return s

def Generate_End_Segment(size = ROOM_SEG_SIZE):
	s = sh.Segment(name = "door", size = size)
	
	# right
	s.add(sh.Box(
		pos = Vec3(size.x + 0.5, 1.0, -size.z + 0.5),
		size = Vec3(size.x - 0.5, size.y, 0.5),
		template = TEMPLATE))
	
	# left
	s.add(sh.Box(
		pos = Vec3(-size.x - 0.5, 1.0, -size.z + 0.5),
		size = Vec3(size.x - 0.5, size.y, 0.5),
		template = TEMPLATE))
	
	# top
	s.add(sh.Box(
		pos = Vec3(0.0, size.y / 2 + 0.5, -size.z + 0.5),
		size = Vec3(1.0, size.y / 2 - 1.5, 0.5),
		template = TEMPLATE))
	
	# bottom
	s.add(sh.Box(
		pos = Vec3(0.0, -size.y / 2 - 0.5, -size.z + 0.5),
		size = Vec3(1.0, size.y / 2 + 0.5, 0.5),
		template = TEMPLATE))
	
	# door
	s.add(sh.Obstacle(
		pos = Vec3(0.0, 0.0, -size.z + 0.5),
		type = random.choice(["doors/double", "doors/basic", "doors/45"]),
		params = {
			"buttons": str(integer(0, 3)),
		}))
	
	Add_Walls(s, Vec3(size.x / 2, size.y / 2, size.z / 2))
	
	return s;

def Generate_Room(path, name, segs):
	r = sh.Room(name = name, music = integer(1, 20), length = int(ROOM_LENGTH), fogColour = [ureal(), ureal(), ureal(), ureal(), ureal(), ureal()], stonehack = True)
	
	for i in range(segs):
		r.add(Generate_Segment(str(int(ROOM_SEG_SIZE.z)) + "_" + str(i)))
	
	r.setEnd(Generate_End_Segment())
	
	r.export(path)

def gen(path):
	for i in range(3):
		Generate_Room(path, "skylink" + str(i + 1), 7)
	
	#Generate_Room(path, "skylink2", 9)
	#Generate_Room(path, "skylink3", 13)

if (__name__ == "__main__"):
	import sys
	gen(sys.argv[1])
