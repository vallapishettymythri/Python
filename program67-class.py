class person:
    species="Human"
    def __init__(self,name):
        self.name=name
p1=person("Emil")
p2=person("Tobias")
print(p1.name,p2.name)
print(p1.species,p2.species)