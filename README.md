# etcd-watcher
The [Etcd](https://github.com/etcd-io/etcd) watcher for PyCasbin. Using [etcd3](https://pypi.org/project/etcd3/) to connect Etcd.
Aims to keep consistence between multiple Casbin enforcer instances.

## Installation

```
pip install etcd-watcher
```

## Simple Example

```python
from watcher import etcd_watcher

updater = etcd_watcher("/casbin" "http://127.0.0.1:2379")
print(updater.get('foo'))
updater.put('bar', 'doot')
print(updater.get('bar'))
updater.delete('bar')

```


### Getting Help

- [PyCasbin](https://github.com/casbin/pycasbin)

### License

This project is licensed under the [Apache 2.0 license](LICENSE).
