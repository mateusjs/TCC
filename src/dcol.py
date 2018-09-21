import subprocess
import sys
import os


class Dcol:

    def DcolI(caminho, arquivo, nome_final):
        if sys.platform == "linux":
            subprocess.call(["ls", "-l"])
        elif sys.platform == "darwin":
            subprocess.call("ls")
        elif sys.platform == "win32":
            subprocess.call("DCOL.exe -i " + arquivo + " -o " + nome_final + " -F 1 -F 2 -F 3 -F 4 -L 1 -L 2 -L 3 -N 1 "
                                                                             "-N 2 -N 3 -N 4 -T 1 -d", shell=True, cwd=caminho,
                            stdout=open(os.devnull, 'wb'))