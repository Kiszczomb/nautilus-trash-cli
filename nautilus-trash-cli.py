# Trash Cli Nautilus Extension
# 
# Prerequisites:
# - python-nautilus package installed
# - kgx, gnome-terminal or xterm installed (currently suported nad tested,
#   feel free to add your terminal emulator)
# 
# Installation:
# - place this file in ~/.local/share/nautilus-python/extensions/,
# - restart Nautilus by running "nautilus -q" 
# - enjoy :)
#
# This script is released to the public domain.

from gi.repository import Nautilus, GObject
from subprocess import call
import subprocess
import os

# path to trash-cli commandes
TRASH_PUT = 'trash-put'
TRASH_RESTORE = 'trash-restore'

# Prepare terminal emulators to accept arguments to execute inside them
TERMINALS = {"kgx" : "kgx", 
         "gnome-terminal" : "gnome-terminal --zoom=1.2 --geometry=128x16 --", 
         "xterm" : "xterm -r -e"}

class TrashPutExtension(GObject.GObject, Nautilus.MenuProvider):

    def launch_trash_put(self, menu, files):
        safepaths = ''
        args = ''

        for file in files:
            filepath = file.get_location().get_path()
            safepaths += '"' + filepath + '" '

        call(TRASH_PUT + ' ' + args + safepaths + '&', shell=True)

    def launch_trash_restore(self, menu, files):
        safepaths = ''
        args = ''

        for file in files:
            filepath = file.get_location().get_path()
            safepaths += '"' + filepath + '" '

        TERM = TERMINALS['xterm']
        # Find first terminal emulator from the list present in OS
        for term in TERMINALS:
            cmd = ['which', term]
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            o, e = proc.communicate()
            if proc.returncode == 0:
                TERM = TERMINALS[term]
                break
        
        call(TERM + ' ' + TRASH_RESTORE + ' ' + args + safepaths + ' &', shell=True)

    def get_file_items(self, *args):
        files = args[-1]
        item = Nautilus.MenuItem(
            name='TrashPut',
            label='Delete using ' + TRASH_PUT,
            tip='Deletes selected files using trash-put command'
        )
        item.connect('activate', self.launch_trash_put, files)

        return [item]
    
    def get_background_items(self, *args):
        file_ = args[-1]
        item = Nautilus.MenuItem(
            name='TrashRestore',
            label='Restore using trash-restore',
            tip='Lists available files to restore in current directory'
        )
        item.connect('activate', self.launch_trash_restore, [file_])

        return [item]
    

    

