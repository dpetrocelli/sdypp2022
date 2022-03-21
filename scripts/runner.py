# Requirement : pip3 install python-dotenv
import io
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
    javaProjectPath = None

    def __init__ (self, javaProjectPath):
        self.getOs()
        self.javaProjectPath = javaProjectPath
        self.getJavaProjectName(self.javaProjectPath)
        
        
    def runCommands (self, args):
      
        return subprocess.run(args, shell=True, capture_output=True)

    def getOs (self):
        self.osPlatform = platform.system()
        print ("-----------------")
        print ("Running OS: {}".format(self.osPlatform))
        print ("-----------------")
        
    def getJavaProjectName(self, javaProjectPath):
        # [JPN 1] - Define arguments to be executed (empty array) 
        if (self.osPlatform == "Windows"):
            
            args=["cat", "{}\\pom.xml".format(javaProjectPath)]
            
            # Put stderr and stdout into pipes
            proc = subprocess.Popen(args, \
                    shell=True, \
                    stderr=subprocess.PIPE, \
                    stdout=subprocess.PIPE)
            
            return_code = proc.wait()
            print('Return code: {}'.format(return_code))
            # Read from pipes
            if (return_code == 0):
                for line in proc.stdout:
                    line = str(line.rstrip().decode('ascii'))
                    if (re.search("name", line)):
                        self.javaProjectName = line.split(">")[1].split("<")[0].strip()
                        break
                # for line in proc.stderr:
                #     print("stderr: " + str(line.rstrip().decode('ascii')))
            print (self.javaProjectName)
        else:
            print ("sarasa")
        #output = subprocess.run(["cat", "c:\\Users\\Vane\\GitHub\\sdypp2022\\Clase1\\pom.xml"], shell=True, check=True, stdout=subprocess.PIPE)
        # [JPN 2] - Run subprocess.run (capture output)
        
        # print('Return code: {}'.format(output.returncode))
        
        # # [JPN 3] - It's time to magic :D 
        # if (output.returncode == 0):
        #     #lines = output.stdout.decode("utf-8").splitlines()
        #     for line in io.TextIOWrapper(output.stdout, encoding="utf-8"):
        #    # while True:
        #         #line = output.stdout.readline()
            
        #         print (line)
        #         if re.search("name", line):
        #             self.javaProjectName = line.split(">")[1].split("<")[0].strip()
        #             break
        #         if not line:
        #             break
        
# 3 ways of parsing files  
# -> 1. ENV FILE
# -> 2. json input file 
# -> 3. sys.argv
                  
# INPUT Variables
#   Parameter 1: Get java folder path
#   Parameter 2: 
#   Parameter 3: 

env_variables = {}

# [CHECK 1] - if inline (SYS ARGV) env vars are defined 
if (len(sys.argv) > 1):
    print ("---------------------------------------")
    print ("SYS ARGV env vars are going to be used ")
    print ("---------------------------------------")
    
    for item in sys.argv[1:]:
        try:
            (key, value) = item.split("=")
            if (str(key).find('--') != -1):
                try:
                    env_variables[key[2:]] = value
                except:
                    print ("adding FAILED")
            else:
                print ("{} vs --arg1 -> key is bad formed".format(key))

        except:
            print (" {} item is in wrong format".format(item))
            exit(1)
    
# [CHECK 2] - if .env config file is created
elif (os.path.exists (os.getcwd()+"/.env")):
    print ("-------------------------------------")
    print (".env config file is going to be used ")
    print ("-------------------------------------")
    try:
        env_variables = dotenv_values(".env")
    except:
        print (".ENV file cannot being readed")
        exit(1)

# [CHECK 3] - if JSON config file is created
elif (os.path.exists (os.getcwd()+"/config.json")):
    print ("-------------------------------------")
    print ("JSON config file is going to be used ")
    print ("-------------------------------------") 
    try:
        with open("config.json", "r") as read_file:
            env_variables = json.load(read_file)
                    
    except:
        print ("JSON file cannot being readed")
        exit(1)
        
else:
    print ("no needed parameters has been set")
    exit (1) 


    
sb = ScriptBuilder(env_variables["JAVA_PROJECT_PATH"])
#print (sb.javaProjectName)
#sb.runCommands("ls -l")
#cp = subprocess.run(["ls -lha"],shell=True)




