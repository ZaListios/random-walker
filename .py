# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*,cover
.hypothesis/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# IPython Notebook
.ipynb_checkpoints

# pyenv
.python-version

# celery beat schedule file
celerybeat-schedule

# dotenv
.env

# virtualenv
venv/
ENV/

# Spyder project settings
.spyderproject

# Rope project settings
.ropeproject

from turtle import *
import math, random
ht()
penup()
setpos(100,100)
pendown()
setpos(100,-100)
setpos(-100,-100)
setpos(-100,100)
setpos(100,100)
penup()
setpos(0,0)
pendown()
while 1:
    yval = ycor()
    xval = xcor()
    a=random.randint(0, 3)
    if a == 0:
        pencolor("#ff0000")
        sety(yval+1)
    elif a == 1:
        pencolor("#00ff00")
        setx(xval+1)
    elif a == 2:
        pencolor("#0000ff")
        sety(yval-1)
    else:
        pencolor("#ff00ff")
        setx(xval-1)
    if xcor == 100:
        setx(-99)
    if ycor == 100:
        sety(-99)
    if xcor == -100:
        setx(99)
    if ycor == -100:
        sety(99)
