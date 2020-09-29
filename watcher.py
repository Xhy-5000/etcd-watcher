import etcd3
import time

class etcd_watcher(object):
    def __init__(self, etcd_host, etcd_port):
        self.etcd_host = etcd_host
        self.etcd_port = etcd_port
        self.callback = None

    def create_client(self):
        etcd = etcd3.client(host = self.etcd_host, port = self.etcd_port)
        return etcd

    def set_update_callback(self, fn):
        '''set_update_callback sets the callback function that the watcher will call
        when the policy in DB has been changed by other instances.'''
        self.update_callback = fn

    def update_callback(self):

        print('callback called because casbin role updated')

    def update(self):
        '''update calls the update callback of other instances to synchronize their policy.
        It is usually called after changing the policy in DB, like enforcer.save_policy()'''
        etcd = etcd3.client(host = self.etcd_host, port = self.etcd_port)
        etcd.update(etcd.Member.peer_urls)

    def start_watch(self):
        '''start_watch is a goroutine that watches the policy change.'''
        etcd = etcd3.client(host=self.etcd_host, port=self.etcd_port)
        for key in etcd.getall():
            events_iterator, cancel = etcd.watch(key)
            for event in events_iterator:
                self.callback = event
                break
            cancel()
            if(self.callback != None):
                self.callback = str(etcd.get(key))
                break
