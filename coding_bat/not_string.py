def not_string(str):
  if "not" == str[:3]:
    return str
  else:
    return "not " + str

print(not_string("not go"))