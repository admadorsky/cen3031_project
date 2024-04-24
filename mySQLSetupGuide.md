Setting up MySQL on your system for Windows:

1. Go to https://dev.mysql.com/downloads/mysql/
2. Click to download the MSI installer
3. Skip Oracle login/signup (unless you wish to sign in)
4. Open when download finishes
5. A setup wizard should open for the MySQL server
6. Click agree and next until you reach "choose setup type"
7. Click "typical"
8. Click install and allow your computer to make changes
9. Leave "Run MySQL configurator" box checked and click finish
10. A MySQL configuration setup wizard should open
11. At the "welcome" and "data directory" steps click next
12. At the "type and networking" step make sure "config type" is set to "development computer" and make sure "TCP/IP" is selected for "connectivity"
13. For "accounts and roles" make up a root password and put it where prompted. You must save this password somewhere accessible!
14. For "windows service" make sure the "configure MySQL server as a windows service" box is checked and the "start MySQL server at system startup" box is also checked
15. "Standard system account" should be selected for "Run windows service as...."
16. For "server file permissions" make sure that "yes, grant full access...." is selected
17. For "sample databases" none need to be selected, click next
18. For "apply configuration" click execute and once done click next and finish
19. Go to your windows search bar and find "MYSQL 8.0 Command Line Client" and open it
20. Input the root password you saved somewhere and press enter
21. On our GitHub repo, find the "mySQLTablePrompt.txt" file and download it to your computer
22. Open the text file in notepad and do 'ctrl a' and 'ctrl c'
23. Then go back to the command line and paste, a window will pop up asking if you're sure you want to paste and you will paste anyway. You shouldn't need to press enter. 
24. Type "QUIT" and the command line will close
25. You should have a python compatible IDE on your computer with the latest version of python installed
26. Open your terminal in that IDE and run this command "pip install mysql-connector-python" and then "python.exe -m pip install --upgrade pip"
