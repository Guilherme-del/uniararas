#include "car.h"
#include <iostream>

int main() {
    Car car1;
    Car car2;

    car1.refuel(20);
    car2.refuel(30);

    car1.move(200);
    car2.move(400);

    std::cout << "Car 1:" << std::endl;
    std::cout << "Distance traveled: " << car1.get_distance_traveled() << " km" << std::endl;
    std::cout << "Remaining fuel: " << car1.get_fuel() << " liters" << std::endl;

    std::cout << "\nCar 2:" << std::endl;
    std::cout << "Distance traveled: " << car2.get_distance_traveled() << " km" << std::endl;
    std::cout << "Remaining fuel: " << car2.get_fuel() << " liters" << std::endl;

    return 0;
}