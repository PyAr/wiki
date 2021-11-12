# Script used to pull the repository and if needed run nikola 
# to update the changes

import os
import shutil
import subprocess

from flask import Flask

REPO_URL = os.environ.get('REPO_URL', 'https://github.com/PyAr/wiki.git')
BRANCH_NAME = os.environ.get('BRANCH_NAME', 'master')
CLONE_PATH = os.environ.get('CLONE_PATH', '/wiki_repo')
DESTINATION_PATH = os.environ.get('DESTINATION_PATH', '/usr/share/nginx/html')


import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration


sentry_dsn = os.environ.get('SENTRY_DSN')
if sentry_dsn:
    sentry_sdk.init(
        dsn=sentry_dsn,
        integrations=[FlaskIntegration()],

        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0,
    )

app = Flask(__name__)

@app.route("/_ping")
def ping():
	return {"succcess": 0}


@app.route("/_git_checkout")
def git_checkout():
    if not os.path.exists(CLONE_PATH):
        return {"succcess": 0, "error": "Repo not cloned"}
    os.chdir(CLONE_PATH)
    local_head = subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip()
    return {"succcess": 1, "local_commit": str(local_head)}


@app.route("/_update", methods=['GET', 'POST', 'PUT'])
def update():
    try:
        return {"succcess": 1, "updated": update_repo()}
    except Exception as e:
        return {"succcess": 0, "error": str(e)}


@app.route("/_test_sentry")
def test_sentry():
    1 / 0

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
	
	shutil.copytree(os.path.join(CLONE_PATH, 'output'), DESTINATION_PATH, dirs_exist_ok=True)
	return should_build