Nautilus trash-cli extension
==============

Nautilus trash-cli is a simple Python extension for the Nautilus file manager that
adds basic integration for [trash-cli](https://github.com/andreafrancia/trash-cli) 
command line utility to the right-click menu:

*   **Delete using trash-put**: moves selected file to trash using trash-put.
*   **Restore using trash-restore**: opens a terminal window with trash-restore
    for current direstory, where user can select file to restore. Curently script
    is able to launch kgx, gnome-terminal or xterm to perform that

## Install Extension

```
wget -qO- https://raw.githubusercontent.com/Kiszczomb/nautilus-trash-cli/main/install.sh | bash
```

## Uninstall Extension

```
rm -f ~/.local/share/nautilus-python/extensions/code-nautilus.py
```
