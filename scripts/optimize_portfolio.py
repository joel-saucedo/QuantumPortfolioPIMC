import sys
import os
import json
from src.quantum.pimc import run_simulation
from src.optimization.algorithms import optimize_portfolio
from src.utils.helpers import load_data, save_results

def main():
    # Load simulation results
    simulation_results = load_data(os.path.join('data', 'output', 'simulation_results.json'))

    # Optimize portfolio based on simulation results
    optimized_portfolio = optimize_portfolio(simulation_results)

    # Save optimized portfolio results
    output_file = os.path.join('data', 'output', 'optimized_portfolio.json')
    save_results(optimized_portfolio, output_file)

    print(f"Optimized portfolio saved to {output_file}")

if __name__ == "__main__":
    main()