# Configure Git-Bash in VSCODE ()

https://medium.com/danielpadua/git-bash-with-vscode-593d5998f6be
https://www.geeksforgeeks.org/how-to-integrate-git-bash-with-visual-studio-code/

# Configure GH Token to modify code and push it :)

## WAY 1 (Not recommended)
1. Login to GH 
2. Go to your profile (logo)
3. Go Settings
4. Developer settings
5. personal access tokens
6. new
7. name it -> full access
8. save your token :) 

# Now clean your current configure
```bash
git config --global user.name ""
git config --global user.email ""
git config -l
```
# Now configure your user (mail) and then paste the token
```bash
git config --global user.email "dmpetrocelli@gmail.com"
```

Lastly, to ensure the local computer remembers the token, we can enable caching of the credentials. This configures the computer to remember the complex token so that we dont have too.
```bash
git config --global credential.helper cache
#or 
git config credential.helper 'cache --timeout=<timeout>'
```
#If needed, you can later clear the token from the local computer by running
```bash
git config --global --unset credential.helper
```
## WAY 2 (How we are going to work :D )

. Debemos evaluar si está corriendo el servidor de ssh:
```bash
eval $(ssh-agent -s)
```

. Create ssh key with the following command
```bash
ssh-keygen -f ~/.ssh/id_rsa -t rsa -N '' -C "dmpetrocelli@gmail.com"
```

. add to .gitignore file
```bash
id_rsa.pub
id_rsa
id_dsa.pub
id_dsa
*.pem
*.key
```

. Create an SSH GitHub key. Go to github.com → Settings → SSH and GPG keys → New SSH Key. Now save your private key to your computer.
```bash

cat ~/.ssh/id_rsa
.....
Once added 
SSH
ssh-rsa-unlu-class
SHA256: xxxxx
Added on Mar 19, 2022
Never used — Read/write
```
. add to the credentials management
ssh-add ~/.ssh/id_rsa 

ssh -T git@github.com
Attempts to ssh to GitHub
bash'''
The authenticity of host 'github.com (20.201.28.151)' can't be established.
ECDSA key fingerprint is SHA256:p2QAMXNIC1TJYWeIOttrVc98/R1BUFWu3/LiyKgUfQM.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'github.com,20.201.28.151' (ECDSA) to the list of known hosts.
Hi dpetrocelli! You've successfully authenticated, but GitHub does not provide shell access.
'''
# runit
git config --global user.name "dpetrocelli"
git config --global user.email "dmpetrocelli@gmail.com"

git add . ; git commit -m "first push" ; git push



# wipu
git remote -v
git remote set-url origin git@github.com:dpetrocelli/sdypp2022.git

# Start Playing (CICD)
GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline.

GitHub proporciona máquinas virtuales Linux, Windows y macOS para que ejecutes tus flujos de trabajo o ..
NICE ->  puedes hospedar tus propios ejecutores auto-hospedados en tu propio centro de datos o infraestructura en la nube.

En tu repositorio, crea el directorio .github/workflows/ para almacenar tus archivos de flujo de trabajo. (x ej: .github/workflows/prueba.yml)

# Create pipeline to deploy to K8s

https://cloud.okteto.com/#/spaces/dpetrocelli
. 0/10 pods
. 5GB storage

OKTETO -> Developer Settings -> Personal Access Tokens -> 

Now github go to project () -> settings ->  secrets -> actions -> 

https://github.com/dpetrocelli/sdypp2022/actions/