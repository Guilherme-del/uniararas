#include "car.h"
#include <algorithm>

void Car::refuel(double amount) {
    if (amount > 0) {
        fuel = std::min(fuel + amount, tank_capacity);
    }
}

void Car::move(double distance) {
    if (fuel > 0) {
        double range = fuel * consumption;
        double achievable_distance = std::min(range, distance);
        fuel -= achievable_distance / consumption;
        distance_traveled += achievable_distance;
    }
}

double Car::get_fuel() {
    return fuel;
}

double Car::get_distance_traveled() {
    return distance_traveled;
}
