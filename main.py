import streamlit as st

# Unit converter functions
def convert_length(value, from_unit, to_unit):
    if from_unit == "Meters" and to_unit == "Kilometers":
        return value / 1000
    elif from_unit == "Kilometers" and to_unit == "Meters":
        return value * 1000
    elif from_unit == "Meters" and to_unit == "Centimeters":
        return value * 100
    elif from_unit == "Centimeters" and to_unit == "Meters":
        return value / 100
    elif from_unit == "Meters" and to_unit == "Millimeters":
        return value * 1000
    elif from_unit == "Millimeters" and to_unit == "Meters":
        return value / 1000
    else:
        return "Invalid unit"

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32 
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value -32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32 
    else:
        return "Invalid Units"

def convert_weight(value, from_unit, to_unit):
    if from_unit == "Kilograms" and to_unit == "Grams":
        return value * 1000
    elif from_unit == "Grams" and to_unit == "Kilograms":
        return value / 1000
    elif from_unit == "Kilograms" and to_unit == "Pounds":
        return value * 2.20462
    elif from_unit == "Pounds" and to_unit == "Kilograms":
        return value / 2.20462
    elif from_unit == "Grams" and to_unit == "Pounds":
        return value / 453.592
    elif from_unit == "Pounds" and to_unit == "Grams":
        return value * 453.592
    else:
        return "Invalid Units"

# Streamlit UI
st.title("Unit Converter 🌍💡")
st.write("Convert between various units of length 📏, temperature ❄️🔥, and weight 🔄 with ease using this intuitive unit converter app! 🌍")

# Select unit type
unit_type = st.selectbox("Choose Unit Type", ["Length", "Temperature", "Weight"])

# Input for Value 
value = st.number_input("Enter value to convert", min_value=0.0)

if unit_type == "Length":
    length_units = ["Meters", "Kilometers", "Centimeters", "Millimeters"]
    from_unit = st.selectbox("From Unit", length_units)
    to_unit = st.selectbox("To Unit", length_units)
    if st.button("Convert 🔄"):
        result = convert_length(value, from_unit, to_unit)
        st.write(f"Result: {result} {to_unit}")

elif unit_type == "Temperature":
    temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From Unit", temperature_units)
    to_unit = st.selectbox("To Unit", temperature_units)
    if st.button("Convert 🔄"):
        result = convert_temperature(value, from_unit, to_unit)
        st.write(f"Result: {result} {to_unit}")

elif unit_type == "Weight":
    weight_units = ["Grams", "Kilograms", "Pounds"]
    from_unit = st.selectbox("From Unit", weight_units)
    to_unit = st.selectbox("To Unit", weight_units)
    if st.button("Convert 🔄"):
        result = convert_weight(value, from_unit, to_unit)
        st.write(f"Result: {result} {to_unit}")

# Horizontal line for separation
st.markdown("---")

# FAQs Section
st.subheader("Frequently Asked Questions (FAQs) ❓")

with st.expander("What is this Unit Converter app?"):
    st.write("""
        This is a simple app to convert between different units of **length**, **temperature**, and **weight**. You can convert units such as meters to kilometers, Celsius to Fahrenheit, and grams to kilograms easily!
    """)

with st.expander("How do I use the converter?"):
    st.write("""
        1. Choose the unit type (Length, Temperature, or Weight).
        2. Enter the value you want to convert.
        3. Select the "from" and "to" units.
        4. Click the "Convert" button to see the result.
    """)

with st.expander("What units can I convert?"):
    st.write("""
        - **Length**: Meters, Kilometers, Centimeters, Millimeters
        - **Temperature**: Celsius, Fahrenheit, Kelvin
        - **Weight**: Grams, Kilograms, Pounds
    """)

with st.expander("Why is the conversion result showing as 'Invalid unit'?"):
    st.write("""
        The error message 'Invalid unit' appears when the selected units do not match the supported conversions. Make sure you choose the correct units for conversion.
    """)

with st.expander("Can I convert between other units?"):
    st.write("""
        Currently, the app supports conversions for **length**, **temperature**, and **weight** only. If you need additional units, feel free to suggest them, and we may consider adding them in future updates!
    """)