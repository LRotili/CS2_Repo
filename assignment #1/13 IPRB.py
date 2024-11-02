hdom = 25
heter = 16
hrec = 23
pop = hdom + heter + hrec

p_dom_phen = 1 - (1/4*heter*(heter-1) + 1/2*heter*hrec + 1/2*heter*hrec + hrec*(hrec-1))/(pop*(pop-1))

print(p_dom_phen)