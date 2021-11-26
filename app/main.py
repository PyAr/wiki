# Script used to pull the repository and if needed run nikola
# to update the changes

import os
import shutil
import subprocess
import threading
import logging
import sys
from queue import Queue

from flask import Flask

import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    stream=sys.stdout
)

REPO_URL = os.environ.get("REPO_URL", "https://github.com/PyAr/wiki.git")
BRANCH_NAME = os.environ.get("BRANCH_NAME", "master")
CLONE_PATH = os.environ.get("CLONE_PATH", "/app/wiki_repo")
DESTINATION_PATH = os.environ.get("DESTINATION_PATH", "/usr/share/nginx/html")

sentry_dsn = os.environ.get("SENTRY_DSN")
if sentry_dsn:
    sentry_sdk.init(
        dsn=sentry_dsn,
        integrations=[FlaskIntegration()],
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0,
    )

# Como nota general todas las URLs empiezan con _ para asegurarme de
# que no haya conflicto con alguna pagina existente. Si se actualiza
# las URLs usadas en este archivo tambien se tiene que actualizar el
# nginx/defaults.conf que esta en este repo
app = Flask(__name__)
queue = Queue()


@app.route("/_update/async", methods=["GET", "POST", "PUT"])
def update_async():
    """Actualiza la wiki pero no espera para saber el resultado de la operacion.

    Este es el endpoint usado por github.
    """
    try:
        queue.put(1)
        return {"succcess": 1, "updated": "unknown"}
    except Exception as e:
        logging.exception("Error when calling update async")
        return {"succcess": 0, "error": str(e)}


@app.route("/_update/sync", methods=["GET", "POST", "PUT"])
def update_sync():
    """Actualiza la wiki pero espera el resultado de la misma.

    Este endpoint es para debug o por si lo queremos forzar.
    """
    try:
        return {"succcess": 1, "updated": update_wiki()}
    except Exception as e:
        logging.exception("Error when calling update sync")
        return {"succcess": 0, "error": str(e)}


def worker():
    while True:
        val = queue.get()
        try:
            update_wiki()
        except Exception as e:
            logging.exception("Error on woker")


def update_wiki():
    """Actualiza la wiki

    Para esto:
    1. Se clona el repo
    2. Hace un pull con los ultimos cambios
    3. Corre nikola
    4. Copia los archivos al path final
    """
    force_build = False
    if not os.path.exists(CLONE_PATH):
        logging.info(f"{CLONE_PATH} not found. Clonning repo")
        subprocess.check_call(["git", "clone", REPO_URL, CLONE_PATH])
        force_build = True
    else:
        logging.info(f"{CLONE_PATH} found")
        # the path might exists but there might be no .git folder. This
        # might happen if a new Wiki version was deployed
        if not os.path.exists(os.path.join(CLONE_PATH, ".git")):
            logging.info(f"{CLONE_PATH} isn't a git repo. Clonning repo")
            force_build = True
            os.chdir("/")
            shutil.rmtree(CLONE_PATH)
            subprocess.check_call(["git", "clone", REPO_URL, CLONE_PATH])
    os.chdir(CLONE_PATH)

    should_build = False
    if force_build:
        should_build = True
    else:
        # git rev-parse HEAD
        # git ls-remote origin -h refs/heads/master
        local_head = subprocess.check_output(["git", "rev-parse", "HEAD"]).strip()
        remote_head = (
            subprocess.check_output(
                ["git", "ls-remote", "origin", "-h", "refs/heads/master"]
            )
            .split()[0]
            .strip()
        )
        logging.info(f"The git versions are: local:{local_head}, remote:{remote_head}")
        should_build = local_head != remote_head
        if should_build:
            logging.info("Doing a git pull")
            subprocess.check_call(["git", "pull"])

    if not should_build:
        logging.info("No changes. Not buidling nikola")
        return False
           
    logging.info("Building nikola")
    subprocess.check_call(["nikola", "build"])

    logging.info("Copying files")  
    cmd = [
        "rsync",
        "-t",
        "-r",
        "--delete",
        "--inplace",
        os.path.join(CLONE_PATH, "output/"),
        DESTINATION_PATH,
    ]
    subprocess.check_call(cmd)
    return should_build


@app.route("/_debug/ping")
def ping():
    """Debug endpoint para testear que la webapp esta corriendo"""
    return {"succcess": 0}


@app.route("/_debug/test_sentry")
def test_sentry():
    """Debug endpoint para testear que sentry esta configurado"""
    1 / 0


@app.route("/_debug/git_commit")
def git_commit():
    """Debug endpoint para testear el utlimo commit que se esta usando."""
    if not os.path.exists(CLONE_PATH):
        return {"succcess": 0, "error": "Repo not cloned"}
    os.chdir(CLONE_PATH)
    local_head = subprocess.check_output(["git", "rev-parse", "HEAD"]).strip()
    return {"succcess": 1, "local_commit": str(local_head)}

threading.Thread(target=worker).start()
