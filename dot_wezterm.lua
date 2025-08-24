local wezterm = require("wezterm")
local config = {}
local act = wezterm.action
config.font_size = 15.0
config.default_prog = { "pwsh.exe" }
-- config.front_end = "WebGpu"
-- config.webgpu_power_preference = "HighPerformance"
config.font = wezterm.font("FiraCode Nerd Font")
config.canonicalize_pasted_newlines = "CarriageReturn"
--     backend="DirectX 12",
--     name="llvmpipe (LLVM 14.0.0, 256 bits)",
--     device_type="Cpu",
-- }
config.window_decorations = "RESIZE"
config.color_scheme = "Catppuccin Mocha"

config.window_padding = {
	left = 2,
	right = 2,
	top = 10,
	bottom = 2,
}

config.leader = { key = " ", mods = "CTRL", timeout_milliseconds = 1000 }

config.keys = {
	-- Splits
	{ key = "\\", mods = "LEADER", action = act.SplitHorizontal({ domain = "CurrentPaneDomain" }) },
	{ key = "-", mods = "LEADER", action = act.SplitVertical({ domain = "CurrentPaneDomain" }) },
	{ key = "x", mods = "LEADER", action = act.CloseCurrentPane({ confirm = false }) },
	{ key = "z", mods = "LEADER", action = act.TogglePaneZoomState },
	-- Tabs
	{ key = "\t", mods = "CTRL", action = act.ActivateTabRelative(1) },
	{ key = "\t", mods = "CTRL|SHIFT", action = act.ActivateTabRelative(-1) },
	{ key = "n", mods = "CTRL|SHIFT", action = act.ActivateTabRelative(1) },
	{ key = "p", mods = "CTRL|SHIFT", action = act.ActivateTabRelative(-1) },
	{ key = "x", mods = "CTRL|LEADER", action = act.CloseCurrentTab({ confirm = true }) },
	{ key = "c", mods = "LEADER", action = act.ShowLauncher },
	{ key = "Escape", mods = "LEADER", action = act.ActivateCopyMode },
	{ key = "x", mods = "ALT", action = act.ActivateCommandPalette },
}
wezterm.on("augment-command-palette", function(window, pane)
	return {
		{
			brief = "Rename tab",
			icon = "md_rename_box",

			action = act.PromptInputLine({
				description = "Enter new name for tab",
				initial_value = "",
				action = wezterm.action_callback(function(window, pane, line)
					if line then
						window:active_tab():set_title(line)
					end
				end),
			}),
		},
	}
end)

-- plugins
-- vim-wezterm navigation
local smart_splits = wezterm.plugin.require("https://github.com/mrjones2014/smart-splits.nvim")
smart_splits.apply_to_config(config, {
	direction_keys = { "h", "j", "k", "l" },
	modifiers = {
		move = "CTRL",
		resize = "META",
	},
})
-- tab bar
local bar = wezterm.plugin.require("https://github.com/adriankarlen/bar.wezterm")
bar.apply_to_config(config, {
	position = "top",
	modules = {
		workspace = {
			enabled = false,
		},
		leader = {
			enabled = false,
		},
		hostname = {
			enabled = false,
		},
		clock = {
			enabled = false,
		},
		cwd = {
			enabled = false,
		},
		pane = {
			enabled = true,
		},
		username = {
			enabled = false,
		},
	},
})

local custom = wezterm.color.get_builtin_schemes()["Catppuccin Mocha"]
custom.background = "#181825"
custom.tab_bar.background = "#1e1e2e"
custom.tab_bar.inactive_tab.bg_color = "#181825"

config.color_schemes = {
	["OLEDppuccin"] = custom,
}
config.color_scheme = "OLEDppuccin"
return config
