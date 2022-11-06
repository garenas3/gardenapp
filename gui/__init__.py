from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QSizePolicy, QDoubleSpinBox,
                             QFormLayout)
from PyQt5.QtGui import QGuiApplication, QFont
from PyQt5.QtCore import Qt


class MainWindow(QWidget):
    """The application's main window.

    There should only ever be one instance of the main window.
    """

    QGuiApplication.setFont(QFont("Arial", 12))  # set default font

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedWidth(405)
        self.setWindowTitle("Garden App")
        layout = QVBoxLayout(self)
        layout.addWidget(DailyReminderToWaterPlants(), alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(TemperatureInput(), stretch=1, alignment=Qt.AlignmentFlag.AlignTop)
        self.show()


class DailyReminderToWaterPlants(QWidget):
    """A reminder to show to the user to water their plants.

    The reminder can be closed by clicking the dismiss button.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        layout = QHBoxLayout(self)

        textLabel = QLabel()
        textLabel.setText("💧 Remember to water your plants!")
        textLabel.setWordWrap(True)
        textLabel.sizePolicy().setHorizontalPolicy(QSizePolicy.Policy.Expanding)
        layout.addWidget(textLabel, stretch=1)

        dismissButton = QPushButton("Dismiss")
        dismissButton.clicked.connect(self.close)
        layout.addWidget(dismissButton, alignment=Qt.AlignmentFlag.AlignRight)

        # TODO: Make reminder daily.


class TemperatureInput(QWidget):
    """Input the current outside temperature and show warnings."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.okMessage = "🙂 Your plants are safe to be outside."
        self.coldMessage = "🥶 Bring your plants indoors!"

        mainLayout = QVBoxLayout(self)
        inputLayout = QHBoxLayout()

        textLabel = QLabel()
        textLabel.setText("Current Temperature")
        inputLayout.addWidget(textLabel, stretch=1)

        temperatureSpinBox = QDoubleSpinBox()
        temperatureSpinBox.setRange(-99.9, 999.9)
        temperatureSpinBox.setDecimals(1)
        temperatureSpinBox.setSuffix(" ℉")
        temperatureSpinBox.setValue(72.0)
        temperatureSpinBox.valueChanged.connect(self.checkForColdTemperature)
        inputLayout.addWidget(temperatureSpinBox)

        mainLayout.addLayout(inputLayout)
        self.statusLabel = QLabel()
        self.statusLabel.setText(self.okMessage)
        mainLayout.addWidget(self.statusLabel, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

    def checkForColdTemperature(self, currentTemperature):
        """Update the status label if the temperature is too cold."""
        critical = 45.0
        if currentTemperature <= critical:
            self.statusLabel.setText(self.coldMessage)
        else:
            self.statusLabel.setText(self.okMessage)
