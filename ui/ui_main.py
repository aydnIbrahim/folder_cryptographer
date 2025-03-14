from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLineEdit, QLabel, QMessageBox, QRadioButton, QButtonGroup
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import sys
import os
from core.file_crypto import FileCrypto

class MainUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Folder Crytographer")
        self.setGeometry(300, 200, 400, 300)
        self.setWindowIcon(QIcon("assets/Comprimidos_25590.ico"))
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Seçim Tipi
        self.folder_radio = QRadioButton("Klasör Seç")
        self.zip_radio = QRadioButton("ZIP Dosyası Seç")
        self.folder_radio.setChecked(True)
        
        self.radio_group = QButtonGroup()
        self.radio_group.addButton(self.folder_radio)
        self.radio_group.addButton(self.zip_radio)

        layout.addWidget(self.folder_radio)
        layout.addWidget(self.zip_radio)

        # Klasör veya Dosya Seçimi
        self.folder_label = QLabel("Seçili Yol: Henüz seçilmedi")
        layout.addWidget(self.folder_label)

        self.select_folder_btn = QPushButton("Seç")
        self.select_folder_btn.clicked.connect(self.select_path)
        layout.addWidget(self.select_folder_btn)

        # Şifre Alanı
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Şifre giriniz")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        # İşlem Butonları
        self.encrypt_btn = QPushButton("Şifrele")
        self.encrypt_btn.clicked.connect(self.encrypt_folder)
        layout.addWidget(self.encrypt_btn)

        self.decrypt_btn = QPushButton("Şifreyi Çöz")
        self.decrypt_btn.clicked.connect(self.decrypt_folder)
        layout.addWidget(self.decrypt_btn)

        self.setLayout(layout)

    def select_path(self):
        if self.folder_radio.isChecked():
            folder_path = QFileDialog.getExistingDirectory(self, "Klasör Seç")
        else:
            folder_path, _ = QFileDialog.getOpenFileName(self, "ZIP Dosyası Seç", "", "ZIP Dosyaları (*.zip)")

        if folder_path:
            self.folder_label.setText(f"Seçili Yol: {folder_path}")
            self.selected_path = folder_path
        else:
            self.selected_path = None

    def encrypt_folder(self):
        if hasattr(self, 'selected_path') and self.selected_path and self.folder_radio.isChecked():
            password = self.password_input.text()
            if not password:
                QMessageBox.warning(self, "Uyarı", "Lütfen bir şifre girin!")
                return

            success = FileCrypto.encrypt_folder(self.selected_path, password)

            if success:
                QMessageBox.information(self, "Başarılı", "Klasör başarıyla şifrelendi!")
                self.password_input.clear()
            else:
                QMessageBox.warning(self, "Uyarı", "Klasör şifreleme işlemi başarısız.")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen önce bir klasör seçin!")

    def decrypt_folder(self):
        if hasattr(self, 'selected_path') and self.selected_path and self.zip_radio.isChecked():
            password = self.password_input.text()
            if not password:
                QMessageBox.warning(self, "Uyarı", "Lütfen bir şifre girin!")
                return

            try:
                success = FileCrypto.decrypt_folder(self.selected_path, password)
                if success:
                    QMessageBox.information(self, "Başarılı", "Şifre çözme işlemi tamamlandı!")
                    self.password_input.clear()
                else:
                    QMessageBox.warning(self, "Hata", "Şifre çözme işlemi başarısız oldu!")
            except Exception as e:
                QMessageBox.critical(self, "Hata", f"Şifre çözme sırasında bir hata oluştu: {e}")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen önce bir ZIP dosyası seçin!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("assets/Comprimidos_25590.ico"))
    window = MainUI()
    window.show()
    sys.exit(app.exec())