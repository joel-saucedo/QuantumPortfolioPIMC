import sys
import os
import json
from src.optimization.algorithms import optimize_portfolio
from src.utils.helpers import save_results

def main():
    # Load simulation results
    simulation_results_path = os.path.join('data', 'output', 'simulation_results.json')
    with open(simulation_results_path, 'r') as f:
        simulation_results = json.load(f)

    # Optimize portfolio based on simulation results
    optimized_portfolio = optimize_portfolio(simulation_results)

    # Save optimized portfolio results
    output_file = os.path.join('data', 'output', 'optimized_portfolio.json')
    with open(output_file, 'w') as f:
        json.dump(optimized_portfolio, f, indent=2)

    print(f"Optimized portfolio saved to {output_file}")

if __name__ == "__main__":
    main()