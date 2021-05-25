#Program için gerekli kütüphaneler alındı
from PIL import Image, ImageDraw
import face_recognition as fr

# Fotoğraf dosyasını Numpy array olarak değişkene tanımlanmasını sağlar.
foto = fr.load_image_file("grup4.jpg")

#Fotoğraf içerisindeki yüz hatlarının alınması
yuz_hatlar = fr.face_landmarks(foto)
# Yeni boş fotoğraf oluşturulması
son_foto = Image.fromarray(foto)
# Döngü kullanılarak yüzlerin hatlarının bulunduğu liste üzerinde iterasyon yapılması
for yuz_hatlar in yuz_hatlar:
    # çiz fonksiyonunun tanımlanması
    ciz = ImageDraw.Draw(son_foto, 'RGBA')

    #Tanımlanan kaşlar üzerinde modifikasyon işlemi
    ciz.polygon(yuz_hatlar['left_eyebrow'], fill=(34, 54, 39, 76))
    ciz.polygon(yuz_hatlar['right_eyebrow'], fill=(34, 54, 39, 64))
    ciz.line(yuz_hatlar['left_eyebrow'], fill=(68, 27, 18, 75), width=1)
    ciz.line(yuz_hatlar['right_eyebrow'], fill=(39, 27, 39, 75), width=1)

    #Tanımlanan dudaklar üzerinde modifikasyon işlemi
    ciz.polygon(yuz_hatlar['top_lip'], fill=(85, 0, 0, 64))
    ciz.polygon(yuz_hatlar['bottom_lip'], fill=(255, 0, 0, 128))
    ciz.line(yuz_hatlar['top_lip'], fill=(45, 20, 0, 46), width=10)
    ciz.line(yuz_hatlar['bottom_lip'], fill=(75, 75, 30, 46), width=10)

    #Tanımlanan göz hatları üzerinde modifikasyon işlemi
    ciz.polygon(yuz_hatlar['left_eye'], fill=(49, 60, 125, 30))
    ciz.polygon(yuz_hatlar['right_eye'], fill=(44, 60, 125, 30))

    #Tanımlanan göz hatları üzerinde çizgi çizme işlemi
    ciz.line(yuz_hatlar['left_eye'] + [yuz_hatlar['left_eye'][0]], fill=(0, 0, 0, 110), width=2)
    ciz.line(yuz_hatlar['right_eye'] + [yuz_hatlar['right_eye'][0]], fill=(0, 0, 0, 110), width=2)
    #Oluşturulan fotoğrafın gösterilmesi
    son_foto.show()
