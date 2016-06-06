import os
import sys
import subprocess
import string

filepath = "ruby_backup.txt"

try:
    cmd = "gem list --local"
    result = subprocess.check_output(cmd, shell=True)
    result = result.replace(" (", "%%")
    result = result.replace(")"," ")
    result = result.replace("\n", "##")

    f = open(filepath, 'wb')
    f.write("##")
    f.write(result)
    f.close()

    print "Ruby env backup success!"
except:
    print "Error: Ruby backup fail"
