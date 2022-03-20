# Requirement : pip install pyyaml
import json
import yaml
import sys
import os
import platform
import subprocess
import re

class ScriptBuilder:
    variable = None
    osPlatform = None
    javaProjectName = None

    def __init__ (self):
        self.getOs()
        self.getJavaProjectName()
        
    def runCommands (self, args):
        return subprocess.run(args, shell=True, capture_output=True)

    def getOs (self):
        self.osPlatform = platform.system()

    def getJavaProjectName(self):
        # [JPN 1] - Define arguments to be executed (empty array) 
        args=["cat ../pom.xml"]
        output = self.runCommands(args)
        
        # [JPN 2] - Run subprocess.run (capture output)
        print('###############')
        print('Return code: {}'.format(output.returncode))
        
        # [JPN 3] - It's time to magic :D 
        if (output.returncode == 0):
            lines = output.stdout.decode("utf-8").splitlines()
            
            for line in lines:
            
                if re.search("name", line):
                    self.javaProjectName = line.split(">")[1].split("<")[0].strip()
                  

sb = ScriptBuilder()
print (sb.javaProjectName)
#sb.runCommands()
#cp = subprocess.run(["ls -lha"],shell=True)




