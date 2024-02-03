Nautilus trash-cli extension
==============

Nautilus trash-cli is a simple Python extension for the Nautilus file manager that
adds basic integration for [trash-cli](https://github.com/andreafrancia/trash-cli) 
command line utility to the right-click menu:

*   **Delete using trash-put**: moves selected file to trash using trash-put.
*   **Restore using trash-restore**: opens a terminal window with trash-restore
    for current direstory, where user can select file to restore. Curently script
    is able to launch kgx, gnome-terminal or xterm to perform that

### Motivation

There's currently some bug causing trash to not work on mounted btrfs subvolumes. 
The ```gio trash``` command, which Nautilus is using in the background to manage trash command 
results in error ```Trashing on system internal mounts is not supported```.
There is an open issue on Gnome gitlab ([#1885](https://gitlab.gnome.org/GNOME/glib/-/issues/1885)),
but for now no change in this manner is visible. This script fixes that problem partialy, by
using ```trash-cli``` instead.

## Install Extension

```
wget -qO- https://raw.githubusercontent.com/Kiszczomb/nautilus-trash-cli/main/install.sh | bash
```

## Uninstall Extension

```
rm -f ~/.local/share/nautilus-python/extensions/code-nautilus.py
```
