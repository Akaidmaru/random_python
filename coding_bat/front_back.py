def front_back(str):
  if len(str) <= 1:
    return str
  else:
    x, y = str[0], str[len(str)-1]
    z = str[1:len(str)-1]
    x, y = y, x
    return x + z + y

print(front_back("ab"))