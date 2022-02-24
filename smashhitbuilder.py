"""
Smash Hit Segment Builder

This interface allows very easy construction of Smash Hit segments. I originally
intend this for use with procedureal generation tools, but it can be used for
any purpose, really.
"""

import os

TRAINING = (1 << 0)
CLASSIC = (1 << 1)
MAYHEM = (1 << 2)
ZEN = (1 << 3)
COOP = (1 << 4)
VERSUS = (1 << 5)
VS = VERSUS

def createTagString(*, name = "tag", params = {}, close = True, text = None, indent = 0):
	"""
	Generate an XML tag string
	
	Name: The name of the tag 
	Params: The attributes to apply to the tag 
	Close: If the tag should be self-closing
	    Text: If not closing, then the text to put between
	"""
	
	# This workaround is needed in order to have tabs in format expressions
	TAB = '\t'
	
	# '<name'
	tag = f"{TAB * indent}<{name}"
	
	# 'attribute="value"'
	for k, v in params.items():
		tag += f" {k}=\"{v}\""
	
	# '/>' or '> text </name>'
	if (close):
		tag += "/>\n"
	else:
		tag += ">\n" + text + f"{TAB * indent}</{name}>\n"
	
	return tag

class Vec2:
	"""
	2D Vector class (not used much)
	"""
	
	def __init__(self, x = 0.0, y = 0.0):
		"""
		Initialise the vector
		"""
		self.x = x
		self.y = y
	
	def __format__(self, spec = None):
		"""
		Format vector to Smash Hit style string
		"""
		return str(self.x) + " " + str(self.y)

class Vec3:
	"""
	3D Vector class
	"""
	
	def __init__(self, x = 0.0, y = 0.0, z = 0.0):
		"""
		Initialise the vector
		"""
		self.x = x
		self.y = y
		self.z = z
	
	def __format__(self, spec = None):
		"""
		Format vector to Smash Hit style string
		"""
		return str(self.x) + " " + str(self.y) + " " + str(self.z)
	
	def __add__(self, other):
		"""
		Add two vectors
		"""
		return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
	
	def __mul__(self, other):
		"""
		Scalar multiplication for vectors
		"""
		if (type(other) == int or type(other) == float):
			return Vec3(self.x * other, self.y * other, self.z * other)
		else:
			return None
	
	def __eq__(self, other):
		"""
		Equality check for vectors
		"""
		return (type(self) == type(other)) and (self.x == other.x) and (self.y == other.y) and (self.z == other.z)
	
	def __ne__(self, other):
		"""
		Non-equality check for vectors
		"""
		return (type(self) != type(other)) or (self.x != other.x) or (self.y != other.y) or (self.z != other.z)

class Colour:
	"""
	Colour class - a Vec3 can be used instead, since all export implicitly uses
	python formatting.
	
	Colours are R, G, B and A channels, with values in the range [0.0, 1.0].
	"""
	
	def __init__(self, r = 1.0, g = 1.0, b = 1.0, a = 1.0):
		"""
		Initialise the vector
		"""
		self.r = r
		self.g = g
		self.b = b
		self.a = a
	
	def __format__(self, spec = None):
		"""
		Format vector to Smash Hit style string
		"""
		res = str(self.r) + " " + str(self.g) + " " + str(self.b)
		
		if (self.a != 1.0):
			res += " " + str(self.a)
		
		return res

class Room:
	"""
	The class representing an entire room and its segments.
	
	Constructor parameters:
		name : String = Room name
		music : String | Int = Music file or integer number
		fogColour : List<Float>[6] = List of Colour values to use, ex: [r, g, b, r, g, b]
		length : Int | List<Int>[3] = Length of the room or list in [training, classic, mayhem]
		segStart : Segment = The starting segment
		segEnd : Segment = The ending segment
		segments : List<Segment>[] = A list of segments in the room
	"""
	
	def __init__(self, name = "", music = 0, fogColour = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2], length = 0, segStart = None, segEnd = None, segments = None, stonehack = None):
		"""
		Initialise the room
		"""
		self.name = name
		self.music = music
		self.fogColour = fogColour
		self.length = length
		self.segStart = segStart
		self.segEnd = segEnd
		self.segments = segments if segments != None else []
		self.stonehack = stonehack
	
	def __format__(self, spec = None):
		"""
		Format the room to a lua script
		"""
		
		# Init function start
		res = """function init()\n"""
		
		# Uncomment this for a more smash hit-like file
		#if (self.segStart):
			#res += '\tpStart = mgGetBool("start", true)\n'
		
		#if (self.segEnd):
			#res += '\tpEnd = mgGetBool("end", true)\n'
		
		#res += "\t\n"
		
		# Music
		if (self.music != None):
			res += f'\tmgMusic("{self.music}")\n'
		
		# Fog colour
		if (self.fogColour):
			res += f'\tmgFogColor({self.fogColour[0]}, {self.fogColour[1]}, {self.fogColour[2]}, {self.fogColour[3]}, {self.fogColour[4]}, {self.fogColour[5]})\n'
		
		res += "\t\n"
		
		# Segments
		for i in range(len(self.segments)):
			res += f'\tconfSegment("{self.name + "/" + self.segments[i].name}", 1)\n'
		
		# The length = 0 line
		res += "\t\n\tl = 0\n\t\n"
		
		# Start segment
		if (self.segStart != None):
			res += f'\tif mgGetBool("start", true) then\n\t\tl = l + mgSegment("{self.name + "/" + self.segStart.name}", -l)\n\tend\n\t\n'
		
		# Set target length
		if (self.length != None and type(self.length) == int):
			res += f'\tlocal targetLen = {self.length}\n'
		else:
			res += f'local targetLen = {self.length[CLASSIC]}\n'
			res += f'if mgGet("player.mode")=="0" then targetLen = {self.length[TRAINING]} end\n'
			res += f'if mgGet("player.mode")=="2" then targetLen = {self.length[MAYHEM]} end\n'
		
		# Loading the segments
		res += """\t\n\twhile l < targetLen do
		s = nextSegment()
		l = l + mgSegment(s, -l)
	end\n"""
		
		res += "\t\n"
		
		# End segment
		if (self.segEnd):
			res += f'\tif mgGetBool("end", true) then\n\t\tl = l + mgSegment("{self.name + "/" + self.segEnd.name}", -l)\n\tend\n\t\n'
		
		# set room length
		res += "\tmgLength(l)\n"
		
		# End init function
		res += "end\n"
		
		# Tick function (usually unused)
		res += "\nfunction tick()\nend\n"
		
		return res
	
	def write(self, path = "defaultRoom.lua"):
		"""
		Write room to a lua file
		"""
		f = open(path, "w")
		f.write(self.__format__())
		f.close()
	
	def export(self, assetsFolder = "devel/assets", extraName = ".mp3"):
		"""
		Export room and segment files to an assets folder
		
		NOTE: Since this uses os.makedirs, the path cannot contain sepcial
		things like '..'
		"""
		
		os.makedirs(assetsFolder + "/rooms", exist_ok = True)
		os.makedirs(assetsFolder + "/segments/" + self.name, exist_ok = True)
		
		# Write self
		self.write(assetsFolder + "/rooms/" + self.name + ".lua" + extraName)
		
		# Write children segments
		if (self.segStart):
			# Set stonehack
			if (self.stonehack != None):
				self.segStart.setStonehack(self.stonehack)
			
			# Write file
			self.segStart.write(assetsFolder + "/segments/" + self.name + "/" + self.segStart.name + ".xml" + extraName)
		
		for i in range(len(self.segments)):
			# Set stonehack
			if (self.stonehack != None):
				self.segments[i].setStonehack(self.stonehack)
			
			# Write file
			self.segments[i].write(assetsFolder + "/segments/" + self.name + "/" + self.segments[i].name + ".xml" + extraName)
		
		if (self.segEnd):
			# Set stonehack
			if (self.stonehack != None):
				self.segEnd.setStonehack(self.stonehack)
			
			# Write file
			self.segEnd.write(assetsFolder + "/segments/" + self.name + "/" + self.segEnd.name + ".xml" + extraName)
	
	def setStart(self, segment):
		"""
		Set the starting segment
		"""
		self.segStart = segment
	
	def setEnd(self, segment):
		"""
		Set the ending segment
		"""
		self.segEnd = segment
	
	def add(self, segment):
		"""
		Add a segment to the room
		"""
		self.segments.append(segment)
	
	def setStonehack(self, stonehack = None):
		"""
		Set the stonehack mode
		"""
		self.stonehack = stonehack

class Segment:
	"""
	The base segment class
	
	Create: Segment(size, template, light, fog, shadow, entities, [name], [stonehack])
	
	  * Stonehack is used to enable something like the stonehack in blender tools.
	  * Name is used for saving segments to files in batches.
	"""
	
	def __init__(self, name = "", size = Vec3(), template = "", light = None, fog = None, shadow = None, entities = None, stonehack = None):
		"""
		Initialise the level
		"""
		
		self.name = name
		
		self.size = size
		self.template = template
		self.light = light
		self.fog = fog
		self.shadow = shadow
		self.entities = entities if entities != None else []
		self.stonehack = stonehack
	
	def __format__(self, spec = None):
		"""
		Format the level to an XML document
		"""
		
		# text for sub-entities
		text = ""
		
		for e in self.entities:
			text += format(e)
			
			# Do the stonehack
			if (self.stonehack and type(e) == Box):
				# If this box does not have the size property set, then we
				# cannot know enough information to make a stonehack box.
				if (not e.size):
					continue
				
				obs = Obstacle(type = "stone", pos = e.pos, params = {"sizeX": e.size.x, "sizeY": e.size.y, "sizeZ": e.size.z}, template = e.template)
				
				if (e.colour != None):
					obs.setParam("color", format(e.colour));
				
				obs.setImportIgnore("STONEHACK_IGNORE")
				
				text += format(obs)
		
		# The attributes of the segment
		params = {"size": self.size}
		
		if (self.template):
			params["template"] = self.template
		
		if (self.light and self.light != [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]):
			params["lightLeft"] = self.light[0]
			params["lightRight"] = self.light[1]
			params["lightTop"] = self.light[2]
			params["lightBottom"] = self.light[3]
			params["lightFront"] = self.light[4]
			params["lightBack"] = self.light[5]
		
		if (self.fog):
			params["fogcolor"] = format(self.fog)
		
		if (self.shadow):
			params["softshadow"] = str(self.shadow)
		
		return createTagString(name = "segment", params = params, close = False, text = text);
	
	def add(self, ent):
		"""
		Add an entity to the level
		"""
		
		self.entities.append(ent)
	
	def getString(self):
		"""
		Get a string of the level
		"""
		
		return self.__format__()
	
	def setStonehack(self, stonehack = None):
		"""
		Set the enablement of the stonehack, which adds stone with boxes so they
		will visibly show.
		"""
		
		self.stonehack = stonehack
	
	def write(self, path = "defaultSegment.xml"):
		"""
		Write the segment out to an uncompressed file
		"""
		
		f = open(path, "w")
		f.write(format(self))
		f.close()
	
	def setProperties(self, obstacleTemplate = None, stoneTemplate = None):
		"""
		Set the properties needed for calls to createXXX so that they will have
		the proper information.
		"""
		
		self.obstacleTemplate = obstacleTemplate if obstacleTemplate != None else self.template
		self.stoneTemplate = stoneTemplate if stoneTemplate != None else self.template
		
		return self
	
	def createBox(self, pos, size = Vec3(0.0, 0.0, 0.0)):
		"""
		Create a box using the default properties
		"""

class Entity:
	"""
	A base class for entites
	"""
	
	def __init__(self):
		self.pos = Vec3(0.0, 0.0, 0.0)
		self.hidden = None
		self.template = ""
	
	def setPos(self, pos = Vec3()):
		self.pos = pos
	
	def setHidden(self, hidden = False):
		self.hidden = hidden
	
	def setTemplate(self, template = ""):
		self.template = template

class Obstacle(Entity):
	"""
	Obstacle class
	
	Create: Obstacle(pos, template, type, params, rot, difficulty, mode)
	"""
	
	def __init__(self, pos = Vec3(), template = "", type = None, params = None, rot = None, difficulty = None, mode = None):
		"""
		Initialise the obstacle
		"""
		super().__init__()
		
		self.pos = pos
		self.template = template
		
		self.type = type
		self.params = params
		self.rot = rot
		self.difficulty = difficulty
		self.mode = mode
		self.importIgnore = None
	
	def __format__(self, spec = None):
		"""
		Format the obstacle as an XML tag
		"""
		params = {"pos": self.pos}
		
		if (self.type):
			params["type"] = self.type
		
		if (self.hidden != None):
			if (self.hidden):
				params["hidden"] = "1"
			else:
				params["hidden"] = "0"
		
		if (self.template):
			params["template"] = self.template
		
		if (self.rot and self.rot.x != 0.0 and self.rot.y != 0.0 and self.rot.z != 0.0):
			params["rot"] = format(self.rot * 6.283)
		
		if (self.difficulty != None and self.difficulty != [0, 1]):
			params["difficulty"] = str(self.difficulty[0]) + " " + str(self.difficulty[1])
		
		if (self.mode):
			params["mode"] = format(self.mode)
		
		if (self.params):
			i = 1
			for p, v in self.params.items():
				params["param" + str(i)] = str(p) + "=" + str(v)
				i += 1
		
		if (self.importIgnore):
			params["_importIgnore"] = self.importIgnore
		
		return createTagString(name = "obstacle", params = params, indent = 1);
	
	def setType(self, type):
		"""
		Set the type of obstacle
		"""
		self.type = type
	
	def setParam(self, key, value):
		"""
		Set or add a parameter to the obstacle
		"""
		self.params[key] = value
	
	def getParam(self, key):
		"""
		Get the given parameter's value
		"""
		return self.params.get(key, None)
	
	def delParam(self, key):
		"""
		Delete a parameter if it exsists
		"""
		if (key in self.params):
			del self.params[key]
	
	def hasParam(self, key):
		"""
		See if the obstacle has the parameter identifed by key.
		"""
		return key in self.params
	
	def setRot(self, rot = Vec3()):
		"""
		Set the obstacle's rotation
		"""
		self.rot = rot 
	
	def setDifficulty(self, min, max):
		"""
		Set the difficulty to [min, max]
		"""
		self.difficulty = [min, max]
	
	def setMode(self, mode = 0):
		"""
		Set the modes that the obstacle appear in
		"""
		self.mode = mode
	
	def setImportIgnore(self, importIgnore = None):
		"""
		Set what the import ignore tags should be set to.
		"""
		self.importIgnore = importIgnore

class Box:
	"""
	Box class
	"""
	
	def __init__(self, pos = Vec3(), template = "", size = Vec3(), visible = None, colour = None, tile = None, tileSize = None, tileRot = None, refelection = None):
		"""
		Initialise the box
		"""
		super().__init__()
		
		self.pos = pos
		self.template = template
		
		self.size = size
		self.visible = visible
		self.colour = colour
		self.tile = tile
		self.tileSize = tileSize
		self.tileRot = tileRot
		self.refelection = refelection
	
	def __format__(self, spec = None):
		"""
		Format the box as an XML string
		"""
		
		params = {"pos": self.pos, "size": self.size}
		
		if (self.template):
			params["template"] = str(self.template)
		
		if (self.visible != None and not self.visible):
			params["visible"] = "0"
		
		if (self.colour != None):
			params["color"] = format(self.colour)
		
		if (self.tile != None):
			if (type(self.tile) == int):
				params["tile"] = str(self.tile)
			else:
				params["tile"] = str(self.tile[0]) + "" + str(self.tile[1]) + "" + str(self.tile[2])
		
		if (self.tileSize != None):
			params["tileSize"] = format(self.tileSize)
		
		if (self.tileRot != None):
			params["tileRot"] = format(self.tileRot * 6.283)
		
		if (self.refelection != None):
			if (self.refelection):
				params["refelection"] = "1"
			else:
				params["refelection"] = "0"
		
		return createTagString(name = "box", params = params, indent = 1);
	
	def setSize(self, size = Vec3()):
		"""
		Set the size for the box
		"""
		self.size = size
	
	def setTemplate(self, template = None):
		"""
		Set the template for the box
		"""
		self.template = template
	
	def setVisible(self, visible = None):
		"""
		Set the visible property for the box. This is if it will be baked into
		the LitMesh.
		"""
		self.visible = visible
	
	def setColour(self, colour = None):
		"""
		Set the colour of the box.
		"""
		self.colour = colour
	
	def setTile(self, tile = None):
		"""
		Set the box tile.
		"""
		self.tile = tile
	
	def setTileSize(self, tileSize = None):
		"""
		Set the box tile size.
		"""
		self.tileSize = tileSize
	
	def setTileRot(self, tileRot = None):
		"""
		Set the box tile rotation.
		"""
		self.tileRot = tileRot
	
	def setRefelection(self, refelection = None):
		"""
		Set the box's refelection.
		"""
		self.refelection = refelection

def shb_test():
	import random
	
	real = random.random
	integer = random.randint
	
	print("<!-- SEGMENT TEST -->")
	
	level = Segment(size = Vec3(12.0, 10.0, 32.0), template = "basic", shadow = 0.4993, stonehack = True, name = "32_0")
	
	for z in range(1, 8):
		x = ((random.random() - 0.5) * 2.0) * 5.0
		
		obs = Obstacle(pos = Vec3(x, 0.5, -z * 4), template = "orange", type = "scoretop")
		level.add(obs)
		
		box = Box(pos = Vec3(x, 0, -z * 4), template = "orange_s", size = Vec3(0.5, 0.5, 0.5))
		level.add(box)
	
	print(f"{level}")
	level.write()
	
	print("\n\n\n-- ROOM TEST --")
	
	room = Room(name = "planet", music = integer(1, 20), length = 200, fogColour = [real(), real(), real(), real(), real(), real()])
	room.setStonehack(True)
	room.setStart(level)
	room.setEnd(level)
	room.add(level)
	
	print(f"{room}")
	room.export("/tmp/apk-editor-studio/apk/{11be7bb4-ce4a-437b-b488-25d5de2f07e0}/assets")
	

if (__name__ == "__main__"):
	shb_test()
