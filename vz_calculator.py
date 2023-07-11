import numpy as np
class VerticalVelocitiesCalculator:
    def __init__(self, mu_b, d, v_z_sun, v_c, R_sun, v_c_sun, U_sun, cos_b):
        self.mu_b = mu_b
        self.d = d
        self.b = b
        self.l=l
        self.v_z_sun = v_z_sun
        #self.v_c = v_c
        self.R_sun = R_sun
        self.R  = R
        self.v_c_sun = v_c_sun
        self.U_sun = U_sun
        self.V_sun = V_sun

    def calculate_vertical_velocity(self):
        S = (vc * (self.R_sun / self.R)- self.v_c_sun) * np.sin(np.radians(self.l))
        S_sun =(self.U_sun * np.cos(np.radians(self.l))) + (self.v_z_sun * np.sin(np.radians(self.l)))
        v_z_prime = ((4.74 * self.mu_b * self.d) / np.cos(np.radians(self.b))) + self.v_z_sun + (S - S_sun) * np.tan(np.radians(self.b)
        return v_z_prime
      
        
