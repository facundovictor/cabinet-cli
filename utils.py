#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess
import tempfile

from configparser import ConfigParser


def get_content_from_editor():
    t = tempfile.NamedTemporaryFile(delete=True)
    try:
        editor = os.environ['EDITOR']
    except KeyError:
        editor = 'nano'
    subprocess.call([editor, t.name])

    # content = t.read().splitlines()
    b_content = t.read()
    t.close()

    # TODO: what encoding is the editor using?
    content = b_content.decode('utf-8')

    return content


def get_configs(path):
    config = ConfigParser()
    config.read(path)

    account_id = None
    vault_name = None
    if 'Credentials' in config:
        credentials = config['Credentials']
        account_id = credentials.get('account')
        vault_name = credentials.get('vault')

    return {
        'account_id': account_id,
        'vault_name': vault_name,
    }
