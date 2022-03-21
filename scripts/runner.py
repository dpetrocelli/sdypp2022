# Requirement : pip3 install python-dotenv

import json
import sys
import os
import platform
import subprocess
import re
#1. ENV config FILE 
from dotenv import dotenv_values
#2. json config file
from collections import OrderedDict

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

# 3 ways of parsing files  
# -> 1. ENV FILE
# -> 2. json input file 
# -> 3. sys.argv
                  
# INPUT Variables
#   Get java folder path
#   



# Use the variable with:
import os
command = os.getenv("MVN_COMMAND")
print ("command {}".format(command))
env_variables = OrderedDict()

if (os.path.exists (os.getcwd()+"/.env")):
    print (".env config file exists")
    try:
        env_variables = dotenv_values(".env")
    except:
        print (".ENV file cannot being readed")
elif (os.path.exists (os.getcwd()+"/config.json")):
    print (".json config file exists ")    
    try:
        with open("config.json", "r") as read_file:
            env_variables = json.load(read_file, object_pairs_hook=OrderedDict)
                    
    except:
        print ("JSON file cannot being readed")
elif (len(sys.argv) > 1):
    print ("Sys argv variables has been defined")
    print (sys.argv)
    
    for item in sys.argv[1:]:
        try:
            (key, value) = item.split("=")
            
            if (key.find("is") == -1):
                print ("{} item has no valid format ".format(item) )
                break
            env_variables[key] = value
        except:
            print ("{} item has no valid format ".format(item) )
            exit(1)
    print (env_variables) 
else:
    print ("no needed parameters has been set")
    exit (1) 
    



    
# for k, v in ((k.lstrip('-'), v):
#     for k,v in (a.split('=') for a in sys.argv[1:])):
#     d[k].append(v)

# print dict(d)
# print ("Argument List:", str(sys.argv))
# if (len(sys.argv) < 2):
#     print ("base arguments has not been defined")
# else:
#     items = sys.argv.items()
# sb = ScriptBuilder()
# print (sb.javaProjectName)
#sb.runCommands()
#cp = subprocess.run(["ls -lha"],shell=True)




