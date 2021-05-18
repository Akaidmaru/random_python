def missing_char(str, n):
  c = ""
  count = 0
  for i in str:
    if i == str[n] and count < 1:
      count += 1
    else:
      c += i
  return c


def missing_char(str, n):
  front = str[:n]   # up to but not including n
  back = str[n+1:]  # n+1 through end of string
  return front + back

print(missing_char("reddmar", 3))

print(x[3:])