from flask import request, abort, jsonify

from app.tasks.routes import asyncrone
from app import auth, tokens, log
from . import base
from .utils import launch

import time

@auth.verify_token
def verify_token(token):
    if token in tokens:
        return token
    else:
        log.error('Unauthorize')


@base.route('/health')
def health():
    log.info('Ping Ready')
    return jsonify({"status": "ready"})


@base.route('/')
def status():
    return jsonify({'result': 'ready'}), 200


@base.route('/api/v1/mplaunch', methods=['POST', 'GET'])
#@auth.login_required
@asyncrone
def launchmpx():
    try:
        if (not request.json) or \
                (not 'mpname' in request.json) or \
                (not 'mpversion' in request.json) or \
                (not 'appname' in request.json) or \
                (not 'appprofil' in request.json) or \
                (not 'appparams' in request.json) or \
                (not 'projectname' in request.json):
            log.error('fields mpname|mpversion|appname|projectname must be in body POST  ')
            abort(400)
        mpname = request.json.get('mpname', 'N/A')
        mpversion = request.json.get('mpversion', "N/A")
        projectname = request.json.get('projectname', "N/A")
        appname = request.json.get('appname', "N/A")
        appprofil = request.json.get('appprofil', "N/A")
        appparams = request.json.get('appparams', "N/A")

        log.info(f'Market place launched {mpname}, {mpversion}, {projectname}, {appname}')
        launch(mpname, mpversion, projectname, appname, appprofil, appparams)

        return jsonify({'result': 'success'}), 201
    except Exception as e:
        log.error(e)
        return jsonify({'result': 'error'}), 500
