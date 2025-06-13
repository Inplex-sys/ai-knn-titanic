```py
params = {} # It's a dict with all the user input
passengers = [[],[]] # It's a panda data frame

ai = AI({
  'passengers': passengers,
  'params': params
})
```

### Installation
Install the app on the server
```sh
user@domain:~# git clone https://github.com/SystemVll/ai-knn-titanic.git
user@domain:~# cd ./ai-knn-titanic/
user@domain:~# pip3 install requests
user@domain:~# python3 ./main.py
```
