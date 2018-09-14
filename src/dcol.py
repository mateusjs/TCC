import subprocess
import sys


class Dcol:

    def DcolI(caminho, arquivo, nome_final):
        if sys.platform == "linux":
            subprocess.call(["ls", "-l"])
        elif sys.platform == "darwin":
            subprocess.call("ls")
        elif sys.platform == "win32":
            print(caminho + " -i " + arquivo + " -o " + nome_final + ".txt -A -d")
            subprocess.call("DCOL.exe -i " + arquivo + " -o " + nome_final + ".txt -A -d", shell=True, cwd=caminho)