# Machine Learning Project

## Software Requirements:

1. [Github Account](https://github.com/)
2. [VS Code](https://code.visualstudio.com/download)

Creating Virtual Environment use either of the 2 commands
```
python3.10 -m venv <nameoftheenvironment>
virtualenv <nameoftheenvironment>
```
CD into the directory
```
cd <nameoftheenvironment>
```

Activate the environment. Use either of the two
```
source bin/activate
. bin/activate
```

Deactiavate the base environment
```
conda deactivate
```

To deactivate the virtual environment
```
deactivate
```

```
pip install -r requirements.txt
```
To add all the files to git
```
git add .
```
To commit changes to github with comments
```
git commit -m "<comment>"
```

To push all the changes to github
```
git push origin main
```

> Note: To ignore all the files and folders from github mention them in the .gitignore files


To setup CI/CD pipeline we need the following:
1. HEROKU_Email
2. HEROKU_API_KEY (From under settings, scroll down to get the API_KEy)
3. HEROKU_APP_NAME