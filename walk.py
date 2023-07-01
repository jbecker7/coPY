import os
import shutil
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap

class ImageExtractor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Extraction")
        self.setFixedWidth(600)
        self.setFixedHeight(400)
        self.source_label = QLabel("Source Directory:")
        self.source_entry = QLineEdit()
        self.source_browse_button = QPushButton("Browse")
        self.source_browse_button.clicked.connect(self.browse_source_directory)

        self.wechat_button = QPushButton("WeChat")
        self.wechat_button.clicked.connect(self.set_wechat_source_directory)

        self.imessage_button = QPushButton("iMessage")
        self.imessage_button.clicked.connect(self.set_imessage_source_directory)

        self.destination_label = QLabel("Destination Directory:")
        self.destination_entry = QLineEdit()
        self.destination_browse_button = QPushButton("Browse")
        self.destination_browse_button.clicked.connect(self.browse_destination_directory)

        self.extract_button = QPushButton("Copy Images")
        self.extract_button.clicked.connect(self.extract_images)

        layout = QVBoxLayout()
        layout.addWidget(self.source_label)
        layout.addWidget(self.source_entry)
        layout.addWidget(self.source_browse_button)
        layout.addWidget(self.wechat_button)
        layout.addWidget(self.imessage_button)
        layout.addWidget(self.destination_label)
        layout.addWidget(self.destination_entry)
        layout.addWidget(self.destination_browse_button)
        layout.addWidget(self.extract_button)

        self.setLayout(layout)

    def browse_source_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Source Directory")
        self.source_entry.setText(directory)

    def set_wechat_source_directory(self):
        wechat_path = os.path.expanduser("~/Library/Containers/com.tencent.xinWeChat/Data/Library/Application Support/com.tencent.xinWeChat/2.0b4.0.9/1facd9704bf68a608171e1cc00ecceff/Message/MessageTemp")
        self.source_entry.setText(wechat_path)

    def set_imessage_source_directory(self):
        imessage_path = os.path.expanduser("~/Library/Messages/Attachments")
        self.source_entry.setText(imessage_path)

    def browse_destination_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Destination Directory")
        self.destination_entry.setText(directory)

    def extract_images(self):
        source_directory = self.source_entry.text()
        destination_directory = self.destination_entry.text()

        # Create the destination folder if it doesn't exist
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)

        # Traverse through the source directory and its subdirectories
        for root, dirs, files in os.walk(source_directory):
            for file_name in files:
                # Check if the file is an image
                if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.heic', '.bmp')):
                    source_path = os.path.join(root, file_name)
                    destination_path = os.path.join(destination_directory, file_name)
                    shutil.copy2(source_path, destination_path)
                    print(f"Copied {file_name} to {destination_directory}")


if __name__ == '__main__':
    app = QApplication([])
    window = ImageExtractor()
    window.show()
    app.exec_()
