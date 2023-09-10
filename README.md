# Space Rocket Simulation

This project implements a basic space rocket takeoff simulation using Python. It covers physics like thrust, drag, gravity, and air resistance, while also demonstrating parallel processing and OpenGL visualization. The simulation calculates the rocket's altitude over time, taking into account environmental factors and rocket properties.

## Physics and Mechanics

The simulation incorporates the following physics and mechanics:

- **Thrust:** The rocket generates thrust based on its engine efficiency and power.
- **Drag:** Air resistance is calculated based on the rocket's velocity, shape, and air density.
- **Gravity:** The gravitational force pulls the rocket downward.
- **Fuel Consumption:** The rocket's mass decreases as fuel is consumed.
- **Altitude and Velocity:** The rocket's altitude and velocity are updated over time based on the net forces acting on it.

## How to Run

1. Clone or download the repository.
2. Navigate to the project directory:
   ```sh
   cd SpaceRocketSim
   ```
3. Install required packages:
   ```sh
   pip install pygame
   pip install pyopengl
   ```
4. Edit the `config.json` file to set rocket properties and simulation parameters.
5. Run the main script to execute the simulation and visualization:
   ```sh
   python main.py
   ```

## Functionality

The project consists of the following components:

- **simulator.py:** Contains classes for the rocket simulation engine and rocket properties.
- **parallel.py:** Implements parallel processing for simulating multiple rockets simultaneously.
- **visualization.py:** Utilizes OpenGL to visualize the rocket's takeoff in a 3D environment.
- **config.json:** Configuration file for setting rocket properties and simulation parameters.
- **main.py:** Orchestrates the overall execution of the simulation and visualization.

By running the `main.py` script, you will trigger the following:

1. Simulate multiple rockets in parallel using the `parallel.py` module.
2. Visualize rocket takeoff using OpenGL and the `visualization.py` module.
3. Observe how rocket behaves based on physics and environmental factors.

