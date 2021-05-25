#Program için gerekli kütüphaneler alındı
from PIL import Image, ImageDraw
import face_recognition as fr
# Load_image_file ile image objesine istenilen fotoğraf tanımlanır
fotograf = fr.load_image_file("grup4.jpg")

# Fotoğraf içindeki var olan yüzlerin yüz hatlarının belirlenmesi için face_landmarks fonksiyonu kullanıldı ve listeye atandı.
yuz_hatlari = fr.face_landmarks(fotograf)

#Pillow kütüphanesi kullanılarak yeni bir fotoğraf oluşturulur ve image objesi yeni fotoğrafa eklenir
son_foto = Image.fromarray(fotograf)

#Image.draw fonksiyonu ve pil_image parametresi d'ye fonksiyon olarak tanımlanır, kolay yönetim sağlar ve değişmeyi engeller.
ciz = ImageDraw.Draw(son_foto)

#for döngüsü yüzleri bulunduran liste üstünde iterasyon yaparak lisete içindeki her eleman için döngüyü çalıştırır.
for cizgi in yuz_hatlari:
    #dictionary içinde değeleri alarak fotoğraf üstünde yüz hatları gösterme işlemi gerçekleştirir.
    for hat in cizgi.keys():
        ciz.line(cizgi[hat], width=3)

#hazırlanmış olan fotoğrafın gösterilmesi için show() fonksiyonu kullanılır.
son_foto.show()