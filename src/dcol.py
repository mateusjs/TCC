import subprocess
import sys


class Dcol(object):

    def DcolI(self):
        if sys.platform == "linux":
            subprocess.call(["ls", "-l"])
        elif sys.platform == "darwin":
            subprocess.call("ls")
        elif sys.platform == "win32":
            subprocess.call("DCOL.exe -i nome.arff -o cmpnome.txt -A -d", shell=True)
