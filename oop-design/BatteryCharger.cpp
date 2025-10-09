struct Device {
    std::string name;
    double consumption;
    int portNeeded;
}

class BatteryCharger {
    private:
        double power_capacity;
        int port_count;
    public:
        BatteryCharger();
        BatteryCharger(double power_capacity, int port_count);
        void charge(const Device &dev, int hours);
}

BatteryCharger::BatteryCharger() {
    power_capacity = 200.0;
    port_count = 4;
}

BatteryCharger::BatteryCharger(double power_capacity, int port_count) : power_capacity(power_capacity), port_count(port_count) {}

void BatteryCharger::charge(const Device &dev, int hours) {
    if (dev.consumption * hours <= power_capacity && dev.portNeeded <= port_count) {
        power_capacity -= dev.consumption * hours;
        port_count -= dev.portNeeded;

        std::cout << "Successfully charged" << std::endl;
    }
    else {
        std::cout << "Failed to charge" << std::endl;
    }
}