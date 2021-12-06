#########################################################
# Config by Ben Pearson                                 #
# Feel free to use and mess around and such. For best   #
# navigation, set foldmethod=marker for vim, or         #
# equivalent on text ediot of choice.                   #
#########################################################
import os
import re
import socket
import subprocess
from libqtile.config import Drag, Key, Screen, Group, Drag, Click, Rule
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook, qtile

# MOD KEYS, CONSTANTS, INITIAL SETUP{{{
# mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser("~")


@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


myTerm = "alacritty"  # My terminal of choice

# }}}
# KEYBINDINGS{{{

keys = [
    # SUPER + FUNCTION KEYS
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "n", lazy.window.toggle_minimize()),
    Key([mod, "shift"], "f", lazy.window.toggle_floating()),
    Key([mod], "w", lazy.window.kill()),
    Key([mod], "v", lazy.spawn("pavucontrol")),
    Key([mod], "d", lazy.spawn("nwggrid -p -o 0.4")),
    Key([mod], "Escape", lazy.spawn("xkill")),
    Key([mod], "Return", lazy.spawn("alacritty")),
    Key([mod], "KP_Enter", lazy.spawn("alacritty")),
    Key([mod], "space", lazy.spawn("ulauncher-toggle")),
    Key([mod, "mod1"], "l", lazy.spawn("betterlockscreen -l")),
    Key(
        [mod, "mod1"],
        "h",
        lazy.spawn("pactl set-sink-port 52 analog-output-headphones"),
    ),
    Key([mod, "mod1"], "s", lazy.spawn("pactl set-sink-port 52 analog-output-lineout")),
    # SUPER + SHIFT KEYS
    Key([mod, "shift"], "Return", lazy.spawn("alacritty -e ranger")),
    Key(
        [
            mod,
        ],
        "w",
        lazy.window.kill(),
    ),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "shift"], "x", lazy.shutdown()),
    # CONTROL + ALT KEYS
    Key(["mod1", "control"], "u", lazy.spawn("pavucontrol")),
    # ALT + ... KEYS
    Key(["mod1"], "p", lazy.spawn("pamac-manager")),
    Key(["mod1"], "f", lazy.spawn("firefox")),
    Key(["mod1"], "m", lazy.spawn("pcmanfm")),
    Key([mod], "e", lazy.spawn('emacsclient -a "" -c')),
    # CONTROL + SHIFT KEYS
    Key([mod2, "shift"], "Escape", lazy.spawn("lxtask")),
    # SCREENSHOTS
    Key([], "Print", lazy.spawn("flameshot full -p " + home + "/Pictures")),
    Key([mod2], "Print", lazy.spawn("flameshot full -p " + home + "/Pictures")),
    # MULTIMEDIA KEYS
    # INCREASE/DECREASE BRIGHTNESS
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),
    # INCREASE/DECREASE/MUTE VOLUME
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),
    # QTILE LAYOUT KEYS
    Key([mod, "shift"], "n", lazy.layout.normalize()),
    # CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    # Toggle Screen
    Key(
        [mod],
        "period",
        lazy.next_screen(),
    ),
    # CHANGE STACK ORDER
    Key(
        [mod, "shift"],
        "j",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down(),
    ),
    Key(
        [mod, "shift"],
        "k",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up(),
    ),
    # RESIZE UP, DOWN, LEFT, RIGHT
    Key(
        [mod, "control"],
        "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
    ),
    Key(
        [mod, "control"],
        "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
    ),
    Key(
        [mod, "control"],
        "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
    ),
    Key(
        [mod, "control"],
        "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
    ),
    Key(
        [mod, "control"],
        "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
    ),
    Key(
        [mod, "control"],
        "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
    ),
    Key(
        [mod, "control"],
        "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
    ),
    Key(
        [mod, "control"],
        "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
    ),
]

groups = []

# FOR QWERTY KEYBOARDS
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


group_labels = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]
# group_labels = ["", "", "", "", "",]

group_layouts = ["tile", "tile", "tile", "tile", "tile", "tile", "tile", "tile", "tile"]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        )
    )

for i in groups:
    keys.extend(
        [
            # CHANGE WORKSPACES
            Key([mod], i.name, lazy.group[i.name].toscreen()),
            Key([mod], "Tab", lazy.screen.next_group()),
            Key(["mod1"], "Tab", lazy.screen.next_group()),
            Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),
            # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
        ]
    )
    # }}}
# LAYOUTS {{{


def init_layout_theme():
    return {
        "margin": 8,
        "margin_on_single": 0,
        "border_width": 2,
        "border_focus": "e1acff",
        "border_normal": "1D2330",
    }


layout_theme = init_layout_theme()


layouts = [
    layout.Floating(**layout_theme),
    layout.Max(),
    layout.Columns(**layout_theme),
    layout.Tile(**layout_theme),
    layout.MonadTall(**layout_theme),
]
# }}}
# WIDGETS {{{

widget_defaults = dict(
    font="Source Code Pro Medium",
    fontsize=18,
    padding=5,
)
nerd_icon_defaults = dict(font="Iosevka Nerd Font", fontsize=20)
extension_defaults = widget_defaults.copy()

# colors for the bar/widgets/panel
def init_colors():
    return [
        ["#282c34", "#282c34"],  # color 0
        ["#596273", "#596273"],  # color 1
        ["#C4C7C5", "#C4C7C5"],  # color 2
        ["#B07190", "#B07190"],  # color 3
        ["#BFBAAC", "#BFBAAC"],  # color 4
        ["#5A8CE8", "#5A8CE8"],  # color 5
        ["#E0B742", "#E0B742"],  # color 6
        ["#D56F6E", "#D56F6E"],  # color 7
        ["#68CB79", "#68CB79"],
    ]  # color 8


colors = init_colors()

# Widget Functions
def replace_text(text):
    return ""


# def replace_text(text):
#     for string in ["/home/ben"]:
#         text = text.replace(string, "")
#     for string in ["Firefox", "vim", "fish", "Obsidian", "pacman"]:
#         if string in text:
#             text = string
#     return text


# This is probably not the best way to do this, but I can't get the
# minimizing behavior without it declared out here like this so
tasklist = widget.TaskList(
    background=colors[0],
    foreground=colors[1],
    icon_size=30,
    font="Iosevka Nerd Font",
    fontsize=20,
    max_title_width=400,
    padding_x=5,
    highlight_method="block",
    borderwidth=0,
    # markup_minimized='<span foreground="#B07190">{}</span>',
    # markup_focused='<span foreground="#5A8CE8">{}</span>',
    # txt_minimized="",
    # txt_maximized="",
    # txt_floating="",
    parse_text=replace_text,
)
tasklist.mouse_callbacks = {
    "Button1": lambda: tasklist.clicked.cmd_toggle_minimize(),
    "Button3": lambda: tasklist.clicked.cmd_kill(),
}
tasklist2 = widget.TaskList(
    background=colors[0],
    foreground=colors[1],
    icon_size=30,
    font="Iosevka Nerd Font",
    fontsize=20,
    max_title_width=400,
    padding_x=5,
    highlight_method="block",
    borderwidth=0,
    # markup_minimized='<span foreground="#B07190">{}</span>',
    # markup_focused='<span foreground="#5A8CE8">{}</span>',
    # txt_minimized="",
    # txt_maximized="",
    # txt_floating="",
    parse_text=replace_text,
)
tasklist2.mouse_callbacks = {
    "Button1": lambda: tasklist2.clicked.cmd_toggle_minimize(),
    "Button3": lambda: tasklist2.clicked.cmd_kill(),
}


def init_widgets_list():
    widgets_list = [
        widget.Spacer(length=2, background=colors[0]),
        # Left Side of the bar
        widget.GroupBox(
            font="Iosevka Nerd Font",
            fontsize=25,
            foreground=colors[2],
            background=colors[0],
            borderwidth=15,
            highlight_method="text",
            this_current_screen_border=colors[5],
            active=colors[3],
            inactive=colors[4],
        ),
        widget.Sep(linewidth=3, margin=5, background=colors[0]),
        tasklist,
        # Center bar
        widget.TextBox(
            font="Iosevka Nerd Font",
            fontsize=25,
            text=" ",
            foreground=colors[5],
            background=colors[0],
        ),
        widget.CurrentLayout(foreground=colors[2], background=colors[0]),
        widget.Sep(linewidth=3, background=colors[0]),
        widget.TextBox(
            font="Iosevka Nerd Font",
            fontsize=25,
            text="﬙",
            foreground=colors[6],
            background=colors[0],
        ),
        widget.CPU(
            format="{load_percent}%",
            foreground=colors[2],
            background=colors[0],
            update_interval=2,
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("alacritty -e gtop")},
        ),
        widget.TextBox(
            font="Iosevka Nerd Font",
            fontsize=25,
            text="",
            foreground=colors[5],
            background=colors[0],
        ),
        widget.Memory(
            format="{MemUsed: .2f}GB /{MemTotal: .2f}GB",
            foreground=colors[2],
            background=colors[0],
            measure_mem="G",
            update_interval=2,
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("alacritty -e gtop")},
        ),
        widget.Sep(linewidth=3, background=colors[0]),
        widget.TextBox(
            font="Iosevka Nerd Font",
            fontsize=25,
            text=" ",
            foreground=colors[8],
            background=colors[0],
        ),
        widget.GenPollText(
            foreground=colors[2],
            background=colors[0],
            update_interval=5,
            func=lambda: subprocess.check_output(
                f"{home}/.config/qtile/scripts/num-installed-pkgs"
            ).decode("utf-8"),
        ),
        # Right Side of the bar
        widget.Spacer(length=bar.STRETCH, background=colors[0]),
        widget.TextBox(
            font="Iosevka Nerd Font",
            fontsize=15,
            text=" ",
            foreground=colors[5],
            background=colors[0],
        ),
        widget.Net(
            format="{down} ↓↑ {up}",
            foreground=colors[2],
            background=colors[0],
            update_interval=2,
        ),
        widget.Sep(size_percent=60, linewidth=3, background=colors[0]),
        widget.TextBox(
            font="Iosevka Nerd Font",
            fontsize=15,
            text=" ",
            foreground=colors[7],
            background=colors[0],
        ),
        widget.Clock(format="%b %d-%Y", foreground=colors[2], background=colors[0]),
        widget.TextBox(
            font="Iosevka Nerd Font",
            fontsize=15,
            text=" ",
            foreground=colors[7],
            background=colors[0],
        ),
        widget.Clock(format="%I:%M:%S %p", foreground=colors[2], background=colors[0]),
        widget.Systray(background=colors[0]),
        widget.Spacer(length=5, background=colors[0]),
    ]
    return widgets_list


def init_widgets_list_secondary():
    widgets_list = [
        widget.Spacer(length=2, background=colors[0]),
        # Left Side of the bar
        widget.GroupBox(
            font="Iosevka Nerd Font",
            fontsize=25,
            foreground=colors[2],
            background=colors[0],
            borderwidth=15,
            highlight_method="text",
            this_current_screen_border=colors[5],
            active=colors[3],
            inactive=colors[4],
        ),
        widget.Sep(linewidth=3, margin=5, background=colors[0]),
        tasklist2,
        widget.TextBox(
            font="Iosevka Nerd Font",
            fontsize=25,
            text=" ",
            foreground=colors[5],
            background=colors[0],
        ),
        widget.CurrentLayout(foreground=colors[2], background=colors[0]),
        widget.Spacer(length=bar.STRETCH, background=colors[0]),
        widget.TextBox(
            font="Iosevka Nerd Font",
            fontsize=25,
            text="⏻ ",
            foreground=colors[5],
            background=colors[0],
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("shutdown -h now")},
        ),
        widget.Spacer(length=10, background=colors[0])
        # Right side of Bar
    ]
    return widgets_list


# screens/bar
def init_screens():
    return [
        Screen(
            top=bar.Bar(
                widgets=init_widgets_list(), size=40, opacity=1, margin=[0, 0, 10, 0]
            ),
            left=bar.Gap(3),
            right=bar.Gap(3),
            bottom=bar.Gap(10),
        ),
        Screen(
            top=bar.Bar(
                widgets=init_widgets_list_secondary(),
                size=40,
                opacity=1,
            ),
            left=bar.Gap(3),
            right=bar.Gap(3),
            bottom=bar.Gap(10),
        ),
    ]


screens = init_screens()

#### END
# }}}
# MOUSE CONFIGURATION{{{
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
]
# }}}
# OTHER CONFIG{{{
dgroups_key_binder = None
dgroups_app_rules = []

main = None


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/scripts/autostart.sh"])


@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(["xsetroot", "-cursor_name", "left_ptr"])


@hook.subscribe.client_new
def set_floating(window):
    if (
        window.window.get_wm_transient_for()
        or window.window.get_wm_type() in floating_types
    ):
        window.floating = True


floating_types = ["notification", "toolbar", "splash", "dialog"]

follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
# }}}
# APP GROUP ASSIGNMENTS{{{
@hook.subscribe.client_new
def move_spawned_apps(client):
    d = {}
    d["1"] = []
    d["2"] = ["Firefox", "firefox", "Navigator"]
    d["3"] = ["obsidian"]
    d["4"] = []
    d["5"] = ["spotify", "Spotify"]
    d["6"] = []
    d["7"] = ["Steam", "steam"]
    d["8"] = ["zoom"]
    d["9"] = []

    wm_class = client.window.get_wm_class()[0]
    for i in range(len(d)):
        if wm_class in list(d.values())[i]:
            group = list(d.keys())[i]
            client.togroup(group)


# }}}
# FLOATING APPS{{{
floating_layout = layout.Floating(
    float_rules=[
        {"wmclass": "confirm"},
        {"wmclass": "dialog"},
        {"wmclass": "download"},
        {"wmclass": "error"},
        {"wmclass": "file_progress"},
        {"wmclass": "notification"},
        {"wmclass": "splash"},
        {"wmclass": "toolbar"},
        {"wmclass": "confirmreset"},
        {"wmclass": "makebranch"},
        {"wmclass": "maketag"},
        {"wmclass": "Arandr"},
        {"wmclass": "feh"},
        {"wmclass": "Galculator"},
        {"wname": "branchdialog"},
        {"wname": "Open File"},
        {"wname": "pinentry"},
        {"wname": "Steam Login"},
        {"wmclass": "ssh-askpass"},
        {"wmclass": "lxpolkit"},
        {"wmclass": "Lxpolkit"},
        {"wmclass": "yad"},
        {"wmclass": "Yad"},
        {"wmclass": "ulauncher"},
        {"wmclass": "Ulauncher"},
        {"wmclass": "zoom"},
    ],
    fullscreen_border_width=0,
    border_width=0,
)  # }}}
auto_fullscreen = False

focus_on_window_activation = "focus"  # or smart

wmname = "LG3D"
# vim: fdm=marker
