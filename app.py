# Script used to pull the repository and if needed run nikola 
# to update the changes

import os
import shutil
import subprocess

from flask import Flask

REPO_URL = os.environ.get('REPO_URL', 'https://github.com/PyAr/wiki.git')
BRANCH_NAME = os.environ.get('BRANCH_NAME', 'master')
CLONE_PATH = os.environ.get('CLONE_PATH', '/nikola2')


app = Flask(__name__)

@app.route("/update")
def update():
    try:
    	return {"succcess": 1, "updated": update_repo()}
    except Exception as e:
    	return {"succcess": 0, "error": str(e)}

def update_repo():
	force_build = False
	if not os.path.exists(CLONE_PATH):
		print("%s not found. Clonning repo" % CLONE_PATH)
		subprocess.check_call(['git', 'clone', REPO_URL, CLONE_PATH])
		force_build = True
	else:
		print("%s found" % CLONE_PATH)
		# the path might exists but there might be no .git folder. This
		# might happen if a new Wiki version was deployed
		if not os.path.exists(os.path.join(CLONE_PATH, '.git')):
			print("%s isn't a git repo. Clonning repo" % CLONE_PATH)
			force_build = True
			os.chdir('/')
			shutil.rmtree(CLONE_PATH)
			subprocess.check_call(['git', 'clone', REPO_URL, CLONE_PATH])

	os.chdir(CLONE_PATH)	
	should_build = False
	if force_build:
		should_build = True
	else:
		# git rev-parse HEAD
		# git ls-remote origin -h refs/heads/master
		local_head = subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip()
		remote_head = subprocess.check_output(['git', 'ls-remote', 'origin', '-h', 'refs/heads/master']).split()[0].strip()
		print("The git versions are: local:%s, remote:%s" % (local_head, remote_head))
		should_build = local_head != remote_head
		if should_build:
			print("Doing a git pull")
			subprocess.check_call(['git', 'pull'])

	if should_build:
		print("Building nikola")
		subprocess.check_call(['nikola', 'build'])
	else:
		print("No changes. Not buidling nikola")
	return should_build