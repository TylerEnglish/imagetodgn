import streamlit as st
from aspose.cad import Image
from aspose.cad.imageoptions import CadRasterizationOptions, DgnOptions

def convert_to_dgn(input_file, output_file):
    # Load the image file
    image = Image.load(input_file)

    # Set rasterization options
    rasterization_options = CadRasterizationOptions()
    rasterization_options.page_width = 1600
    rasterization_options.page_height = 1600

    # Set DGN options
    dgn_options = DgnOptions()
    dgn_options.vector_rasterization_options = rasterization_options

    # Save as DGN
    image.save(output_file, dgn_options)

st.title("Image to DGN Converter")

uploaded_file = st.file_uploader("Choose an image file", type=["svg", "png", "jpeg", "jpg"])

if uploaded_file is not None:
    input_file = uploaded_file.name
    output_file = "output.dgn"

    with open(input_file, "wb") as f:
        f.write(uploaded_file.getbuffer())

    convert_to_dgn(input_file, output_file)

    st.success("Conversion successful!")
    st.download_button("Download DGN file", data=open(output_file, "rb"), file_name=output_file)
