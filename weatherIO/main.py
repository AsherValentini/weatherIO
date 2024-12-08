from PyQt5.QtWidgets import QApplication
from views.interface import WeatherAppView
from controllers.weather_controller import WeatherController
import sys


def main():
    app = QApplication(sys.argv)
    controller = WeatherController()
    view = WeatherAppView(controller)
    view.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
