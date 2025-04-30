'''class Post:
    def __init__(self,name, description,author, id):
        self.name=name
        self.description=description
        self.author=author
        self.id=id
post_a= Post("Vremenska prognoza", "Danas ce biti suncano,do 18 stepeni","Admin",1)
post_b=Post("Sport","Danas ce utakmica", "Admin",2)
print(post_a.name)
print(post_b.description)
print(type(post_a))'
'''
import math
class Krug:
    def __init__(self,poluprecnik):
        self.poluprecnik=poluprecnik
    def povrsina(self):
        return self.poluprecnik**2*math.pi
    def set_poluprecnik(self,poluprecnik):
        self.poluprecnik=poluprecnik
krug_1=Krug(5)
povrsina_krug_1=krug_1.povrsina()
print (povrsina_krug_1)        

        