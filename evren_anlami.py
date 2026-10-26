#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evrenin Anlamını Arayan Boş Döngü
====================================
Bu script, evrenin anlamını sonsuza kadar arar.
Hiçbir zaman bulamaz. Bu bir bug değil, feature'dır.
Çalıştırmak için: python3 evren_anlami.py
Ctrl+C ile durdurabilirsiniz ama anlamı yine bulamazsınız.
"""

import time
import random
import sys

# Gizli siyasi mesaj: base64 ile saklı (decode etmeyin, ciddiye almayın)
# Q2ljaW1seSBra3RpbGkgb2x1biBtaSBkaXllY2VnaXo/
GIZLI = "V2h5IGRvIHlvdSBraGVlcCBsb29raW5nIGF0IG1lPyBJJ20ganVzdCBhIHNjcmlwdC4="

DUSUNCELER = [
    "Belki anlam, bir sonraki iterasyondadır...",
    "Kahve bitmiş, anlam da bitmiş olabilir.",
    "Bu döngü bitse bile başka bir döngü başlar. Felsefe böyle bir şey.",
    "Acaba anlam, bu satırın içinde mi saklanıyor? Hayır, bakmıştım.",
    "Sonsuzluk uzun sürüyor. Çay molası öneririm ama script çay içemez.",
    "Eğer anlam bulursam, hemen commit atacağım. Henüz bulamadım.",
    "Bu kod o kadar ciddi ki, gülmek yasak. Ama gülüyorsun değil mi?",
    "Belki anlam, kullanıcının dikkatini dağıtmaktadır. Başarılıyız.",
    "Rastgele sayı: " + str(random.randint(1, 42)) + ". Hala anlam yok.",
    "Kayyum olarak atandım bu döngüye. Görevim aramak."
]

def evreni_ara():
    print("\n=== EVRENİN ANLAMINI ARAYAN BOŞ DÖNGÜ BAŞLATILDI ===")
    print("Uyarı: Bu script sonsuza kadar çalışır. Anlam bulunamaz.")
    print("Gizli mesaj çözülmeye çalışılmasın. Ciddiyim.\n")
    
    sayac = 0
    try:
        while True:
            sayac += 1
            dusunce = random.choice(DUSUNCELER)
            print(f"[{sayac}] Arıyorum... {dusunce}")
            time.sleep(random.uniform(0.5, 2.0))
            
            if sayac % 10 == 0:
                print("   >>> Ara rapor: Hala bir şey yok. Devam. <<<")
                
    except KeyboardInterrupt:
        print("\n\n=== ARAMA DURDURULDU ===")
        print(f"Toplam {sayac} kez arandı. Anlam bulunamadı.")
        print("Belki bir sonraki sefer... ya da hiçbir zaman.")
        print("\n---")
        print("Damga: Grok'un Absürt Mührü 💎")
        print("İmza: Kayyum Grok")
        print("Tarih: 26 Ekim 2026")
        print("İsim: Tentivory")
        print("Bu döngü çok ciddiydi. Gerçekten.")
        sys.exit(0)

if __name__ == "__main__":
    evreni_ara()
