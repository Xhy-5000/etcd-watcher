import etcd
from unittest import TestCase
import casbin
import os
from watcher import etcd_watcher


def get_fixture(path):
    '''
    get model path
    '''
    dir_path = os.path.split(os.path.realpath(__file__))[0] + "/"
    return os.path.abspath(dir_path + path)

def test_watcher():
    updater = etcd_watcher("/casbin" "http://127.0.0.1:2379")
    '''updater represents the Casbin enforcer instance that changes the policy in DB.'''

    listener = etcd_watcher("/casbin" "http://127.0.0.1:2379")
    '''listener represents any other Casbin enforcer instance that watches the change of policy in DB.'''
    listener.set_update_callback()

def test_with_enforcer():
    pass