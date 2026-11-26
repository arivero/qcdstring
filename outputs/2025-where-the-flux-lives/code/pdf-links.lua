-- Resolve local links in the downloadable PDF against its tagged edition.
local base = "https://github.com/arivero/qcdstring/blob/y2025-v3/outputs/"
function Link(link)
  if link.target:sub(1, 3) == "../" then
    link.target = base .. link.target:sub(4)
  elseif not link.target:match("^%a[%w+.-]*:") and link.target:sub(1, 1) ~= "#" then
    link.target = base .. "2025-where-the-flux-lives/" .. link.target
  end
  return link
end
