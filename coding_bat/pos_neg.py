def pos_neg(a, b, negative):
  if negative == True:
    if a < 0:
      if b < 0:
        return True
      else:
        return False
    else:
      return False
  else:
    if a < 0:
      if b < 0:
        return False
      else:
        return True
    elif a > 0:
      if b > 0:
        return False
      else:
        return True

        
print(pos_neg(-4, 5, True))