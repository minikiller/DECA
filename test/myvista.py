import streamlit as st
import pyvista as pv
from stpyvista import stpyvista

# Set up the Streamlit app
st.title("Streamlit with PyVista Example")

# Create a PyVista sphere
sphere = pv.Sphere()

# Create a PyVista plotter
plotter = pv.Plotter(off_screen=True)
plotter.add_mesh(sphere, color="lightblue")

# Render the plot and get the image as a base64 string
plotter.screenshot('sphere.png')

# Display the plot using stpyvista
stpyvista(plotter)
