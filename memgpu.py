import os
import subprocess

try:
  user = raw_input('Username: ') #python2
except:
  user = input('Username: ') #python3
servers = ['10.29.208.7' + str(i) for i in range(3, 10)]
servers += ['10.29.208.5' + str(i) for i in range(2, 10)]

print('server\tAvail gpu mem')
for server in servers:
  queryGpu = ' "nvidia-smi --query-gpu=memory.free --format=csv,noheader"'
  proc = subprocess.Popen('ssh '+ user + '@' + server + queryGpu, stdout=subprocess.PIPE, shell=True)
  out, err = proc.communicate()
  if len(out):
    print(server + '\t' + str(int(out[:-5])))
  else:
    print(server + ' is unreachable')

