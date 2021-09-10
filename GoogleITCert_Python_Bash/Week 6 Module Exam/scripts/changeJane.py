#!/usr/bin/env python3

import sys
import subprocess


with open( sys.argv[1] ) as file:

    file_content = file.readlines()

    oldName = [ line.strip().strip("\n") for line in file_content]
    print(oldName)
 
    newName = [ i.replace("jane", "jdoe") for i in oldName]
    print(newName)

    result = subprocess.run(["mv", ".."+oldName[0], ".."+newName[0]])
    result = subprocess.run(["mv", ".."+oldName[1], ".."+newName[1]])

    # for i in oldName:
    #     for j in newName:
    #         result = subprocess.run(["mv", ".."+i, ".."+j ])

#result = subprocess.run(["mv", ".."+str(oldName), ".."+str(newName)])

print(result.returncode)
print(result.stderr)
print(result.stdout)
            

