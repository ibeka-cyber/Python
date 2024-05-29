import cv2 as cv
import pyttsx3

# pyttsx3 motorunu başlat
engine = pyttsx3.init()

# Kamera yakalama
cap = cv.VideoCapture(0)

# Cascade dosyasını yükleme
my_cascade = cv.CascadeClassifier(r"C:\Users\iremb\Desktop\train\classifier\cascade.xml")

# Yazı tipi seçimi
font1 = cv.FONT_HERSHEY_SIMPLEX

# Daha önce "Mavi kalem" yazısını söyleyip söylemediğimizi kontrol etmek için bir bayrak
said_flag = False

# Kamera açıksa döngüyü başlat
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Aynalama
    frame = cv.flip(frame, 1)
    
    # Gri tona çevirme
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    # Nesne algılama
    pencils = my_cascade.detectMultiScale(gray, 1.3, 7)
    
    # Algılanan nesneleri çerçeveleme ve etiketleme
    for (x, y, w, h) in pencils:
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv.putText(frame, "Mavi kalem", (x, y - 10), font1, 1, (0, 255, 0), 2, cv.LINE_AA)
        
        # "Mavi kalem" yazısını sesli olarak söyleme
        if not said_flag:
            engine.say("Blue pencil")
            engine.runAndWait()
            said_flag = True
    
    # Eğer "Mavi kalem" algılanmadıysa bayrağı sıfırla
    if len(pencils) == 0:
        said_flag = False
    
    # Görüntüyü gösterme
    cv.imshow("Mavi kalem", frame)
    
    # 'q' tuşuna basıldığında döngüyü sonlandır
    if cv.waitKey(1) == ord("q"):
        break

# Kaynakları serbest bırakma
cap.release()
cv.destroyAllWindows()
