import numpy as np
class VerticalVelocitiesCalculator:
    def __init__(self, mu_b,l,b,d,R,v_c):
        self.mu_b = mu_b
        self.d = d
        self.b = b
        self.l=l
        self.v_z_sun = 7.25
        self.R  = R
        self.v_c = v_circ(self.R)
        self.R_sun = 8.15
        self.v_c_sun = 229
        self.U_sun = 11.1
        self.V_sun = 12.24

    def calculate_vertical_velocity(self):
        if -20<=self.b<=20:
            S = (self.v_c * (self.R_sun / self.R)- self.v_c_sun) * np.sin(np.radians(self.l))
            S_sun =(self.U_sun * np.cos(np.radians(self.l))) + (self.v_z_sun * np.sin(np.radians(self.l)))
            v_z_prime = ((4.74 * self.mu_b * self.d) / np.cos(np.radians(self.b))) + self.v_z_sun + (S - S_sun) * np.tan(np.radians(self.b)
            return v_z_prime
        else:
             print("Source is not close to the midplane, Sorry!")                                                                                                            
                                                                                                                         
    def vcirc(self,R):
        vc=229-(1.7*(self.R-self.R_sun))                                                                                                          
        return vc
                                                                                                                     
