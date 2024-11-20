#createLIGGGHTS_data.py

import os

def create_Liggghts_file(atom_section_df, tot_number_of_particles, radius, density):
    file_save_path = "ForSpheres\convertingZone\spheres_positions.data"
    atom_types = 1

    if os.path.exists(file_save_path):
        print("File already exists and will be overwritten")

    # Create a file
    with open(file_save_path, 'w') as fp:
        # Write the header section
        fp.write("# LIGGGHTS data file generated from Paraview-CSV\n\n")
        fp.write("\t\t\t\t\t#### HEADER\n")
        fp.write(f"{tot_number_of_particles} atoms \t\t\t\t # Total number of atoms (number of rows in the CSV file)\n")
        fp.write(f"{atom_types} atom types \t\t\t\t # Assuming all spheres are of a single type\n")
        fp.write("-0.9 0.9 xlo xhi \t\t\t # x-dimension bounds\n")
        fp.write("-0.9 0.9 ylo yhi \t\t\t # y-dimension bounds\n")
        fp.write("-0.5 0.5 zlo zhi \t\t\t # z-dimension bounds\n\n")

        # Write the body section
        fp.write("\t\t\t\t\t#### BODY\n")

        fp.write("Atoms\n")
        # Convert each row of the DataFrame to the required format and write to the file
        for index, row in atom_section_df.iterrows():
            if index < tot_number_of_particles: #Ensure not to create an empty line of Atoms-Section
                fp.write(f"{index}\t{atom_types}\t{radius}\t{density}\t{row['position_0']}\t{row['position_1']}\t{row['position_2']}\n")
            else:
                fp.write(f"{index}\t{atom_types}\t{radius}\t{density}\t{row['position_0']}\t{row['position_1']}\t{row['position_2']}")


