# Algunos comandos de vagrant
```
vagrant up
vagrant provision
vagrant ssh
```

Recordar que el código estára en `/vagrant`

# Algunos comandos de git
```
git status
git add <archivo>
git commit -m "<mensaje descriptivo del commit>"
git push origin <nombre de la rama>
git checkout <nombre de otra rama>
git checkot -b <nombre de una nueva rama>
git pull origin <nombre de una rama>
```

# Después del `vagrant ssh`
```
echo "export LC_ALL=C.UTF-8 \nexport LANG=C.UTF-8" >> .profile
exit
vagrant ssh
cd /vagrant
pip install -r requirements.txt
```
