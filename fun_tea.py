
import streamlit as st
import math

st.set_page_config(
    page_title="My Chai Recipe Lab",
    page_icon="☕",
    layout="centered"
)

st.title("☕ My Chai Recipe Calculator")
st.caption("Experiment, measure and develop your signature chai.")

# ---------------------------------
# RECIPE CONFIGURATION
# All quantities are per 100 ml serving
# ---------------------------------

RECIPES = {
    "Strong Kadak Chai": {
        "water": 60,
        "milk": 60,
        "tea": 2.2,
        "ginger": 0,
        "cardamom": 0,
        "cinnamon": 0,
    },
    "Ginger Chai": {
        "water": 60,
        "milk": 60,
        "tea": 2.0,
        "ginger": 2.0,
        "cardamom": 0,
        "cinnamon": 0,
    },
    "Elaichi Chai": {
        "water": 60,
        "milk": 60,
        "tea": 2.0,
        "ginger": 0,
        "cardamom": 0.25,
        "cinnamon": 0,
    },
    "Masala Chai": {
        "water": 60,
        "milk": 60,
        "tea": 2.0,
        "ginger": 1.5,
        "cardamom": 0.25,
        "cinnamon": 0.15,
    }
}

SUGAR_LEVELS = {
    "Low": 4,
    "Medium": 6,
    "High": 8
}

# ---------------------------------
# USER INPUTS
# ---------------------------------

st.subheader("1. Enter your requirements")

col1, col2 = st.columns(2)

with col1:
    cups = st.number_input(
        "Number of cups",
        min_value=1,
        max_value=1000,
        value=5,
        step=1
    )

with col2:
    cup_size = st.selectbox(
        "Cup size",
        [100, 120, 150, 180],
        index=0,
        format_func=lambda x: f"{x} ml"
    )

sugar = st.selectbox(
    "Sugar preference",
    ["Low", "Medium", "High"]
)

chai_type = st.selectbox(
    "Select chai type",
    list(RECIPES.keys())
)

# ---------------------------------
# RECIPE CALCULATION
# ---------------------------------

recipe = RECIPES[chai_type]

scale = (cups * cup_size) / 100

water = recipe["water"] * scale
milk = recipe["milk"] * scale
tea = recipe["tea"] * scale
ginger = recipe["ginger"] * scale
cardamom = recipe["cardamom"] * scale
cinnamon = recipe["cinnamon"] * scale
sugar_qty = SUGAR_LEVELS[sugar] * scale

# ---------------------------------
# OUTPUT
# ---------------------------------

st.divider()
st.subheader("2. Your calculated recipe")

st.success(f"{cups} cups of {chai_type}")

col1, col2 = st.columns(2)

with col1:
    st.metric("Water", f"{water:.0f} ml")
    st.metric("Milk", f"{milk:.0f} ml")
    st.metric("Tea powder", f"{tea:.1f} g")
    st.metric("Sugar", f"{sugar_qty:.1f} g")

with col2:
    st.metric("Ginger", f"{ginger:.1f} g")
    st.metric("Cardamom", f"{cardamom:.1f} g")
    st.metric("Cinnamon", f"{cinnamon:.1f} g")

# ---------------------------------
# COOKING PROCEDURE
# ---------------------------------

st.divider()
st.subheader("3. Preparation procedure")

st.write("### Step 1: Prepare ingredients")
st.write(
    f"Measure {water:.0f} ml water and "
    f"{milk:.0f} ml milk."
)

st.write(
    f"Measure {tea:.1f} g tea powder "
    f"and {sugar_qty:.1f} g sugar."
)

if ginger > 0:
    st.write(
        f"Wash and crush {ginger:.1f} g fresh ginger."
    )

if cardamom > 0:
    st.write(
        f"Lightly crush {cardamom:.1f} g cardamom."
    )

if cinnamon > 0:
    st.write(
        f"Prepare {cinnamon:.1f} g cinnamon."
    )

st.write("### Step 2: Boil water")

st.write(
    "Add water to a clean vessel. "
    "Heat until it starts boiling."
)

if ginger > 0 or cardamom > 0 or cinnamon > 0:
    st.write("### Step 3: Extract spice flavours")
    st.write(
        "Add the measured spices and simmer "
        "for approximately 2–3 minutes."
    )

st.write("### Step 4: Add tea powder")
st.write(
    f"Add {tea:.1f} g tea powder. "
    "Brew for approximately 2 minutes."
)

st.write("### Step 5: Add milk and sugar")
st.write(
    f"Add {milk:.0f} ml milk and "
    f"{sugar_qty:.1f} g sugar."
)

st.write("### Step 6: Simmer")
st.write(
    "Simmer gently for 3–4 minutes. "
    "Avoid excessive boiling."
)

st.write("### Step 7: Strain and serve")
st.write(
    f"Strain into {cups} cups and serve fresh."
)

st.info(
    "Note: These are starting experimental ratios. "
    "Actual final volume will vary due to evaporation. "
    "Measure the finished yield and adjust your next batch."
)

# ---------------------------------
# EXPERIMENT NOTES
# ---------------------------------

st.divider()
st.subheader("4. Record your experiment")

rating = st.slider(
    "How was the taste?",
    min_value=1,
    max_value=5,
    value=3
)

notes = st.text_area(
    "Your observations",
    placeholder="Example: Tea too strong, less creamy, "
                "ginger flavour was good..."
)

if st.button("Save experiment notes"):
    st.success(
        f"Experiment rating: {rating}/5. "
        "Copy your observations into your recipe notebook."
    )

# ---------------------------------
# DOWNLOAD RECIPE
# ---------------------------------

recipe_text = f"""
CHAI RECIPE
===========

Chai: {chai_type}
Cups: {cups}
Cup size: {cup_size} ml
Sugar: {sugar}

INGREDIENTS
-----------
Water: {water:.1f} ml
Milk: {milk:.1f} ml
Tea: {tea:.1f} g
Sugar: {sugar_qty:.1f} g
Ginger: {ginger:.1f} g
Cardamom: {cardamom:.1f} g
Cinnamon: {cinnamon:.1f} g

PREPARATION
-----------
1. Boil water.
2. Extract spice flavours if applicable.
3. Add tea and brew.
4. Add milk and sugar.
5. Simmer gently for 3-4 minutes.
6. Strain and serve fresh.

EXPERIMENT RATING: {rating}/5
NOTES: {notes}
"""

st.download_button(
    "Download my chai recipe",
    data=recipe_text,
    file_name="my_chai_recipe.txt",
    mime="text/plain"
)