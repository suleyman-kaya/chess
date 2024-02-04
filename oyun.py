from Satranc import Oyun, Tahta

tahta = Tahta()
oyun = Oyun(tahta_p = tahta.TahtaOlustur(), oyuncu_b_p = "Oyuncu 1", oyuncu_s_p = "Oyuncu 2")

oyun.tahtayi_goster()
oyun.hamle("a1", "b1")
oyun.tahtayi_goster()

"""
oyun.tahtayi_goster()
oyun.hamle("h4", "e7")
oyun.hamle("b1", "c1")
oyun.tahtayi_goster()
oyun.hamle("e7", "e1")
oyun.hamle("c1", "d1")
oyun.tahtayi_goster()
oyun.hamle("e1", "b1")
oyun.hamle("d1", "e1")
oyun.tahtayi_goster()
oyun.hamle("b1", "a1")
oyun.hamle("e1", "f1")
oyun.tahtayi_goster()
oyun.hamle("a1", "a5")
oyun.hamle("f1", "g1")
oyun.tahtayi_goster()
"""