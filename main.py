import numpy as np
import matplotlib.pyplot as plt

def projectile(u, angle, height=0):
    
    theta = np.radians(angle)
    
    # Initial Velocity Components
    ux = u * np.cos(theta)
    uy = u * np.sin(theta)
    
    # Time of flight
    g = 9.8 
    t_flight = (2*uy) / g
    
    # Create time array
    t = np.linspace(0, t_flight, 100)
    
    # Calculate x and y positions
    x = ux * t
    y = height + uy*t - 0.5*g*t**2
    
    # Plot the trajectory
    plt.figure(figsize=(10, 6))
    plt.plot(x, y)
    plt.title("Projectile Motion")
    plt.xlabel("Horizontal Distance (m)")
    plt.ylabel("Vertical Distance (m)")
    plt.grid(True)
    plt.axis('equal')
    plt.show()

#input
u = float(input("Initial Velocity : ")) 
angle = float(input("Angle : ")) 
height = 0

projectile(u, angle, height)