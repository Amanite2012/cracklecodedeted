
phrase1 = "?@  ^ç!^¤¨^ç|=^ç  [}+&^ç  ?@  &%:.  #!:.^ç{]  ^çç°^ç  °+<>(]¤¨|=:.!^  ù$^ç!^  ?@^ç+&{]^ç!^"
phrase2 = "?@^ç  /=^ç(]&%{]/=^ç  &%  ç°<>+&!^  ù$^ç!^  !^ç°&%><><  /=^ç  #!:.^ç{]  !^+&|=-§^ç:.ù$ù$^ç|=  ù$^ç!^  ?@<>+&^ç+&|=!^  (]^ç|=°+:."
dico = {}
for i in range (0, len(phrase2), 2):
    temp = phrase2[i]+phrase2[i+1]
    if temp not in dico:
        dico[temp] = None
for i in range (0, len(phrase1), 2):
    temp = phrase1[i]+phrase1[i+1]
    if temp not in dico:
        dico[temp] = None
dico["?@"] = "l"
dico["^ç"] = "e"
dico["  "] = " "

for i in range (0, len(phrase2), 2):
    temp = phrase2[i]+phrase2[i+1]
    print(dico[temp], end="")
print()
for i in range (0, len(phrase1), 2):
    temp = phrase1[i]+phrase1[i+1]
    print(dico[temp], end="")
print()