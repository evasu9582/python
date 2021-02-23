import pickle
with open('simple.json','w') as p:
    p.write("""{
                "brand": "Ford",
                "model": "Mustang",
                "year": 1964
            }""")

print(p)
with open('simple.json','r') as r:
    r.readlines()

print(r)
