import streamlit as st
import aspose.cad as cad
from aspose.cad import Color
from aspose.cad import Image as CadImage
from aspose.cad.imageoptions import DwgOptions, CadRasterizationOptions
import os

def convert_to_dwg(img_file, dwg_output_file):
    # Load the SVG file using Aspose.CAD
    image = CadImage.load(img_file)

    cadRasterizationOptions = CadRasterizationOptions()
    cadRasterizationOptions.page_height = image.height + .0
    cadRasterizationOptions.page_width = image.width + .0
    cadRasterizationOptions.zoom = 1.0
    cadRasterizationOptions.background_color = Color.white
    cadRasterizationOptions.no_scaling = True
    # cadRasterizationOptions.automatic_layouts_scaling = False


    dwg_options = DwgOptions()
    dwg_options.vector_rasterization_options = cadRasterizationOptions
    image.save(dwg_output_file, dwg_options)

st.title("Image to DWG Converter")
uploaded_file = st.file_uploader("Choose an PNG file", type=["png"])

if uploaded_file is not None:
    
    
    # Define the output DWG file path
    dwg_output_file = "output.dwg"
    
    # Convert the SVG to DWG format
    convert_to_dwg(uploaded_file, dwg_output_file)
    
    # Check if the DWG file was successfully created and has content
    if os.path.exists(dwg_output_file) and os.path.getsize(dwg_output_file) > 0:
        st.success("Conversion successful!")
        with open(dwg_output_file, "rb") as file:
            st.download_button("Download DWG file", data=file, file_name=dwg_output_file)
    else:
        st.error("Conversion failed or resulted in an empty DWG file.")
    
