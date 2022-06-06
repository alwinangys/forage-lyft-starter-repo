from car import Car
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from spindler_battery import SpindlerBattery
from nubbin_battery import NubbinBattery

class CarFactory(Car):
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_milegage = current_mileage
        self.last_service_mileage = last_service_mileage
        return Car(CapuletEngine, SpindlerBattery)

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_milegage = current_mileage
        self.last_service_mileage = last_service_mileage
        return Car(WilloughbyEngine, SpindlerBattery)

    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.warning_light_on = warning_light_on
        return Car(SternmanEngine, SpindlerBattery)

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_milegage = current_mileage
        self.last_service_mileage = last_service_mileage
        return Car(WilloughbyEngine, NubbinBattery)

    def create_thovax(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_milegage = current_mileage
        self.last_service_mileage = last_service_mileage
        return Car(CapuletEngine, NubbinBattery)