def fibd(gen,lifespan):
  serie = [1] + [0]*(lifespan-1)
  for i in range(gen-1):
    serie = [sum(serie[1:])] + serie[:-1]
  return sum(serie)

print(fibd(85, 20))