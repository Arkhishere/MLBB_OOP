class HeroML:
    def __init__(self, nama, role, hp, attack):
        self.nama = nama
        self.role = role
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.is_alive = True

    def serang(self, target):
        if self.is_alive == False:
            print(f"{self.nama} udah mati, ga bisa nyerang!")
            return
        
        print(f"{self.nama} nyerang {target.nama}!")
        target.terima_damage(self.attack)

    def terima_damage(self, damage):
        self.hp = self.hp - damage
        if self.hp <= 0:
            self.hp = 0
            self.is_alive = False
            print(f"{self.nama} kena hit {damage}. Sisa HP: {self.hp}")
            print(f"Yah, {self.nama} udah mati!")
        else:
            print(f"{self.nama} kena hit {damage}. Sisa HP: {self.hp}/{self.max_hp}")

    def recall(self):
        if self.is_alive == False:
            print(f"{self.nama} masih mati woy, ga bisa recall!")
            return
        
        self.hp = self.max_hp
        print(f"{self.nama} recall dulu ke base, hp penuh lagi!")

    def tampil_status(self):
        if self.is_alive == True:
            kondisi = "Masih Hidup"
        else:
            kondisi = "Mati (Nunggu Respawn)"
        
        print("Status Hero:")
        print(f"Nama   : {self.nama}")
        print(f"Role   : {self.role}")
        print(f"HP     : {self.hp}/{self.max_hp}")
        print(f"Attack : {self.attack}")
        print(f"Status : {kondisi}")
        print()


hero1 = HeroML("Granger", "Marksman", 2000, 250)
hero2 = HeroML("Claude", "Marksman", 1800, 200)

hero1.tampil_status()
hero1.serang(hero2)
hero2.serang(hero1)
hero1.recall()
hero1.tampil_status()