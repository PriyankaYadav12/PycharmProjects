Oxford = { "lisa": "dancer", "jinny": "rap", "jisso": "vocal", "rose": "lead",
          "Gift": "Something given by this new years gift",
          "profit": "Here something profit from in this year",
          "youtube": "this is best app for anything foe anyone"
           }

# print(Oxford)
# print(Oxford["Gift"])
# for a, b in Oxford.items(): #items() print seperate and line to line
#    print(a,":=", b)

# for key in Oxford.keys(): #keys() print only key
#    print(key)

Oxford.update({"royal": "classes", "list" :[1, 2, 3, 4]})
for a, b in Oxford.items(): #items() print seperate and line to line
    print(a,":=", b)

