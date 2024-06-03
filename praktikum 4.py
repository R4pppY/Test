# #overriding
# class Hero:

#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
        
#     def info(self):
#         print(f"Nama = {self.name} \nhealth = {self.health} ")

# class Stat_str(Hero):
#     def __init__(self, name):
#         super().__init__(name, 100)

#     def info(self):
#         print(f"Nama = {self.name} \nhealth")

# Ares = Stat_str("Ares")
# Ares.info()



# #overloading
# class Hero:

#     def __init__(self, name, health):
#         self.name = name
#         self.health = health

#     def info(self, tipe):
#         print(f"Nama = {self.name} \nhealth = {self.health}\nTipe = {tipe}")


# class Stat_str(Hero):
#     def __init__(self, name):
#         super().__init__(name, 100)


#     def info(self, tipe):
#         super().info("strenght")


# class Stat_dex(Hero):
#     def __init__(self, name):
#         super().__init__(name, 90)

#Overriding dan overloading

class Hero:

    def __init__(self,name,health):
        self.name = name
        self.health = health
    
    def info(self,tipe):
        print(f"Nama = {self.name} \nhealth = {self.health}\nTipe = {tipe}")
        
class Stat_str(Hero):
    def __init__(self, name):
        super().__init__(name, 100)
        # self.tipe = "Strenght"

    def info(self,tipe):
        # super().info("Strenght")
        print(f"Nama = {self.name} \nhealth = {self.health}\nTipe = {tipe}")

class Stat_dex(Hero):
    def __init__(self, name):
        super().__init__(name, 90)
        
    def info(self):
        super().info("Dex")

Ares = Stat_str("Ares")
Ares.info("Strenght")

print("="*25)

Hermes = Stat_dex("Hermes")
Hermes.info()