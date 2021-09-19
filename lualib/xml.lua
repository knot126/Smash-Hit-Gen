#!/usr/bin/lua

--------------------------------------------------------------------------------
-- XML reading and writing support
--------------------------------------------------------------------------------

function _XmlNode_output(this)
	--[[
	Save the XML node to a string.
	]]
	local base = "<"
	
	base = base .. this.name
	
	if this.attributes ~= nil then
		for k, v in pairs(this.attributes) do
			base = base .. " " .. tostring(k) .. "=\"" .. tostring(v) .. "\""
		end
	end
	
	if this.children ~= nil then
		base = base .. ">\n"
		
		for i = 1, #this.children do
			base = base .. "\t" .. _XmlNode_output(this.children[i]) .. "\n"
		end
		
		base = base .. "</" .. this.name .. ">\n"
	else
		base = base .. "/>"
	end
	
	return base
end

function _XmlNode_save(this, filename)
	--[[
	Save the XML node to a file.
	]]
	
	f = io.open(filename, "w")
	f:write(this:write())
	f:close()
end

function XmlNode(name, attributes, children)
	--[[
	Create an XML node
	]]
	return {
		name = name,
		attributes = attributes,
		children = children,
		write = _XmlNode_output,
		save = _XmlNode_save
	}
end

--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
