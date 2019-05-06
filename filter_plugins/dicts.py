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

class FilterModule(object):
  def filters(self):
    return {
     'pluck': pluck,
     'anywithattr': any_with_attr,
     'selectattr': select_attr
    }
