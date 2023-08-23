import json
from simulator import Rocket
from parallel import main as parallel_main
from visualization import visualize_rocket

def load_config(filename):
    with open(filename, "r") as file:
        return json.load(file)

def main():
    config = load_config("config.json")
    rocket = Rocket(config["rocket_mass"], config["rocket_thrust"], config["target_altitude"])

    # Pass rocket and config to parallel processing module
    parallel_main()

    # Pass rocket and config to OpenGL visualization module
    visualize_rocket(rocket, config)

if __name__ == "__main__":
    main()
