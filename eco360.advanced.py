import streamlit as st
from streamlit_drawable_canvas import st_canvas

# --- Data for furniture ---
furniture_options = {
    "Sofa": "https://cdn.pixabay.com/photo/2017/11/06/08/42/sofa-2920149_1280.jpg",
    "Chair": "https://cdn.pixabay.com/photo/2014/04/03/11/44/chair-310156_1280.png",
    "Table": "https://cdn.pixabay.com/photo/2016/11/29/04/18/table-1869715_1280.jpg",
}

base_prices = {
    "Sofa": 500,
    "Chair": 150,
    "Table": 300,
}

# --- Title ---
st.title("🛋️ Eco360 Furniture Customizer")

# --- Furniture selection ---
selected_furniture = st.selectbox("Choose furniture:", list(furniture_options.keys()))
st.image(furniture_options[selected_furniture], width=300)

# --- Color picker ---
color = st.color_picker("Pick a color for your furniture", "#00f900")
st.write(f"Selected color: {color}")

# --- Quantity input ---
quantity = st.number_input("Quantity", min_value=1, max_value=10, value=1)

# --- Live Cost Estimator ---
# Simple color premium logic: if dark colors cost more, else base price
def is_dark_color(hex_color):
    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    luminance = (0.299*r + 0.587*g + 0.114*b) / 255
    return luminance < 0.5

color_cost = 50 if is_dark_color(color) else 0
base_price = base_prices[selected_furniture]
total_cost = (base_price + color_cost) * quantity

st.markdown(f"### Estimated Cost Breakdown:")
st.write(f"- Base price per unit: ${base_price}")
st.write(f"- Color premium (dark colors): ${color_cost}")
st.write(f"- Quantity: {quantity}")
st.write(f"**Total Estimated Cost: ${total_cost}**")

# --- Layout Visualization (drawable canvas) ---
st.markdown("### Draw your layout:")
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # translucent orange
    stroke_width=2,
    stroke_color="#000000",
    background_color="#eee",
    height=300,
    width=500,
    drawing_mode="rect",
    key="canvas",
)

if canvas_result.image_data is not None:
    st.image(canvas_result.image_data, caption="Your layout sketch")

# --- 3D Model Embed (Sketchfab iframe) ---
st.markdown("### 3D Furniture Preview:")
sketchfab_model_url = "https://sketchfab.com/models/7w7e7w2c0cb14cb981faeaaf6db27b72/embed"
st.markdown(f"""
<iframe
    title="3D model"
    frameborder="0"
    allowfullscreen
    mozallowfullscreen="true"
    webkitallowfullscreen="true"
    allow="autoplay; fullscreen; xr-spatial-tracking"
    xr-spatial-tracking
    execution-while-out-of-viewport
    execution-while-not-rendered
    web-share
    src="{sketchfab_model_url}"
    width="600"
    height="400"
></iframe>
""", unsafe_allow_html=True)

# --- Feedback & Ratings ---
st.markdown("### Feedback & Rating")
rating = st.slider("Rate this design (1 = worst, 5 = best)", 1, 5, 3)
feedback = st.text_area("Leave your feedback")

if st.button("Submit Feedback"):
    st.success(f"Thanks for your rating of {rating} and your feedback!")
    # Here you can save feedback to a DB or file

# --- Animation / Walkthrough Video ---
st.markdown("### Walkthrough Video")
st.video("https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4")

