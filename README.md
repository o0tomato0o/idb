# cs373-idb


Database:

Company table:
1 Google
2 Oracle
3 Amazon
4 Facebook
5 Twitter
6 Linkedin
7 Tripadvisor
8 Ebay
9 Rackspace
10 Indeed//covered

Location table:
1 Austin,TX
2 Seattle
3 San Francisco
4 Los angles
5 New York
6 Boston
7 Dallas
8 Chicago
9 San Jose//covered

Language table:
1 Java
2 C/C++
3 PHP
4 Python
//covered

5 C#
6 Ruby
7 Html/CSS
8 Javascript

Skillset table:
1 Spring, J2EE, Hibernate
2 Mobile computing, IOS, Andriod
3 Network
4 Web, Html, javascript, CSS
5 Hadoop, big data
6 Database, SQL, NoSQL
//covered

Setting up the project locally:

1. Install virtualenv if not already installed with "pip install virtualenv". This should be done outside the repo.
2. Create a virtual environment with "virtualenv name" where name is the name of the environment.
3. run ". name/bin/activate". This is done everytime you want to work on the project locally.
4. Run "python setup.py develop". This will install all dependecies needed to lauch project.
5. Run "python programmerJobs.py". This launches the project.
6. In your browser, visit http://localhost:5000
7. To exit the virtual environment, just type "deactivate".

Accessing the remote server:

1. Go to http://www.rackspace.com/knowledge_center/article/connecting-to-a-server-using-ssh-on-linux-or-mac-os and follow the instruction under "Generate a new SSH key pair"
2. Email your id_rsa.pub file to kevinosvaldovalle@gmail.com (If you have security concerns, don't worry. There is a reason it's called a public key)
3. Once i've added the key to the server, you should be able to access the server via ssh through "ssh kvalle@104.130.229.90" (We can just use my account as everything is already set up there)
4. You should be prompted for a password, enter "redApple"
5. To work on the project run "workon virtualEnvironment"

Restarting the serving process on the server:
1. In the virtual environment run "ps -C python"
2. A process should return with a pid, usually this is a 3-5 digit number
3. Run "kill pid" where pid is the pid from above
4. Run "nohup python programmerJobs.py &"
5. You can control-c and exit the server now. 

Let me know if there is anything missing or unclear -Kevin
