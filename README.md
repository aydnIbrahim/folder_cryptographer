# 🔒 Folder Cryptographer

**Folder Cryptographer**, kullanıcıların belirlediği bir **şifre** ile klasörleri **şifreleyerek sıkıştıran** bir **GUI tabanlı** Python uygulamasıdır. 

🚀 **Özellikler:**
- 📂 **Klasör Şifreleme**: Kullanıcı tarafından belirlenen bir şifre ile klasör içeriği şifrelenir.
- 🔑 **Güvenli Şifreleme**: PyCryptodome kütüphanesi ile güçlü şifreleme algoritmaları kullanır.
- 📦 **Sıkıştırma (ZIP Formatında)**: Şifrelenmiş klasörü `.zip` formatında arşivler.
- 🖥️ **Kolay Kullanım (GUI Tabanlı)**: PyQt6 ile tasarlanmış görsel arayüz sayesinde terminal kullanımı gerektirmez.

---

### **1️⃣. Projeyi GitHub'dan Klonlayın**
İlk olarak, projeyi bilgisayarınıza indirin:

```sh
git clone https://github.com/aydnIbrahim/folder_cryptographer.git
cd folder_crytographer
```
📌 **Alternatif:** Eğer Git kullanmıyorsanız, **"Download ZIP"** seçeneği ile projeyi manuel olarak indirip açabilirsiniz.

---

### **2️⃣. Sanal Ortam (Virtual Environment) Oluşturun**
Bağımlılıkları izole etmek için sanal ortam oluşturmanız önerilir.

✅ **Windows için:**
```sh
python -m venv venv
venv\Scripts\activate
```
---

### **3️⃣. Bağımlılıkları Yükleyin**
Gerekli kütüphaneleri yüklemek için aşağıdaki komutu çalıştırın:

```sh
pip install -r requirements.txt
```
---

### **4️⃣. Uygulamayı Çalıştırın**
Şimdi uygulamayı başlatabilirsiniz:

✅ **Windows için:**
```sh
python app.py
```

📌 **Not:** Eğer GUI açılmazsa, eksik bağımlılık olup olmadığını kontrol edin:  
```sh
pip list
```

---

## 📚 **Bağımlılıklar**
Bu proje aşağıdaki Python kütüphanelerini kullanmaktadır:

- **PyQt6** → GUI Arayüzü için
- **Pycryptodome** → Şifreleme işlemleri için
- **Pycryptodomex** → Alternatif şifreleme kütüphanesi
- **PyZipper** → Şifrelenmiş ZIP dosyaları oluşturmak için

📌 Eğer bağımlılık yükleme sırasında sorun yaşarsanız, aşağıdaki komutlarla manuel yükleme yapabilirsiniz:

```sh
pip install pyqt6 pycryptodome pycryptodomex pyzipper
```