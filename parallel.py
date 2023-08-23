import multiprocessing
from simulator import simulate_rocket
from simulator import Rocket
def parallel_main(config):
    
    num_processes = multiprocessing.cpu_count()
    rocket = Rocket(config["rocket_mass"], config["rocket_thrust"], config["target_altitude"],config["air_density"] )
    pool = multiprocessing.Pool(processes=num_processes)
    results = [pool.apply_async(simulate_rocket, args=(rocket, config)) for _ in range(num_processes)]
    pool.close()
    pool.join()

    altitudes = [result.get() for result in results]
    average_altitude = sum(altitudes) / len(altitudes)
    print("Average Final Altitude:", average_altitude)

