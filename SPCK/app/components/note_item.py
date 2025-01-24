from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QSizePolicy,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QApplication,
)
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPalette, QColor, QPixmap, QFont
from PyQt6.QtCore import Qt
import sys


class NoteItem(QWidget):
    def __init__(self, root_ui_path, note, currentEmail):
        super().__init__()
        self.root_ui_path = root_ui_path
        # Set the size policy
        size_policy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        self.setSizePolicy(size_policy)

        # Set minimum and maximum size
        self.setMinimumSize(QSize(300, 100))
        self.setMaximumSize(QSize(300, 150))

        # Set the stylesheet
        self.setStyleSheet(
            """
            QWidget {
                background-color: #FDF5E6;
                color: rgb(81, 81, 81);
            }
        """
        )

        # Set the layout (QVBoxLayout)
        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setStretch(0, 1)
        layout.setStretch(1, 0)
        layout.setStretch(2, 1)
        layout.setStretch(3, 0)

        # Set the layout to the widget
        self.setLayout(layout)

        # Create the titleHLayout_2 (QHBoxLayout)
        title_h_layout_2 = QHBoxLayout()
        title_h_layout_2.setStretch(0, 4)
        title_h_layout_2.setStretch(1, 1)

        # Create the first QLabel (title_label_2)
        title_label_2 = QLabel(note["title"])
        title_font = QFont()
        title_font.setPointSize(10)
        title_font.setWeight(QFont.Weight.Bold)  # Set font weight to bold
        title_label_2.setFont(title_font)
        title_label_2.setStyleSheet("padding-left: 10px; font-weight: bold;")

        # Add the first label to the layout
        title_h_layout_2.addWidget(title_label_2)

        # Create the second QLabel (iconNote1_2)
        icon_note1_2 = QLabel()
        icon_note1_2.setStyleSheet("background-color: #FDF5E6;")
        icon_note1_2.setMaximumSize(QSize(30, 30))
        icon_note1_2.setScaledContents(False)

        # Set the pixmap (image) for iconNote1_2
        pixmap = QPixmap("MyTien/app/assets/icons/note.png")
        scaled_pixmap = pixmap.scaled(
            30,
            30,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        icon_note1_2.setPixmap(scaled_pixmap)

        # Add the second label to the layout
        title_h_layout_2.addWidget(icon_note1_2)

        # Add titleHLayout_2 to the main layout
        self.layout().addLayout(title_h_layout_2)

        # Create label_3 (QLabel)
        label_3 = QLabel(note["note"])

        # Disable acceptDrops
        label_3.setAcceptDrops(False)

        # Set stylesheet for padding
        label_3.setStyleSheet("padding: 0 10px;")

        # Enable word wrapping
        label_3.setWordWrap(True)

        # Add label_3 to the main layout
        self.layout().addWidget(label_3)

        # Create horizontalLayout_4 (QHBoxLayout)
        horizontal_layout_4 = QHBoxLayout()
        horizontal_layout_4.setStretch(0, 4)
        horizontal_layout_4.setStretch(1, 1)

        # Set size constraint to fixed size
        horizontal_layout_4.setSizeConstraint(QHBoxLayout.SizeConstraint.SetFixedSize)

        # Create label_4 (QLabel)
        label_4 = QLabel()
        label_4.setText("")  # Empty text as per the XML

        # Add label_4 to the layout
        horizontal_layout_4.addWidget(label_4)

        # Create B_Edit1_2 (QPushButton)
        edit_button = QPushButton("Edit")
        edit_button.setMaximumSize(50, 25)
        # Set the cursor to PointingHandCursor when hovering over the button
        edit_button.setCursor(Qt.CursorShape.PointingHandCursor)
        # Set the style sheet for the button
        edit_button.setStyleSheet(
            """
            border: 10px;
            background-color: #f2f0f0;
            color: rgb(120, 128, 140);
        """
        )
        # bat su kien cho nut edit
        edit_button.clicked.connect(lambda: self.edit_button_clicked(note))

        # Add the edit button to the layout
        horizontal_layout_4.addWidget(edit_button)

        # Add the horizontal layout to the main layout
        self.layout().addLayout(horizontal_layout_4)
        self.currentEmail = currentEmail

    def edit_button_clicked(self, note):
        from views.edit import Edit

        try:
            if not hasattr(self, "edit_window"):
                self.edit_window = Edit(self.root_ui_path, "Edit note", note, self.currentEmail)
            self.edit_window.show()
        except Exception as e:
            print(e)
