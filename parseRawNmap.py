import sys, re, os, hashlib

environmentKey='secretsalt'

try:
    os.environ[environmentKey]
except KeyError:
    print "first you need to define envorniment variable secret salt (export ", environmentKey, "=blahhh)"
    exit()

with open(sys.argv[1]) as f:  
   line = f.readline()
   while line:
       line = f.readline()
       if(line.startswith('Starting Nmap')):
           dateMatch = re.search('\d{4}-\d{2}-\d{2} \d{2}:\d{2} GMT', line)
       macMatch = re.search('([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})', line)
       if(macMatch):
           anonymizedMac = hashlib.md5(macMatch.group() + os.environ[environmentKey]).hexdigest()
           print '{}; {}'.format(dateMatch.group(), anonymizedMac)
