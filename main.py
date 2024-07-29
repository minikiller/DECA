# obj_file_path='/home/user/project/sunlf/expre/TestSamples/examples/results/alfw1/alfw1.obj'
obj_file_path='./output_wang.obj'
# obj_file_path='/home/user/project/sunlf/expre/output_file2.obj'

import streamlit as st
import pyvista as pv
import stpyvista as stpv

# Initialize the Streamlit app
st.title("Interactive 3D OBJ Viewer with PyVista and stpyvista")

# Provide a path to the local OBJ file
# obj_file_path = "obj/four.obj"

# Load the mesh using PyVista
mesh = pv.read(obj_file_path)

# Set up the plotter with off-screen rendering
plotter = pv.Plotter(off_screen=True)
# plotter.add_mesh(mesh, color='white')  # show_edges=True adds the gridlines
plotter.add_mesh(mesh, color='white', show_edges=True)  # show_edges=True adds the gridlines
plotter.view_isometric()
plotter.show_axes()
plotter.show_grid()  # Display the grid

# Render the PyVista plotter using stpyvista
stpv.stpyvista(plotter)

# Display mesh information
st.write("### Mesh Information")
st.write(f"Number of points: {mesh.n_points}")
st.write(f"Number of faces: {mesh.n_faces}")
