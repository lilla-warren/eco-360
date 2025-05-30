import streamlit as st

# Title
st.title("Eco 360 Prototype")

# Furniture options and colors
furniture_options = {
    "Modular Sofa": ["#A0522D", "#696969", "#1E90FF"],
    "Recycled Coffee Table": ["#8B4513", "#2F4F4F"],
    "Bookshelf": ["#556B2F", "#708090"],
}

# Sidebar for furniture selection
st.sidebar.header("Customize Furniture")

selected_furniture = st.sidebar.selectbox("Choose furniture", list(furniture_options.keys()))
colors = furniture_options[selected_furniture]

# Select color
selected_color = st.sidebar.radio("Select color", colors)

# Layout slider
layout = st.sidebar.slider("Adjust Layout (1 to 5)", 1, 5, 1)

# Budget input
budget = st.sidebar.number_input("Budget (AED)", min_value=0, value=5000, step=100)

# Duration input
duration = st.sidebar.number_input("Duration (Months)", min_value=1, value=12, step=1)

# AR experience toggle
ar_enabled = st.sidebar.checkbox("Enable AR Experience")

# Main page display
st.header(f"Preview your {selected_furniture}")

# Show a colored box simulating furniture color
st.markdown(f"""
<div style="width:100%; height:200px; background-color:{selected_color}; 
             display:flex; align-items:center; justify-content:center; 
             color:white; font-size:24px; border-radius:10px;">
  {selected_furniture} - Layout {layout}
</div>
""", unsafe_allow_html=True)

# Show budget and duration info
st.write(f"**Budget:** AED {budget}")
st.write(f"**Duration:** {duration} months")
st.write(f"**AR Experience Enabled:** {'Yes' if ar_enabled else 'No'}")

# Placeholder for 3D model viewer
st.subheader("3D Model Viewer (Coming Soon)")
st.info("This is a placeholder for a 3D model viewer.")

# Walkthrough simulation button
if st.button("Play Walkthrough"):
    st.success("Walkthrough simulation feature coming soon!")

