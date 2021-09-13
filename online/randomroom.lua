--[[
# Smash Hit: Generated Rooms

## License

Copyright 2020 Knot126

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
]]

function initGlobals()
	--[[
	## Table of obstacles (version 1)
	
	**Note:** This has not been implemented and may change due to issues with a
	previous attempt at implementing it.
	
	This table contains tables which hold the name of the obstacle, their
	paramaters, and the value ranges for their paramaters. Not all of this info
	is used at the moment, but it is helpful to have a layout for everything.
	
	```lua
	The format is the following:
	{
		"name" = obstaclename                  -- The name of the obstacle
		"params" = {                           -- A table of paramaters
			{param_name, param_type, [param_max, param_min], [param_vals]},
			{param_name, param_type, [param_max, param_min], [param_vals]}
		},
		"type" = requirements                  -- Controls when the obstacle
		                                       -- should be spawned
	}
	```
	
	### Types
	
	The type property cotains data about where to obstacle should spawn.
	
	**Note:** In the future, all obstacles will need to specify their own spawn
	function.
	
	| Integer | Meaning                                                       |
	| ------- | ------------------------------------------------------------- |
	| -2      | Obstacle will use the spawn function to decide X/Y-axies*     |
	| -1      | Obstacle does not care about spawn position                   |
	| 0       | Obstacle needs to be high in the air                          |
	| 1       | Obstacle needs to be on solid ground                          |
	| 2       | Obstacle needs to be at {0.0, 1.0, z} to collide              |
	| 3       | Obstacle needs to be at {0.0, -height/2, z} to collide        |
	| 4       | Obstacle needs to be low to the ground                        |
	| 5       | Obstacle needs to be left/right of the player where y = 0.0   |
	| 6       | Obstacle needs to be high up and left/right of the player     |
	| 7       | Obstacle needs to be at {0.0, height/2, z} to collide         |
	| 8       | Obstacle needs to be at {0.0, 0.0, z} to collide              |
	]]
	
	-- init config table
	config = {}
	
	--[[
	## Power-up and crystal list
	
	A list of valid power-ups and crystals in this version of Smash Hit.
	]]
	config.powerups = {"ballfrenzy", "nitroballs", "slowmotion"}
	config.crystals = {"scorediamond", "scoremulti", "scorestar", "scoretop"}
	
	--[[
	## Particle Effects
	
	A list of particle effects in the the game. A random effect will be chosen
	to use.
	]]
	config.particles = {"lowrising", "sidesrising", "dustyfalling", "fallinglite", "starfield", "falling", "lowrising2", "bubbles"}
	
	--[[
	## Materials list
	
	List of valid materials in this version of Smash Hit.
	]]
	config.materials = {"steel", "wood", "glass"}
	
	--[[ 
	## Music list
	
	Table of music names. Same as the system is in Random Hit; append any extra
	tracks to the end of the list to add them.
	]]
	config.music = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "29_2", "30", "31", "32", "33", "34", "35", "36", "37", "38_1", "38_2", "39", "40", "41", "42_1", "42_2", "43", "44", "bowling"}
	
	--[[
	## Obstacles
	
	A list of obstacles that should be used in a normal room with their
	spawn functions.
	]]
	config.obstacles = {
		{name = "3dcross", mode = -2,
		spawn = function(z) 
			local x = 0.0;
			local y = 0.0;
			local thic = mgRndFloat(0.08, 0.14)
			local rad = thic + mgRndFloat(0.08, 0.14);
			mgObstacle("3dcross", x, y, z, gen.colour(), "size=" .. mgRndFloat(0.5, 2.0), "thickness=" .. thic, "radius=" .. rad)
		end},
		-----
		{name = "sidesweeper", mode = -2,
		spawn = function(z)
			local x = 0.0;
			local y = 0.0;
			mgObstace("sidesweeper", x, y, z, gen.colour(), "width=" .. mgRndFloat(1.5, 2.5))
		end},
		-----
		{name = "bar", mode = -2,
		spawn = function(z)
			local x = 0.0;
			local y = 1.0;
			mgObstacle("bar", x, y, z, gen.colour(), "thickness=" .. mgRndFloat(0.10, 0.14), "height=" .. mgRndFloat(0.06, 0.24), "blocker=" .. gen.rnd_bool(), "move=" .. mgRndInt(0, 1), "offset=" .. mgRndFloat(0.0, 30.0), "speed=" .. mgRndFloat(0.5, 1.5), "maxwidth=24")
		end},
		-----
		{name = "suspendcube", mode = -2,
		spawn = function(z)
			local x = 0.0;
			local y = mgRndFloat(0.6, 1.0);
			mgObstacle("suspendcube", x, y, z, gen.colour(), "width=" .. mgRndFloat(1.0, 2.5), "height=" .. mgRndFloat(1.0, 2.5), "depth=" .. mgRndFloat(0.2, 0.4))
		end},
		-----
		{name = "dna", mode = -2,
		spawn = function(z)
			local x = 0.0;
			local y = 1.0;
			mgObstacle("dna", x, y, z, gen.colour(), "segments=" .. mgRndInt(12, 18))
		end},
		-----
		{name = "laser", mode = -2,
		spawn = function(z)
			local x = -room.width+0.5;
			local y = 1.0;
			mgObstacle("laser", x, y, z, "beams=" .. mgRndInt(1, 8), "move=" .. mgRndInt(0, 1), "speed=" .. mgRndFloat(0.15, 0.35))
		end},
		-----
		{name = "suspendcylinder", mode = -2,
		spawn = function(z)
			local x = 0.0;
			local y = 1.0;
			mgObstacle("suspendcylinder", x, y, z, gen.colour(), "width=" .. mgRndFloat(3.0, 4.5))
		end},
		-----
		{name = "beatwindow", mode = -2,
		spawn = function(z)
			local x = 0.0;
			local y = 0.0;
			mgObstalce("beatwindow", x, y, z, gen.colour(), "offset=" .. mgRndFloat(0.0, 30.0), "beat=" .. mgRndFloat(1.0, 3.0), "width=" .. mgRndFloat(3.0, 5.0))
		end},
		-----
		{name = "bigcrank", mode = -2,
		spawn = function(z)
			local x = 0.0;
			local y = 1.0;
			mgObstacle("bigcrank", x, y, z, gen.colour(), "thickness=" .. mgRndFloat(0.08, 0.12), "height=" .. mgRndFloat(0.5, 2.0), "offset=" .. mgRndFloat(0.0, 30.0))
		end},
		-----
		{name = "pyramid", mode = -2,
		spawn = function(z)
			local x = 0.0;
			local y = room.floorDistance+0.5;
			mgObstacle("pyramid", x, y, z, gen.colour(), "levels=" .. mgRndInt(3, 6), "size=" .. mgRndFloat(0.18, 0.24), "material=" .. getRndFrom(config.materials))
			if not room.enableFloor then
				createBox({2.0, 2.0, 0.5}, {x, y - 1.0, z})
			end
		end},
		-----
		{name = "bigpendulum", mode = -2,
		spawn = function(z)
			local x = 0;
			local y = 0.5;
			mgObstacle("bigpendulum", x, y, z, gen.colour(), "dinglare=" .. gen.rnd_bool(), "followbeat=" .. gen.rnd_bool())
		end},
		-----
		{name = "rotor", mode = -2, 
		spawn = function(z)
			local x = 0;
			local y = getRndFrom({2.0, -1.0});
			mgObstacle("rotor", x, y, z,
			           gen.colour(), 
			           "length=" .. mgRndFloat(0.5, 3.0), 
			           "arms=" .. mgRndInt(2, 6), 
			           "endplate=" .. gen.rnd_bool(), 
			           "speed=" .. mgRndFloat(1.0, 4.0))
			end},
		-----
		{name = "cactus", mode = -2,
		spawn = function(z)
			local x = 0.0;
			local y = room.floorDistance+0.5;
			mgObstacle("cactus", x, y, z, gen.colour(), "scale=" .. mgRndFloat(0.8, 1.2), "thickness=" .. mgRndFloat(0.09, 0.11))
		end},
		-----
		{name = "gyro", mode = -2,
		spawn = function(z)
			local x = 0.0
			local y = 1.0
			mgObstacle("gyro", x, y, z, gen.colour(), "glass=" .. gen.rnd_bool(), "hexagon=" .. gen.rnd_bool(), "hollow=" .. gen.rnd_bool())
		end},
	}
	
	-- create room table
	room = {}
	
	--[[
	## Rotation
	
	Rotation is a set of randomly selected integerss from 0 to 2.
	]]
	room.rot = {0, 0}
	if mgRndInt(1, 15) == 7 then
		room.rot = {mgRndInt(-2, 2), mgRndInt(-2, 2)}
	end
	
	-- Room size
	room.size = {18, 15, --[[mgRndInt(80, 320)]]200}
	
	-- Room colour
	room.colour = {mgRndFloat(-0.35, 1.35), mgRndFloat(-0.35, 1.35), mgRndFloat(-0.35, 1.35)}
	
	-- Breaks
	room.breakBefore = 16
	room.breakAfter = 16
	
	--[[
	## Room Properties
	
	Global table for controling some room properties.
	]]
	
	-- Set the walls first so room width can be set to max value if there
	-- are not any walls.
	room.enableWalls = mgRndBool()
	if room.enableWalls then
		room.width = mgRndInt(4, 10) / 2
	else
		room.width = 8.0
	end
	room.ceilingHeight = mgRndInt(6, 18) / 2
	room.floorDistance = mgRndInt(-8, -1) / 2
	room.enableCeiling = mgRndBool()
	room.enableFloor = mgRndBool()
	room.glassColor = {mgRndFloat(-0.35, 1.35), mgRndFloat(-0.35, 1.35), mgRndFloat(-0.35, 1.35)}
	
	--[[
	## Room Order
	
	The number room this is in the CP, starting from zero.
	]]
	order = mgGetInt("order", 0)
	
	-- Offset paramater - this lets us fix some issues
	if order > 0 then
		room.boxOffset = (room.size[3] / 4) + 0.2
	else
		room.boxOffset = 0
	end
end

-- ----------------------------------------------------------------------------
-- Helper functions
-- ----------------------------------------------------------------------------

-- table for obstacle functions
gen = {}

function getRndFrom(e)
	-- Return a random value from some table
	return e[math.random(#e)]
end

function getRndOpposite(n)
	if mgRndBool() then
		return -n
	else
		return n
	end
end

function getRndSize(mx, my, mz)
	local t = {0, 0, 0}
	t[1] = mgRndFloat(0.5, mx) / 2
	t[2] = mgRndFloat(0.5, my) / 2
	t[3] = mgRndFloat(0.5, mz) / 2
	return t
end

function getWallColor()
	return tostring(room.colour[1]) .. " " .. tostring(room.colour[2]) .. " " .. tostring(room.colour[3])
end

function getGlassColor()
	return room.glassColor[1] .. " " .. room.glassColor[2] .. " " .. room.glassColor[3]
end

function createBox(size, pos)
	-- size  : table {x (width), y (height), z (depth)}
	-- pos   : table {x, y, z}
	pos[3] = pos[3] + room.boxOffset
	mgBox(size[1]/2, size[2]/2, size[3]/2, pos[1], pos[2], pos[3])
	mgObstacle("stone",
	           pos[1], pos[2], pos[3],
	           "sizeX=" .. tostring(size[1]/2),
	           "sizeY=" .. tostring(size[2]/2),
	           "sizeZ=" .. tostring(size[3]/2),
	           "color=" .. getWallColor())
end

function getRndSidePos()
	return {getRndOpposite(mgRndFloat(1.5, room.width)),
	        getRndOpposite(mgRndFloat(1.5, room.ceilingHeight))}
end

-- obstacle ease-of-use functions

function gen.colour()
	return "color=" .. getGlassColor()
end

function gen.wall_colour()
	return "color=" .. getWallColor()
end

function gen.rnd_bool()
	if mgRndBool() then
		return "true"
	else
		return "false"
	end
end

-- ----------------------------------------------------------------------------
-- Builders: These build the obstacles at various points.
-- ----------------------------------------------------------------------------

function buildWalls()
	--[[
	## Wall Builder
	
	This builder will build the walls, floor, and ceiling in parts of some size
	if they exsist.
	]]
	local div_size = room.size[3]/24
	-- note: updated during refactor for long rooms (16 -> 24)
	
	for i = 0, room.size[3]-(div_size/2), div_size do
		if room.enableWalls then
			-- left wall
			createBox({1.0, room.size[2]*2, div_size}, {-room.width, 0.0, -(div_size/2)-i})
			
			-- right wall
			createBox({1.0, room.size[2]*2, div_size}, {room.width, 0.0, -(div_size/2)-i})
		end
		
		if room.enableCeiling then
			-- ceiling
			createBox({room.size[1]*2, 1.0, div_size}, {0.0, room.ceilingHeight, -(div_size/2)-i})
		end
		
		if room.enableWalls then
			-- floor
			createBox({room.size[1]*2, 1.0, div_size}, {0.0, room.floorDistance, -(div_size/2)-i})
		end
	end
end

function buildDecor()
	--[[
	## Decor Builder
	
	**Note:** This builder may be replaced by a diffrent builder.
	
	Builds the columns on either side of the room. If there are walls, they
	will align to the walls. If there are no walls, they will be placed
	randomly.
	]]
	for z = 0, room.size[3], mgRndInt(12, 32) do
		local left = mgRndBool()
		local right = mgRndBool()
		
		-- Without walls, place decorations in a random position
		local x = 0.0
		if room.enableWalls then
			x = room.width - 1
		else
			x = mgRndFloat(1.5, 8.0)
		end
		
		if left then
			createBox({1.0, room.size[2] * 2, 1.0}, {-x, 0.0, -z})
		end
		
		if right then
			createBox({1.0, room.size[2] * 2, 1.0}, {x, 0.0, -z})
		end
	end
end

function buildObstacles()
	--[[
	## New Obstacle Builder
	
	This builder will place the obstacles using only the spawn function.
	]]
	for z = room.breakBefore, room.size[3]-room.breakAfter, mgRndFloat(8, 24) do
		local obs = getRndFrom(config.obstacles)
		obs.spawn(-z+room.boxOffset)
	end
end

function buildSimpleUnevenFloor()
	--[[ 
	## Uneven Floor Builder
	
	**Warning:** This builder will be replaced in the future.
	
	Builds the uneven (bumps) in the floor if there is a floor to build them on.
	]]
	if room.enableWalls then
		for z = 0, room.size[3], mgRndInt(3, 6) / 2 do
			local p = 0.0
			
			-- If there are no walls let the uneven parts go anywhere
			if room.enableWalls then
				p = room.width - 1.0
			else
				p = room.size[1]
			end
			
			local x = mgRndInt(-p, p)
			local wy = mgRndInt(5, 25) / 100
			createBox({1.0, wy, 1.0}, {x, room.floorDistance+(0.5+(wy/2)), -z})
		end
		
		for z = 0, room.size[3], mgRndInt(3, 6) / 2 do
			local w = 0
			local c = 0
			-- Calculate for without/with walls
			if room.enableCeiling then
				w = room.floorDistance
			else
				w = -room.size[2]
			end
			
			if room.enableWalls then
				c = room.ceilingHeight
			else
				c = room.size[2]
			end
			
			local y = mgRndInt(w + 1.0, c - 1.0)
			local wx = mgRndInt(5, 25) / 100
			local x = getRndOpposite((room.width-0.5-(wx/2)))
			createBox({wx, 1.0, 1.0}, {x, y, -z})
		end
	end
end

function buildEndWall()
	--[[
	## End Wall Builder
	
	Builds the ending wall with a zero, one, or two button door.
	]]
	local z = room.size[3] - 0.5
	
	createBox({room.size[1], room.size[2], 1.0}, {-(room.size[1]/2)-1.0, 0.0, -z})
	createBox({room.size[1], room.size[2], 1.0}, {(room.size[1]/2)+1.0, 0.0, -z})
	createBox({2.0, room.size[2], 1.0}, {0.0, -room.size[2]/2, -z})
	createBox({2.0, room.size[2], 1.0}, {0.0, (room.size[2]/2)+2.0, -z})
	
	mgObstacle("doors/basic", 0.0, 0.0, -z, "buttons=" .. tostring(mgRndInt(0, 2)))
end

function buildWallessRoom()
	--[[
	## Walless Room Builder
	
	Builder for a room without any walls, ceiling, or floor.
	]]
	for z = 0, room.size[3], (mgRndInt(1, 4)/2) do
		local pos = getRndSidePos()
		createBox({1.0, 1.0, 1.0}, {pos[1], pos[2], -z})
		if (mgRndInt(1, 100) == 50) then
			mgPowerUp(getRndFrom(config.powerups), pos[1], pos[2]+0.5, -z)
		end
	end
end

-- ----------------------------------------------------------------------------
-- Main Functions
-- ----------------------------------------------------------------------------

function init()
	-- init global variables
	initGlobals()
	
	-- set the fog color
	mgFogColor(mgRndFloat(-0.35, 1.35), mgRndFloat(-0.35, 1.35), mgRndFloat(-0.35, 1.35), 
	           mgRndFloat(-0.35, 1.35), mgRndFloat(-0.35, 1.35), mgRndFloat(-0.35, 1.35))
	
	-- set the music
	mgMusic(getRndFrom(config.music))
	
	-- set the rotation
	mgSetRotation(room.rot[1], room.rot[2])
	
	-- set particle effects
	if mgRndBool() then
		mgParticles(getRndFrom(config.particles))
	end
	
	-- build the room using various builders
	buildWalls()
	buildDecor()
	buildSimpleUnevenFloor()
	if not room.enableCeiling and not room.enableWalls and not room.enableWalls then
		buildWallessRoom()
	end
	buildObstacles()
	buildEndWall()
	
	-- set room length
	mgLength(room.size[3])
end

function tick()
end
