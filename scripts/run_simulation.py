import os
import sys
import json
from src.quantum.pimc import PIMC
from src.optimization.algorithms import optimize_portfolio
from config.settings import CONFIG

def main():
    # Load configuration settings
    with open(CONFIG['simulation_config'], 'r') as config_file:
        simulation_params = json.load(config_file)

    # Initialize PIMC simulation
    pimc_simulation = PIMC(**simulation_params)

    # Run the simulation
    results = pimc_simulation.run()

    # Save results to output directory
    output_file = os.path.join('data', 'output', 'simulation_results.json')
    with open(output_file, 'w') as outfile:
        json.dump(results, outfile)

    # Optimize portfolio based on simulation results
    optimized_results = optimize_portfolio(results)

    # Save optimized results
    optimized_output_file = os.path.join('data', 'output', 'optimized_results.json')
    with open(optimized_output_file, 'w') as outfile:
        json.dump(optimized_results, outfile)

if __name__ == "__main__":
    main()