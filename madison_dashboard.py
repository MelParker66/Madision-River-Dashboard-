import streamlit as st 
import pandas as pd 
import os 

import requests

def get_weather(api_key, location="West Yellowstone,US"):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&units=imperial&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

weather = get_weather("a2cfdfe2546b26b83b6f5159076e4ef2")

st.set_page_config(page_title="Madison River Hatch Guide", layout="wide") 

st.title("Madison River Hatch Guide")

col_left, col_right = st.columns([2, 1])

with col_left:
    st.image("C:/Users/Doug/Documents/MadisonFlies/Dan.jpeg", width=600)  # Adjust path and width as needed

with col_right:
    if weather:
        st.markdown("### 🌤️ Current Weather in West Yellowstone")
        st.caption(f"*{weather['weather'][0]['description'].title()}*")
        st.metric("Temperature", f"{weather['main']['temp']} °F")
        st.metric("Wind", f"{weather['wind']['speed']} mph")
    else:
        st.warning("Weather data not available.")

st.subheader("Montana Fly Selection by Month") 

import requests

def get_weather(a2cfdfe2546b26b83b6f5159076e4ef2, location="West Yellowstone,US"):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&units=imperial&appid={a2cfdfe2546b26b83b6f5159076e4ef2}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

months = [
    "March", "April", "May", "June",
    "July", "August", "September", "October"
]

selected_month = st.selectbox("Choose a month", months)

fly_types = ["All", "Dry Fly", "Nymph", "Streamer"]
selected_type = st.selectbox("Filter by fly type", fly_types)


hatch_summaries = {
    "March": "Early-season fishing with Midges and subsurface patterns. Cold water, slow takes.",
    "April": "Blue Wing Olives and Midges dominate. Cloudy days bring surface action.",
    "May": "Western March Browns appear sporadically. Water warms, fish get active.",
    "June": "Pale Morning Duns and Yellow Sallies hatch strong. Evening Caddis skittering begins.",
    "July": "Caddis and PMDs continue. Terrestrials start showing watch for hoppers.",
    "August": "Grasshoppers and Tricos take over. Big surface eats and technical mornings.",
    "September": "Beetles and hoppers still strong. Cooler temps bring BWO resurgence.",
    "October": "Blue Wing Olives return. Browns get aggressive great streamer month."
}

st.markdown(f"#### 🗓️ Hatch Summary for {selected_month}")
st.info(hatch_summaries[selected_month])

fly_images = {
    "Blue Wing Olive": { 
        "months": ["April", "May", "October"], 
        "size": "14-22",
        "type": "Dry Fly",
        "image": "C:/Users/Doug/Documents/MadisonFlies/Blue_Wing_Olive.jpg",
        "notes": "Effective on cloudy days; triggers surface rises in slower water."  
    },
    "Midge": {
        "months": ["March", "April"],
        "size": "16–22",
        "type": "Nymph",
        "image": "C:/Users/Doug/Documents/MadisonFlies/Midge.jpg",
        "notes": "Early-season staple; best fished subsurface."
    },
    "Western March Brown": {
        "months": ["May"],
        "size": "12–14",
        "type": "Dry Fly",
        "image": "C:/Users/Doug/Documents/MadisonFlies/Western_March_Brown.jpg",
        "notes": "Sporadic hatch, but big trout love them when they appear."
    },
    "Pale Morning Dun": {
        "months": ["June", "July", "August"],
        "size": "14–20",
        "type": "Dry Fly",
        "image": "C:/Users/Doug/Documents/MadisonFlies/Pale_Morning.jpg",
        "notes": "Most abundant mayfly in June; drives consistent surface feeding."
    },
    "Yellow Sally": {
        "months": ["June", "July"],
        "size": "10–12",
        "type": "Dry Fly",
        "image": "C:/Users/Doug/Documents/MadisonFlies/Yellow_Sally.jpg",
        "notes": "Small stonefly that hatches in warm weather; great for pocket water."
    },
    "Caddis (Various)": {
        "months": ["June", "July", "August"],
        "size": "12–20",
        "type": "Dry/Emerger",
        "image": "C:/Users/Doug/Documents/MadisonFlies/Caddis_Various_Fly.jpg",
        "notes": "Evening hatches dominate summer; great for skittering across riffles."
    },
    "Grasshopper": {
        "months": ["August", "September", "October"],
        "size": "8–14",
        "type": "Terrestrial",
        "image": "C:/Users/Doug/Documents/MadisonFlies/Grasshopper.jpg",
        "notes": "Big surface takes in late summer; twitch across banks and seams."
    },
    "Beetle": {
        "months": ["September", "October"],
        "size": "12–18",
        "type": "Terrestrial",
        "image": "C:/Users/Doug/Documents/MadisonFlies/Beetle.jpg",
        "notes": "Foam-bodied and flashy; great for slow seams and undercut banks."
    },
    "Trico Mayfly": {
        "months": ["July", "August"],
        "size": "18–22",
        "type": "Dry Fly",
        "image": "C:/Users/Doug/Documents/MadisonFlies/Trico_Mayfly.jpg",
        "notes": "Tiny mayfly best fished in slow water; often ignored in fast currents."
    },
    "Sparkle Minnow": {
        "image": "C:/Users/Doug/Documents/MadisonFlies/sparkle_minnow.jpg",
        "months": ["August", "September"],
        "type": "Streamer",
        "size": "2-3",
        "notes": "Early morning, cast it across or downstream and then retrieve with a series of strops and pauses."
}

}
months = [
    "March", "April", "May", "June",
    "July", "August", "September", "October"
]

st.markdown(f"### 🪶 Flies for {selected_month}")

col1, col2 = st.columns(2)
count = 0

for fly, data in fly_images.items():
    if selected_month in data["months"]:
        if selected_type == "All" or data["type"] == selected_type:
            target_col = col1 if count % 2 == 0 else col2
            with target_col:
                if os.path.exists(data["image"]):
                    st.image(data["image"], width=150)
                else:
                    st.warning(f"Image not found for {fly}")
                st.caption(f"**{fly}** – {data['type']}, Size {data['size']}")
                st.write(data["notes"])
            count += 1

import streamlit as st

st.title("Madison River Flyfishing Chatbot")

# Simple seasonal fly logic
def get_fly_recommendation(month, technique):
    month = month.lower()
    technique = technique.lower()

    if technique == "nymphing":
        if month in ["march", "april", "may"]:
            return "Spring nymphing: try rubber legs, Prince Nymphs, Hare's Ear, and San Juan Worms."
        elif month in ["june", "july", "august"]:
            return "Summer nymphing: use rubber legs, Hare's Ear, and tandem rigs."
        else:
            return "Fall/winter nymphing: BWOs, midges, and soft hackles. Use minimal weight."

    elif technique == "dry fly":
        if month in ["june", "july", "august"]:
            return "Summer dry fly: match the hatch with PMDs, caddis, salmonflies, and terrestrials."
        else:
            return "Shoulder season dry fly: BWOs, midges, and attractors like Royal Trude."

    elif technique == "streamer":
        return "Streamer tip: fish early mornings with Woolly Buggers or 20-Inchers in lower sections."

    else:
        return "Try soft hackles in shallow water. Adjust tippet size by dividing hook size by 3."

# UI
month = st.selectbox("Choose your fishing month", [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
])

technique = st.radio("Select your technique", ["Nymphing", "Dry Fly", "Streamer", "Other"])

if st.button("Get Fly Recommendation"):
    st.markdown(f"**Bot:** {get_fly_recommendation(month, technique)}")




















