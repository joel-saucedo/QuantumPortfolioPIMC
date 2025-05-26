# Configuration settings for the QuantumPortfolioPIMC project

# General settings
SIMULATION_CONFIG = {
    'num_particles': 100,
    'time_steps': 1000,
    'temperature': 1.0,
    'potential_energy': 'harmonic',
}

# Portfolio optimization settings
OPTIMIZATION_CONFIG = {
    'risk_aversion': 0.5,
    'max_iterations': 1000,
    'tolerance': 1e-6,
}

# File paths
DATA_INPUT_PATH = 'data/input/'
DATA_OUTPUT_PATH = 'data/output/'
VISUALIZATION_PLOTS_PATH = 'visualizations/plots/'
VISUALIZATION_REPORTS_PATH = 'visualizations/reports/'

# Logging settings
LOGGING_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(levelname)s - %(message)s',
    'filename': 'logs/project.log',
}