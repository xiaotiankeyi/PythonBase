import os
import subprocess

os.system("G: && cd moco && java -jar moco-runner-0.12.0-standalone.jar http -p 5555 -c test.json")

a = os.popen("dir", 'r')
print(a.read())


a, b = subprocess.getstatusoutput("dir")
print(a, b)