import matplotlib.pyplot as plt
import numpy as np
import os

def visualize_results(simulation_data, output_dir):
    """
    Generate visualizations from simulation data and save them to the specified output directory.

    Parameters:
    simulation_data (dict): A dictionary containing simulation results.
    output_dir (str): The directory where visualizations will be saved.
    """

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Example visualization: Plotting the simulation results
    plt.figure(figsize=(10, 6))
    plt.plot(simulation_data['time'], simulation_data['values'], label='Simulation Results')
    plt.title('Simulation Results Over Time')
    plt.xlabel('Time')
    plt.ylabel('Values')
    plt.legend()
    plt.grid()

    # Save the plot
    plot_path = os.path.join(output_dir, 'simulation_results.png')
    plt.savefig(plot_path)
    plt.close()

    print(f"Visualization saved to {plot_path}")

# Example usage (this part can be removed or commented out in the final script)
if __name__ == "__main__":
    # Mock simulation data for demonstration purposes
    simulation_data = {
        'time': np.linspace(0, 10, 100),
        'values': np.sin(np.linspace(0, 10, 100))
    }
    output_dir = '../visualizations/plots'
    visualize_results(simulation_data, output_dir)