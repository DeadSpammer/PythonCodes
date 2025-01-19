import requests
from bs4 import BeautifulSoup

url = input("url : ")
aranan_kelime = input("Kelime : ")
max_uzunluk = 50


try:
        # Siteye HTTP isteği gönder
        response = requests.get(url)
        response.raise_for_status()  # HTTP isteği hatasını kontrol et

        # HTML içeriğini parse et
        soup = BeautifulSoup(response.text, 'html.parser')

        # Eşleşen metinleri listele
        bulunan_etiketler = []

        for tag in soup.find_all():
            # Aranan kelimeyi etiketin adı, sınıfı, id'si veya metni içinde ara
            if (aranan_kelime.lower() in tag.name.lower() or
                aranan_kelime.lower() in " ".join(tag.get('class', [])).lower() or
                aranan_kelime.lower() in tag.get('id', '').lower() or
                aranan_kelime.lower() in tag.text.lower()):
                
                # Etiketin metin içeriğini al
                etiket_metni = " ".join(tag.text.split())

                # Eğer metin boş değilse ve uzunluk filtresine uygunsa listeye ekle
                if etiket_metni and len(etiket_metni) <= max_uzunluk and len(etiket_metni) > 1:
                    bulunan_etiketler.append((tag.name,etiket_metni))

        # Sonuçları yazdır
        if bulunan_etiketler:
            print(f"'{aranan_kelime}' kelimesiyle eşleşen ve {max_uzunluk} karakteri geçmeyen metinler:")
            for i, (etiket,metin) in enumerate(bulunan_etiketler, 1):
                print(f"{i}.Etiket:<{etiket}> | Metin: {metin}\n")
        else:
            print(f"'{aranan_kelime}' kelimesiyle eşleşen uygun uzunlukta bir metin bulunamadı.")

except requests.exceptions.RequestException as e:
    print(f"Bir hata oluştu: {e}")