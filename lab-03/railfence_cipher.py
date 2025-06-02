import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.railfence import Ui_MainWindow
import requests


class RailFenceApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.call_api_railfence_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_railfence_decrypt)

    def call_api_railfence_encrypt(self):
        URL = "http://127.0.0.1:5000/api/railfence/encrypt"
        plain_text = self.ui.txt_plain_text.toPlainText()
        key_str = self.ui.txt_key.text()
        try:
            key = int(key_str)
        except ValueError:
            QMessageBox.warning(self, "Invalid Key", "Key must be an integer for Rail Fence Cipher.")
            return

        payload = {
            "plain_text": plain_text,
            "key": key
        }

        try:
            response = requests.post(URL, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setPlainText(data.get("encrypted_text", "Error: No encrypted_text found"))

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Rail Fence Encrypted Successfully")
                msg.exec_()
            else:
                error_message = f"Error from API: {response.status_code} - {response.text}"
                QMessageBox.warning(self, "API Error", error_message)
                print(error_message)
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Network Error", f"Could not connect to API: {e}")
            print(f"Network Error: {e}")

    def call_api_railfence_decrypt(self):
        URL = "http://127.0.0.1:5000/api/railfence/decrypt"
        cipher_text = self.ui.txt_cipher_text.toPlainText()
        key_str = self.ui.txt_key.text()
        try:
            key = int(key_str)
        except ValueError:
            QMessageBox.warning(self, "Invalid Key", "Key must be an integer for Rail Fence Cipher.")
            return

        payload = {
            "cipher_text": cipher_text,
            "key": key
        }

        try:
            response = requests.post(URL, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setPlainText(data.get("decrypted_text", "Error: No decrypted_text found"))

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Rail Fence Decrypted Successfully")
                msg.exec_()
            else:
                error_message = f"Error from API: {response.status_code} - {response.text}"
                QMessageBox.warning(self, "API Error", error_message)
                print(error_message)
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Network Error", f"Could not connect to API: {e}")
            print(f"Network Error: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RailFenceApp()
    window.show()
    sys.exit(app.exec_())