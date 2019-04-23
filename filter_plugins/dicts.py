def pluck(collection, key, default=None):
  if default == None:
    return [el[key] for el in collection]
  else:
    return [el.get(key, default) for el in collection]

def any_with_attr(collection, key):
  return len(list(filter(lambda el: el.get(key, False), collection))) > 0

class FilterModule(object):
  def filters(self):
    return {
     'pluck': pluck,
     'anywithattr': any_with_attr
    }
