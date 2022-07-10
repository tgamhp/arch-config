# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import os
import subprocess
import re

mod = "mod4"
terminal = guess_terminal()

@hook.subscribe.startup_once
def autostart():
    processes = [
        ['nitrogen', '--restore'],
        ['lxpolkit'],
        ['picom'],
        ['pasystray'],
        ['nm-applet'],
        ['kdeconnect-indicator'],
        ['flameshot'],
        ['fcitx5'],
        ['/usr/bin/syncthing', 'serve', '--no-browser'],
    ]

    for p in processes:
        subprocess.Popen(p)

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # USER DEFINED
    Key([mod], "space", lazy.spawn('dmenu_run -p "  Run  " -h 30 -bw 4 -l 10 -sb "#007acc" -fn "Noto Sans:regular:pixelsize=15"'),
        desc="application launcher"),
        
    Key([mod], "q", lazy.spawn('bash /home/ahmed/.scripts/power.sh'),
        desc="power menu"),
        
    Key([mod], "m", lazy.spawn('bash /home/ahmed/.scripts/man.sh'),
        desc="search man pages"),
   
    Key([mod],"f", lazy.spawn("firefox"), 
        desc="Firefox"),
    
    Key([mod],"e", lazy.spawn("pcmanfm"), 
        desc="file manager"),

    Key([mod],"a", lazy.spawn("anki"), 
        desc="Anki"),

    Key([],"XF86AudioRaiseVolume", lazy.spawn("bash /home/ahmed/.scripts/volumectl.sh up"), 
        desc="Raise volume"),

    Key([],"XF86AudioLowerVolume", lazy.spawn("bash /home/ahmed/.scripts/volumectl.sh down"), 
        desc="Lower volume"),

    Key([],"XF86MonBrightnessUp", lazy.spawn("bash /home/ahmed/.scripts/brightctl.sh up"), 
        desc="Increase brightness"),

    Key([],"XF86MonBrightnessDown", lazy.spawn("bash /home/ahmed/.scripts/brightctl.sh down"), 
        desc="Decrease brightness"),

    Key([],"XF86AudioMute", lazy.spawn("bash /home/ahmed/.scripts/volumectl.sh toggle"), 
        desc="Mute audio"),

    Key([],"Print", lazy.spawn("flameshot gui"), 
        desc="select screenshot area"),

    Key([mod],"p", lazy.spawn("keepassxc"), 
        desc="keepassxc"),

    Key([mod, "shift"],"p", lazy.spawn("killall keepassxc"), 
        desc="keepassxc"),
]

#groups = [Group(i) for i in "123456789"]
groups = [
    Group(name="1", label="", layout="columns",
          matches=[
              Match(wm_class="anki")
          ]),
    Group(name="2", label="", layout="columns",
          matches=[
              Match(wm_class="firefox")
          ]),
    Group(name="3", label="", layout="columns",
          matches=[
              Match(wm_class="Steam")
          ]),
    Group(name="4", label="", layout="columns",
          matches=[
              
          ]),
    Group(name="5", label="", layout="columns",
          matches=[
              Match(wm_class="Gimp")
          ]),
    Group(name="6", label="", layout="columns",
          matches=[
          ]),
    Group(name="7", label="", layout="columns",
          matches=[
          ]),
]

for group in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                group.name,
                lazy.group[group.name].toscreen(),
                desc="Switch to workspace {}".format(group.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                group.name,
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to workspace {}".format(group.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
		border_focus="#007acc", 
		border_normal="#000000",
		border_focus_stack=["#d75f5f", "#8f3d3d"], 
		border_width=4, 
		margin=[0, 8, 8, 8], 
		margin_on_single=[0,8,8,8],
	),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    ]

widget_defaults = dict(
    font="Noto Sans Display Bold", 
    fontsize=14,
    padding=8,
    foreground="#ffffff",
    fontshadow="#000000"
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(
		),
                widget.GroupBox(
			padding=8,
    			font="Noto Sans Display Bold", 
			block_highlight_text_color='#007aff',
			borderwidth=0,
			highlight_method='line',
			highlight_color="#423e4d",
			margin=5,
			fontsize=18,
			inactive='#444444',
			active='#ffffff',
			disable_drag=True,
			fontshadow="#000000",
			urgent_text="#ffff00"
                ),
                #widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                #widget.TextBox("default config", name="default"),
                widget.Systray(icon_size=25),
                widget.Clock(
			format="%I:%M %p",
			mouse_callbacks={
				"Button1":lazy.spawn("gsimplecal"),
				"Button3":lazy.spawn("gsimplecal"),
				"Button5":lazy.spawn("gsimplecal"),
				"Button4":lazy.spawn("killall gsimplecal"),
			}
		),
            ],
            32,
	    background="#211f26",
	    opacity=1.0,
	    margin=8,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.toggle_floating()),
]


layout_theme = {
    "border_width": 4,
    "border_focus": "#007acc",
    "border_normal": "#000000",
}


dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class='keepassxc'), 
        Match(wm_class='Gcolor3'),
        Match(wm_class="Steam"),
        Match(wm_class='fcitx5-config-qt'),
        Match(wm_class='Lxappearance'), 
        Match(wm_class='lightdm-gtk-greeter-settings'),
        Match(
		wm_class="anki",
		title=re.compile('Statistics'),
	),
        Match(
		wm_class="anki",
		title=re.compile('Preferences'),
	),
	Match(wm_class='io.elementary.calendar'),
	Match(wm_class='Places'),
    ],
    **layout_theme,
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True


# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
