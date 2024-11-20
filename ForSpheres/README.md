# LEAT_LIGGGHTS Particle Position Data Conversion - for Spheres

This project converts particle position data from a CSV file to a LIGGGHTS-compatible `.data` file. The input CSV file should be created in ParaView, with an index starting at 0, and saved in the `convertingZone` directory. The user needs only to adjust the file path and sphere properties in the configuration.

## Project Structure

- **`main.py`**: Main script to run the data conversion. Defines input CSV path, sphere radius, and density.
- **`importCSV.py`**: Reads the CSV file using `pandas` and prepares it for conversion.
- **`createLIGGGHTS_data.py`**: Converts the CSV data to a `.data` file for LIGGGHTS, adding radius and density to each entry.

## Prerequisites

- **Python** 3.x
- **pandas** 2.2.3

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd LEAT_LIGGGHTS
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:
   - **Windows**:
     ```bash
     .venv\Scripts\activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Place your CSV file** (e.g., `particle_positions.csv`) in the `convertingZone` directory.
      ```csv
   Points_0,Points_1,Points_2
   -0.00271702,-0.0130748,0.000936094
   -0.00148737,-0.0132663,0.000499771
   -6.53189e-05,-0.0133391,0.000499771
   ...
   ```

   The file must include headers: position_0, position_1, position_2, which correspond to the x, y, and z coordinates of each sphere.
   Each row represents a sphere's position in space.

2. **Configure your settings**:
   - Open `main.py` and set the following variables:
     ```python
     csv_path = "convertingZone/particle_positions.csv"  # Path to your CSV file
     sphere_radius = 0.0002  # Sphere radius in meters
     sphere_density = 2700   # Sphere density in kg/m^3
     ```

3. **Run the script**:
   ```bash
   python main.py
   ```

4. The converted file `particle_positions.data` will be saved in the `convertingZone` directory.

## LIGGGHTS `.data` File Format

The `.data` file follows the LIGGGHTS format and includes:
- **Header Section**: Total number of atoms, atom types, and dimension bounds.
- **Body Section**: 
  - `Masses`: Specifies mass for atom type 1.
  - `Atoms`: Contains atom ID, atom type, x, y, z coordinates, radius, and density.





