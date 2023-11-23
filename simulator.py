class Rocket:
    def __init__(self, mass, thrust, target_altitude,air_density):
        self.mass = mass
        self.thrust = thrust
        self.target_altitude = target_altitude
        self.air_density = air_density  # Add air_density as an attribute
        self.fuel_consumption_rate = 0.1

    def calculate_thrust(self):
        # Calculate thrust based on engine efficiency and other factors
        engine_efficiency = 0.9
        other_factors = 1.2
        thrust = self.thrust * engine_efficiency * other_factors

        return thrust
        return self.thrust

    def calculate_drag(self, velocity):
        drag_coefficient, cross_sectional_area=0.3,0.05
        # Calculate drag based on velocity, rocket shape, and air density
        return 0.005 * self.air_density * velocity**2 * drag_coefficient * cross_sectional_area

    def update_mass(self, time_step):
        # Update mass due to fuel consumption
        self.mass -= self.fuel_consumption_rate * time_step

class RocketSimulator:
    def __init__(self, rocket, config):
        self.rocket = rocket
        self.time_step = config["time_step"]
        self.gravity = config["gravity"]
        self.air_density = config["air_density"]
        self.config=config

    def simulate(self):
        altitude = 0
        velocity = 0
        time = self.config["simulation_time"]

        while altitude < self.rocket.target_altitude and time > 0:
            thrust = self.rocket.calculate_thrust()
            drag = self.rocket.calculate_drag(velocity)
            gravity_force = self.gravity * self.rocket.mass
            net_force = thrust - drag - gravity_force

            acceleration = net_force / self.rocket.mass
            velocity += acceleration * self.time_step
            altitude += velocity * self.time_step

            self.rocket.update_mass(self.time_step)  # Update rocket mass after fuel consumption

            time -= self.time_step

        return altitude

def simulate_rocket(rocket, config):
    simulator = RocketSimulator(rocket, config)
    return simulator.simulate()
