import sys
import getopt

def usage():
  print(r'python3 7argv.py --ip=127.0.0.1 --port=80 55 66')

try:
    options,args = getopt.getopt(sys.argv[1:],"hp:i:", ["help","ip=","port="])
except getopt.GetoptError:
    sys.exit()
for name,value in options:
    if name in ("-h","--help"):
        usage()
    if name in ("-i","--ip"):
        print ('ip is----',value)
    if name in ("-p","--port"):
        print ('port is----',value)


# python3 7argv.py -i 127.0.0.1 -p 80 55 66
# python3 7argv.py --ip=127.0.0.1 --port=80 55 66