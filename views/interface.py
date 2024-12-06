from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
)


class WeatherAppView(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Weather App")
        self.setGeometry(100, 100, 100, 100)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.city_input = QLineEdit(self)
        self.city_input.setPlaceholderText("Enter City Name")
        layout.addWidget(self.city_input)

        self.fetch_button = QPushButton("Get Weather", self)
        self.fetch_button.clicked.connect(self.fetch_weather)
        layout.addWidget(self.fetch_button)

        self.result_label = QLabel("", self)
        layout.addWidget(self.result_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def fetch_weather(self):
        city = self.city_input.text()
        if city:
            status_code, result = self.controller.get_weather(city)
            if "error" in result:
                self.result_label.setText(f"Error: {result['error']}")
            else:
                self.result_label.setText(
                    f"City: {result['city']}\n"
                    f"Temperature: {result['temperature']}°C\n"
                    f"Description: {result['description']}"
                )


if __name__ == "__main__":
    import sys
    from controllers.weather_controller import WeatherController

    app = QApplication(sys.argv)
    controller = WeatherController()
    view = WeatherAppView(controller)
    view.show()
    sys.exit(app.exec())
