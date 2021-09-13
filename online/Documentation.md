# Smash Hit: Generated Rooms

## License

Copyright 2020 Knot126

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

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

## Particle Effects

A list of particle effects in the the game. A random effect will be chosen
to use.

## Materials list

List of valid materials in this version of Smash Hit.

## Music list

Table of music names. Same as the system is in Random Hit; append any extra
tracks to the end of the list to add them.

## Obstacles

A list of obstacles that should be used in a normal room with their
spawn functions.

## Rotation

Rotation is a set of randomly selected integerss from 0 to 2.

## Room Properties

Global table for controling some room properties.

## Wall Builder

This builder will build the walls, floor, and ceiling in parts of some size
if they exsist.

## Decor Builder

**Note:** This builder may be replaced by a diffrent builder.

Builds the columns on either side of the room. If there are walls, they
will align to the walls. If there are no walls, they will be placed
randomly.

## New Obstacle Builder

This builder will place the obstacles using only the spawn function.

## Uneven Floor Builder

**Warning:** This builder will be replaced in the future.

Builds the uneven (bumps) in the floor if there is a floor to build them on.

## End Wall Builder

Builds the ending wall with a zero, one, or two button door.

## Walless Room Builder

Builder for a room without any walls, ceiling, or floor.

