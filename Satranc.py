class Tahta:
    def __init__(self):
        self.a = ["[K]", "[A]", "[F]", "[V]", "[Ş]", "[F]", "[A]", "[K]"]
        self.b = ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"]
        self.c = [" - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "]
        self.d = [" - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "]
        self.e = [" - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "]
        self.f = [" - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "]
        self.g = ["{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}"]
        self.h = ["{K}", "{A}", "{F}", "{V}", "{Ş}", "{F}", "{A}", "{K}"]
        self.Sablon = [self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.h]
    
    def TahtaOlustur(self):
        return self.Sablon


class Oyun:
    def __init__(self, tahta_p: list, oyuncu_b_p: str, oyuncu_s_p: str):
        self.tahta = tahta_p
        self.oyuncu_b = oyuncu_b_p
        self.oyuncu_s = oyuncu_s_p
        self.b_oyuncusunun_yedigi_taslar = []
        self.s_oyuncusunun_yedigi_taslar = []

    def tahtayi_goster(self):
        """
        Kullanıcıya CLI'da tahtanın güncel durumunu gösterir
        """
        print(f"{self.oyuncu_b} tarafından yenilen taşlar:")
        b = self.b_oyuncusunun_yedigi_taslar
        print(*b, sep=", ")

        print("\n")

        print(f"{self.oyuncu_s} tarafından yenilen taşlar:")
        s = self.s_oyuncusunun_yedigi_taslar
        print(*s, sep=", ")

        print("\n")
        print("   1 - 2 - 3 - 4 - 5 - 6 - 7 - 8  ")
        print(" +-------------------------------+")

        i = 0
        liste = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}

        for satir in self.tahta:
            print(f"{liste[i]}" + "|"+' '.join(satir) + "|" + f"{liste[i]}")
            i += 1
        
        print(" +-------------------------------+")
        print("   1 - 2 - 3 - 4 - 5 - 6 - 7 - 8  ")
        print("\n")

    def cozumle(self, ifade: str) -> int:
        """
        a1, b2 gibi ifadelerdeki "a", "b", "c" ifadelerini tahta satırlarının
        indislerine dönüştürür.
        """
        liste = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7,}
        return liste[ifade]
    
    def hareket_kuralina_uyuyor_mu(self, tas: str, nereden: str, nereye: str) -> bool:
        satir_rf = self.cozumle(nereden[0])
        sutun_rf = int(nereden[1]) - 1

        satir_hedef = self.cozumle(nereye[0])
        sutun_hedef = int(nereye[1]) - 1
        
        # Kontrol edildi ✔
        if(tas[1] == "K"):
            if(satir_rf == satir_hedef or sutun_rf == sutun_hedef):
                return True
        
        # Kontrol edildi ✔
        elif(tas[1] == "A"):
            if(
                (abs(satir_rf - satir_hedef) == 2 and abs(sutun_rf - sutun_hedef) == 1)
                or
                (abs(satir_rf - satir_hedef) == 1 and abs(sutun_rf - sutun_hedef) == 2)
            ):
                return True

        # Kontrol edildi ✔  
        elif(tas[1] == "F"):
            if(
                abs(satir_rf - satir_hedef) == abs(sutun_rf - sutun_hedef)    
            ):
                return True

        # Kontrol edildi ✔   
        elif(tas[1] == "V"):
            if(
                (abs(satir_rf - satir_hedef) == abs(sutun_rf - sutun_hedef)) is not
                (satir_rf == satir_hedef or sutun_rf == sutun_hedef)
            ):
                return True

        # Kontrol edildi ✔   
        elif(tas[1] == "Ş"):
            if(
                (satir_rf == satir_hedef + 1) or (satir_rf == satir_hedef - 1)
                or
                (sutun_rf == sutun_hedef + 1) or (sutun_rf == sutun_hedef - 1)
            ):
                return True

        # Kontrol edildi ✔  
        elif((tas[0] == "[") and (tas[1] == "p")):
            if(satir_hedef - satir_rf == 1):
                return True
            
        elif((tas[0] == "{") and (tas[1] == "p")):
            if(satir_rf - satir_hedef == 1):
                return True
            
        else:
            return False

    def yiyebiliyor_mu(self, swap1: str, swap2: str) -> bool:
        """
        İstenen hamlede taş yeniliyorsa yenir.
        """
        if(swap1[0] != swap2[0]):
            return True
        
    def kurali_kontrol_et(self, tas: str, nereden: str, nereye: str) -> bool:
        """
        İstenen hamle bütün kurallara uygunsa True döndürür.
        """
        hareket_kuralina_uyuyor_mu = self.hareket_kuralina_uyuyor_mu(tas, nereden, nereye)
        return hareket_kuralina_uyuyor_mu

    def hamle(self, nereden: str, nereye: str):
        """
        Nereden (orn.: "a1" = "01"): değiştirilen değer -> swap: nereye
        Nereye  (orn.: "g5" = "65"): neredekiyle değiş? -> swap: nereden
        """
        satir_rf = self.cozumle(nereden[0])
        sutun_rf = int(nereden[1]) - 1

        satir_hedef = self.cozumle(nereye[0])
        sutun_hedef = int(nereye[1]) - 1

        swap1 = eval(f"self.tahta[{satir_rf}][{sutun_rf}]")
        swap2 = eval(f"self.tahta[{satir_hedef}][{sutun_hedef}]")

        if(self.kurali_kontrol_et(swap1, nereden, nereye) and swap2 == " - "):
            self.tahta[satir_hedef][sutun_hedef] = swap1
            self.tahta[satir_rf][sutun_rf] = swap2

        elif(self.kurali_kontrol_et(swap1, nereden, nereye) and self.yiyebiliyor_mu(swap1, swap2)):
            if(swap1[0] == "["):
                self.s_oyuncusunun_yedigi_taslar.append(self.tahta[satir_hedef][sutun_hedef])
            
            elif(swap1[0] == "{"):
                self.b_oyuncusunun_yedigi_taslar.append(self.tahta[satir_hedef][sutun_hedef])
            
            self.tahta[satir_hedef][sutun_hedef] = swap1
            self.tahta[satir_rf][sutun_rf] = " - "

        else:
            print("\n\n\t[!] Hamleniz, satranç kurallarının dışında kalmaktadır.")
            print("\t[i] Lütfen gözden geçirin.\n\n")