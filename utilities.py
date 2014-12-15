
def mkmove(f):
  def new_f(*args, **kwds):
  	if args[0]._turn_up:
  		print "Cannot", f.func_name, "your turn is up."
  	else:
  		args[0]._turn_up = True
  		return f(*args, **kwds)
  new_f.func_name = f.func_name
  return new_f
