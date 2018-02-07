import os
import sys
import subprocess

if len(sys.argv) < 2:
  print('As argments, takes one or more files with a script to run per line')
if sys.argv[1] == '-h' or sys.argv[1] == '--help':
  print('As argments, takes one or more files with a script to run per line')
tasks = []
for i in range(1, len(sys.argv):
  tasks += open(sys.argv[i], 'r').readlines()
try:
  user = raw_input('Username: ') #python2
except:
  user = input('Username: ') #python3
servers = ['10.29.208.7' + str(i) for i in range(3, 10)]
servers += ['10.29.208.5' + str(i) for i in range(2, 10)]

while len(tasks) > 0:
  task = tasks.pop()

  foundAvailable = False
  while not(foundAvailable):
    if len(servers) == 0:
      print('No more available servers')
      print('Remaining tasks:')
      for t in tasks:
        print(t)
      open(sys.argv[1] + '.res', 'w').writelines()
      sys.exit()
    server = servers.pop()
    queryGpu = ' "nvidia-smi --query-gpu=memory.free --format=csv,noheader"'
    proc = subprocess.Popen('ssh ' + user + '@' + server + queryGpu, stdout=subprocess.PIPE, shell=True)
    out, err = proc.communicate()
    mem = int(out[:-5])
    if mem > 6000:
      foundAvailable = True
  
  os.system('ssh ' + user + '@' + server + task)
  print('Executed {} on {}'.format(task, server))

