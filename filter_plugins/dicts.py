def pluck(collection, key, default=None):
  if default == None:
    return [el[key] for el in collection]
  else:
    return [el.get(key, default) for el in collection]

def any_with_attr(collection, key):
  return len(list(filter(lambda el: el.get(key, False), collection))) > 0

def select_attr(collection, key, value, default=None):
  if default == None:
    return [el for el in collection if el[key] == value]
  else:
    return [el for el in collection if el.get(key, default) == value]

def primary_ipv6_address(host):
  return next(address for address in host['all_ipv6_addresses'] if address.startswith('2'))

class FilterModule(object):
  def filters(self):
    return {
     'pluck': pluck,
     'anywithattr': any_with_attr,
     'selectattr': select_attr,
     'primaryipv6address': primary_ipv6_address
    }
