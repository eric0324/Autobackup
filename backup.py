# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import string
import re

argv = sys.argv

#Processing backup path
cmd = "cat .config"
result = subprocess.check_output(cmd, shell=True)
path = re.split("DESDIR=([^\n]+)", result)

def allBackup():
    python()
    ruby()
    nodejs()
    git()
    atom()
    vim()

def python():
    filepath = path[1] + "/python"

    try:
        print "Start python backup",
        cmd = "pip list"
        result = subprocess.check_output(cmd, shell=True)
        result = result.replace(" (", "%%")
        result = result.replace(")"," ")
        result = result.replace("\n", "\n##")
        f = open(filepath, 'wb')
        f.write("##")
        f.write(result)
        f.close()

        print " ..done"
    except:
        print "Error: Python backup fail"

def ruby():
    filepath = path[1] + "/ruby"

    try:
        print "Start Ruby backup",
        cmd = "gem list --local"
        result = subprocess.check_output(cmd, shell=True)
        result = result.replace(" (", "%%")
        result = result.replace(")"," ")
        result = result.replace("\n", "\n##")

        f = open(filepath, 'wb')
        f.write("##")
        f.write(result)
        f.close()

        print " ..done"
    except:
        print "Error: Ruby backup fail"

def nodejs():
    filepath = path[1] + "/nodejs"

    try:
        print "Start NodeJS backup",

        cmd = "npm ls -g"
        result = subprocess.check_output(cmd, shell=True)
        result = result.replace("@", "%%")
        result2 = re.sub(r'((│|├|└)\s(┬|─|└|├|└)*)|((├|└)(┬|─|└|├|└)*)', "##", result)
        result = re.sub(r'(##)((\s)^|(##)*)*', "##", result2)
        result = result.replace("##  ##", "##")
        result = result.replace("##    ##", "##")
        result = result.replace("##      ##", "##")
        result = result.replace("  ## ", "##")
        result = result.replace("## ", "")
        result = result.replace("  /usr/local/lib", "")
        f = open(filepath, 'wb')
        f.write("  ")
        f.write(result)
        f.close()

        print "Start NodeJS backup ..done"
    except:
        print "Error: NodeJS backup fail"


def git():
    try:
        print "Start Git backup",
        cmd = "cp -p ~/.gitconfig "+ path[1] + "/git"
        result = subprocess.check_output(cmd, shell=True)
        print " ..done"
    except:
        print "Error: Git backup fail"


def atom():
    filepath = path[1] + "/atom"

    try:
        print "Start Atom backup",
        cmd = "apm list --bare"
        result = subprocess.check_output(cmd, shell=True)
        result = result.replace("@", "%%")
        result = result.replace("\n", "\n##")
        result = result.replace("####", "")
        f = open(filepath, 'wb')
        f.write("##")
        f.write(result)
        f.close()

        print " ..done"
    except:
        print "Error: Atom backup fail"

def vim():
    try:
        print "Start Vim backup",
    	cmd = "cp -p ~/.vimrc ~/env_backup/vim"
    	result = subprocess.check_output(cmd, shell=True)
    	print " ..done"
    except:
	print "Error: Vim backup fail"

#Main function


if argv[1] == '-all':
    allBackup()
elif argv[1] == '-python':
    python()
elif argv[1] == '-ruby':
    ruby()
elif argv[1] == '-nodejs':
    nodejs()
elif argv[1] == '-git':
    git()
elif argv[1] == '-atom':
    atom()
elif argv[1] == '-vim':
    vim()
