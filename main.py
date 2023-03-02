import numpy as np


class Ball:
    # position_x, position_y, position_z, velocity_x,
    # velocity_y, velocity_z, acceleration_x, acceleration_y,
    # acceleration_z, radius, mass
    def __init__(self, position, velocity, acceleration, radius, mass):
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        self.acceleration = np.array(acceleration)
        self.radius = radius
        self.mass = mass

    def set_position(self, position_x, position_y, position_z):
        self.position = np.array([position_x, position_y, position_z])

    def get_position(self):
        return self.position

    def set_velocity(self, velocity_x, velocity_y, velocity_z):
        self.velocity = np.array([velocity_x, velocity_y, velocity_z])

    def get_velocity(self):
        return self.velocity

    def set_acceleration(self, acceleration_x, acceleration_y, acceleration_z):
        self.acceleration = np.array([acceleration_x, acceleration_y, acceleration_z])

    def get_acceleration(self):
        return self.acceleration

    def set_radius(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_mass(self, mass):
        self.mass = mass

    def get_mass(self):
        return self.mass





