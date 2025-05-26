import os
import json
from datetime import datetime

def generate_report(simulation_results, optimization_results, output_dir):
    report_data = {
        "simulation_results": simulation_results,
        "optimization_results": optimization_results,
        "generated_at": datetime.now().isoformat()
    }

    report_filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    report_path = os.path.join(output_dir, report_filename)

    with open(report_path, 'w') as report_file:
        json.dump(report_data, report_file, indent=4)

    print(f"Report generated: {report_path}")

if __name__ == "__main__":
    # Example usage
    simulation_results = {"example_metric": 42}  # Replace with actual simulation results
    optimization_results = {"optimized_value": 100}  # Replace with actual optimization results
    output_dir = "visualizations/reports"

    os.makedirs(output_dir, exist_ok=True)
    generate_report(simulation_results, optimization_results, output_dir)