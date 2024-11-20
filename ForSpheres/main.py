#main.py

from importCSV import csvReader
from createLIGGGHTS_data import create_Liggghts_file


csv_path = "ForSpheres\convertingZone\particle_positions.csv"
sphere_radius = 0.0002 # meter
sphere_density = 2700 # kg/m^3


if __name__ == "__main__":
    atoms_section_sphere, tot_number_rows = csvReader(csv_path)    
    create_Liggghts_file(atoms_section_sphere, tot_number_rows, sphere_radius, sphere_density)
