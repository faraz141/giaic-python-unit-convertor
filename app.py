import streamlit as st

# Page setup
st.set_page_config(page_title="Google Unit Converter", layout="centered")

# Custom CSS for styling (optional)
st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .stTextInput, .stNumberInput, .stSelectbox, .stButton button {
            border-radius: 10px !important;
        }
        .stButton button {
            background-color: #1a73e8;
            color: white;
            padding: 0.6rem 1.5rem;
            border: none;
        }
        .stButton button:hover {
            background-color: #1669c1;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🔁 Google Unit Converter")
st.caption("Made with ❤️ in Streamlit – Inspired by Google's simple converter")

# Unit categories and conversion logic
unit_categories = {
    "Length": {
        "Meter": 1,
        "Kilometer": 0.001,
        "Centimeter": 100,
        "Millimeter": 1000,
        "Mile": 0.000621371,
        "Yard": 1.09361,
        "Foot": 3.28084,
        "Inch": 39.3701
    },
    "Weight / Mass": {
        "Kilogram": 1,
        "Gram": 1000,
        "Milligram": 1e6,
        "Pound": 2.20462,
        "Ounce": 35.274
    },
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Time": {
        "Second": 1,
        "Minute": 1/60,
        "Hour": 1/3600,
        "Day": 1/86400
    },
    "Speed": {
        "m/s": 1,
        "km/h": 3.6,
        "mph": 2.23694,
        "ft/s": 3.28084
    },
    "Area": {
        "Square Meter": 1,
        "Square Kilometer": 1e-6,
        "Square Centimeter": 10000,
        "Square Millimeter": 1e6,
        "Square Mile": 3.861e-7,
        "Square Yard": 1.19599,
        "Square Foot": 10.7639,
        "Square Inch": 1550
    },
    "Volume": {
        "Cubic Meter": 1,
        "Liter": 1000,
        "Milliliter": 1e6,
        "Cubic Centimeter": 1e6,
        "Cubic Inch": 61023.7,
        "Cubic Foot": 35.3147
    },
    "Digital Storage": {
        "Byte": 1,
        "Kilobyte": 1/1024,
        "Megabyte": 1/(1024**2),
        "Gigabyte": 1/(1024**3),
        "Terabyte": 1/(1024**4)
    },
    "Energy": {
        "Joule": 1,
        "Kilojoule": 0.001,
        "Calorie": 0.239006,
        "Kilocalorie": 0.000239006,
        "Watt-hour": 0.000277778
    },
    "Pressure": {
        "Pascal": 1,
        "Bar": 1e-5,
        "PSI": 0.000145038,
        "Atmosphere": 9.8692e-6
    },
    "Power": {
        "Watt": 1,
        "Kilowatt": 0.001,
        "Horsepower": 0.00134102
    }
}

# Category selection
category = st.selectbox("Select a Unit Category", list(unit_categories.keys()))
value = st.number_input("Enter value", min_value=0.0, step=0.1)

# Handle temperature separately
if category == "Temperature":
    temp_units = unit_categories[category]
    from_unit = st.selectbox("From Unit", temp_units)
    to_unit = st.selectbox("To Unit", temp_units)

    def convert_temp(val, from_u, to_u):
        if from_u == to_u:
            return val
        if from_u == "Celsius":
            return val * 9/5 + 32 if to_u == "Fahrenheit" else val + 273.15
        elif from_u == "Fahrenheit":
            return (val - 32) * 5/9 if to_u == "Celsius" else (val - 32) * 5/9 + 273.15
        elif from_u == "Kelvin":
            return val - 273.15 if to_u == "Celsius" else (val - 273.15) * 9/5 + 32

    if st.button("Convert"):
        result = convert_temp(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = **{result:.4f} {to_unit}**")

else:
    units = unit_categories[category]
    from_unit = st.selectbox("From Unit", list(units.keys()))
    to_unit = st.selectbox("To Unit", list(units.keys()))

    def convert_generic(val, from_u, to_u, data):
        return val / data[from_u] * data[to_u]

    if st.button("Convert"):
        result = convert_generic(value, from_unit, to_unit, units)
        st.success(f"{value} {from_unit} = **{result:.4f} {to_unit}**")
