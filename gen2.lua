#!/usr/bin/lua

--------------------------------------------------------------------------------
-- XML reading and writing support
--------------------------------------------------------------------------------

function _XmlNode_output(this)
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

function XmlNode(name, attributes, children)
	return {
		name = name,
		attributes = attributes,
		children = children,
		write = _XmlNode_output
	}
end

--------------------------------------------------------------------------------

x = XmlNode("node", {first = "second", test = "23124"})
print(XmlNode("node", {first = "second", test = "23124"}, {x}):write())

print 'test'
