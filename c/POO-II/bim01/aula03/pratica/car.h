#ifndef CAR_H
#define CAR_H

class Car {
private:
    double tank_capacity = 50;
    double fuel = 0;
    double consumption = 15;
    double distance_traveled = 0;

public:
    void refuel(double amount);
    void move(double distance);
    double get_fuel();
    double get_distance_traveled();
};

#endif