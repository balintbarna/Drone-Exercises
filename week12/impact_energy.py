from data_reader.data_reader import data_loader

def get_impact_velocity(velocity: data_loader):
    impact_velocity = -1
    down_vel = velocity.velocity_down
    for i in range(len(down_vel)):
        current_vel = down_vel[i]
        if(current_vel > 2):
            impact_velocity = current_vel
    return impact_velocity

def calculate_impact_energy(velocity: data_loader, mass = 1.95):
    v = get_impact_velocity(velocity)
    m = mass
    E = 0.5*m*v*v
    energy = E
    return energy
