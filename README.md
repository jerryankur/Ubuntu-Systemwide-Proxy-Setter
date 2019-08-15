# Ubuntu-Systemwide-Proxy-Setter
I worte down this python script to set systemwide proxy in Ubuntu with pre-authentication. Internet data will be tunneled through the proxy.

Usage:
1. Download the script to your local folder.
2. Open the terminal in the folder. (or through cd ./)
3. Run the script by command:
         sudo python setproxy.py
4. Choose 1 to set proxy, 2 to unset it
5. Enter host name, port and credentials. if your proxy is without credentials, leave the credential box empty and press return key
6. Proxy will be succesfully written to system. if execution gives error , run the script again and choose the 2 option to revert back all the settings back to default. Usually it will not give error, error can rarely arise possible due to any  missing system variable file.

Help:
It will be helpful for people who want to use proxy systemwide/globally in ubuntu with pre-authentication.

Working: apt,terminal,software center, wget , and all ubuntu apps 
Note: Browsers use ubuntu settings proxy. To use proxy in browsers like chrome/firefox , also set the proxy in your ubuntu settings.
