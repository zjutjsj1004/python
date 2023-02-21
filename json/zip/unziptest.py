import subprocess

unzip = subprocess.Popen("find . -name '*.zip' -exec sh -c 'unzip -d ${1%.*} $1' _ {} \;",shell=True)
unzip.wait()   