#!/bin/bash
cp -r ./dns-app /opt/
echo '#!/bin/bash' | sudo tee /usr/local/bin/dns-changer
echo 'sudo python3 /opt/dns-app/DNS.py' | sudo tee -a /usr/local/bin/dns-changer
chmod +x /usr/local/bin/dns-changer
echo "Installation complete. You can now run the program by typing 'dns-changer' in the terminal."
