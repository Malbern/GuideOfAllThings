##bashemail
pixel+%Y%m%d%H%M%S@gmail.com
##bashgitclean
git branch —merged | egrep -v “(^\*|master|dev|main)” | xargs git branch -d
##bashgitfix
git add . && git commit —amend —no-edit && git push origin $(git rev-parse —abbrev-ref HEAD) —force 
##bashportrun
lsof -i tcp:%filltext:name=port:width=20:default=8080%
##bashrandomemail
 #!/bin/bash

echo -n “pixel+$RANDOM@gmail.com”