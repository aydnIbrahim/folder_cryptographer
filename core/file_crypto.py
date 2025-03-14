import os
import shutil
import pyzipper
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

class FileCrypto:
    @staticmethod
    def encrypt_folder(folder_path: str, password: str):
        """
        Verilen klasörü şifreleyerek ZIP dosyası oluşturur ve orijinal klasörü siler.
        """
        zip_filename = folder_path.rstrip(os.sep) + ".zip"
        try:
            with pyzipper.AESZipFile(zip_filename, 'w', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as zipf:
                zipf.setpassword(password.encode())
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, folder_path)
                        zipf.write(file_path, arcname)
            
            shutil.rmtree(folder_path)  # Orijinal klasörü tamamen sil
            return True
        except Exception as e:
            return False

    @staticmethod
    def decrypt_folder(zip_filename: str, password: str) -> bool:
        """
        Şifreli ZIP dosyasını çözer ve orijinal klasörü geri yükler.
        Başarılı olursa True, hata oluşursa False döner.
        """
        if not zip_filename.endswith(".zip"):
            zip_filename += ".zip"

        if not os.path.exists(zip_filename):
            return False

        try:
            with pyzipper.AESZipFile(zip_filename, 'r') as zipf:
                zipf.setpassword(password.encode())
                
                # Şifre doğrulama
                if zipf.testzip():
                    return False
                
                extracted_folder = zip_filename.replace(".zip", "")
                zipf.extractall(extracted_folder)

            os.remove(zip_filename)  # ZIP dosyasını tamamen sil
            return True
        except (RuntimeError, Exception) as e:
            return False
