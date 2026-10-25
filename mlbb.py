class HeroML:
    def __init__(self, nama, role, hp, physical_attack):
        self.nama = nama
        self.role = role
        self.hp = hp
        self.max_hp = hp
        self.physical_attack = physical_attack
        self.is_alive = True

    def serang(self, target):
        if not self.is_alive:
            print(f"{self.nama} sudah tereliminasi, tidak bisa menyerang!")
            return
        
        print(f"{self.nama} menyerang {target.nama} dengan basic attack!")
        target.terima_damage(self.physical_attack)

    def terima_damage(self, jumlah_damage):
        self.hp -= jumlah_damage
        print(f"{self.nama} menerima {jumlah_damage} damage. Sisa HP: {max(0, self.hp)}/{self.max_hp}.")
        
        if self.hp <= 0:
            self.hp = 0
            self.is_alive = False
            print(f"You have been slain! {self.nama} berhasil dieliminasi.")

    def recall(self):
        if not self.is_alive:
            print(f"{self.nama} sedang menunggu waktu respawn, tidak bisa recall!")
            return
        
        self.hp = self.max_hp
        print(f"{self.nama} berhasil recall ke altar. HP kembali penuh ({self.max_hp}/{self.max_hp}).")

    def tampil_status(self):
        kondisi = "Hidup" if self.is_alive else "Tumbang (Respawn)"
        print("=== STATUS HERO ===")
        print(f"Hero   : {self.nama} ({self.role})")
        print(f"HP     : {self.hp}/{self.max_hp}")
        print(f"Attack : {self.physical_attack}")
        print(f"Status : {kondisi}")
        print("===================")

# --- PENGUJIAN SISTEM ---
hero1 = HeroML("Granger", "Marksman", 2400, 260)
hero2 = HeroML("Layla", "Marksman", 2000, 200)

hero1.tampil_status()
hero1.serang(hero2)
hero2.serang(hero1)
hero1.recall()
hero1.tampil_status()