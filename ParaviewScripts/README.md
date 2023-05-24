# ElmerFEM_Colab
# Execute ElmerFEM's Flow Step example in Google Colab.
This core code is currently under development and aims to utilize the ElmerFEM and Google Colab platform for educational purposes. 
It enables running ElmerFEM online directly from the GitHub repository, eliminating the need for extra software installation.
Suitable for teaching Finite Element Method (FEM) in classes.

# Contributions are welcome:
- Code for plotting the color surfaces representing the velocity magnitude and pressure profiles.
  
Python script to batch generate velocity plot  
Assumes paraview is installed and in the path  
Assumes it is in the current directory with the vtu file created from Elmer  
 

Run script  
pvpython makevelocity.py  ! makes velovity plot  
pvpython plots.py ! make velocity, pressure, and wire mesh  
pvpython plotline.py 0.003 0.0 0.096  ! Plots x velocity at position 0.003 from 0.0 to 0.096 on y axis



