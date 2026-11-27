-- In the standalone PDF, resolve repository links against this edition.
local base = "https://github.com/arivero/qcdstring/blob/y1999/outputs/"
function Link(link)
  if link.target:sub(1, 3) == "../" then
    link.target = base .. link.target:sub(4)
  elseif not link.target:match("^%a[%w+.-]*:") and link.target:sub(1, 1) ~= "#" then
    link.target = base .. "1999-string-at-the-tip/" .. link.target
  end
  return link
end
