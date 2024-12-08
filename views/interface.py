from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
)

from PyQt5.QtCore import QObject, QThread, pyqtSignal
import asyncio


class FetchWeatherWorker(QObject):
    finished_getting_weather = pyqtSignal(dict)

    def __init__(self, controller, city):
        super().__init__()
        self.controller = controller
        self.city = city

    def run(self):
        """
        Runs the weather fetch operation in an async loop.
        """

        asyncio.run(self.fetch_weather_async())

    async def fetch_weather_async(self):
        """
        Asynchronously fetches the weather data.
        """
        result = await self.controller.get_weather(self.city)
        self.finished_getting_weather.emit(result)


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
        """
        Starts the worker thread to fetch weather data.
        """
        city = self.city_input.text()
        if not city:
            self.result_label.setText("Please enter a city name.")
            return

        self.result_label.setText("Fetching...")
        self.fetch_weather_thread = QThread()
        self.fetch_weather_worker = FetchWeatherWorker(self.controller, city)
        self.fetch_weather_worker.moveToThread(self.fetch_weather_thread)

        # Connect signals and slots
        self.fetch_weather_thread.started.connect(self.fetch_weather_worker.run)
        self.fetch_weather_worker.finished_getting_weather.connect(self.display_result)
        self.fetch_weather_worker.finished_getting_weather.connect(
            self.fetch_weather_thread.quit
        )
        self.fetch_weather_worker.finished_getting_weather.connect(
            self.fetch_weather_worker.deleteLater
        )
        self.fetch_weather_thread.finished.connect(
            self.fetch_weather_thread.deleteLater
        )

        # Start the thread
        self.fetch_weather_thread.start()

        # Disable button while fetching
        self.fetch_button.setEnabled(False)
        self.fetch_weather_thread.finished.connect(
            lambda: self.fetch_button.setEnabled(True)
        )

    def display_result(self, result):
        """
        Displays the result from the worker on the GUI.
        """

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
