def fibrabb(gen, ofs):
   if gen == 0:
      return 0
   if gen == 1:
      return 1
   else:
       pop = fibrabb (gen-1, ofs) + ofs *fibrabb(gen-2, ofs)
       return pop
   
print(fibrabb(32,3))
