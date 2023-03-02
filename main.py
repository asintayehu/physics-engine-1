import numpy as np
from math import sqrt

global EARTH_MASS


class Ball:
    G_CONSTANT = (6.67 * (10**-11))
    M_EARTH = (5.97219 * (10 ** 2))
    EARTH_POSITION = (0, 0, 0)

    def __init__(self, position, velocity, acceleration, radius, mass):
        """
        :param position: vector representing position
        :param velocity: vector representing velocity
        :param acceleration: vector representing acceleration
        :param radius: number representing radius of ball
        :param mass: number representing mass of ball
        """
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        self.acceleration = np.array(acceleration)
        self.radius = radius
        self.mass = mass

    def update_position(self, dt):
        """
        :param dt: delta time, a change in time since the last update
        """
        self.position += self.velocity * dt

    # accessor and mutator functions for attributes
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

    """
    apply_force(force): Applies a force vector to the ball, which changes its acceleration.
    apply_impulse(impulse): Applies an impulse vector to the ball, which changes its velocity.
    calculate_gravity(gravity): Calculates the effect of gravity on the ball, based on its mass and the acceleration due to gravity.
    calculate_collision(other_object): Determines whether the ball has collided with another object in the scene, and updates its velocity and position accordingly.
    """

    # f_grav = G * (M_earth * m_ball) / r^2
    def calculate_gravity(self):
        # r = sqrt((self.position[0] - self.EARTH_POSITION)**2 + (self.position[1] - self.EARTH_POSITION)^2 + (self.position[2] - self.EARTH_POSITION)^2)
        r = sqrt((self.position[0])**2 + (self.position[1])**2 + (self.position[2])**2)
        f_grav = self.G_CONSTANT * (self.M_EARTH * self.mass) / r**2
        return f_grav

    def apply_force(self, force):
        pass

    def apply_impulse(self, impulse):
        pass

    def calculate_collision(self):
        pass





