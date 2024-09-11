import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from vega_datasets import data


def render_map():
    # Generate random coordinates and past scores
    np.random.seed(42)
    data_points = pd.DataFrame({
        'latitude': np.random.uniform(30, 48, 5),  # Latitude range for USA
        'longitude': np.random.uniform(-125, -70, 5),  # Longitude range for USA
        'past_score': np.random.randint(90, 100, 5),
        'current_score': [99, 97 , 95 , 92 , 87],
        'future_score': np.random.randint(90, 100, 5)  # Random past scores between 85 and 100
    })

    # Manually categorize the current scores into colors
    def score_to_color(score):
        if score >= 95:
            return 'green'
        elif score >= 90:
            return 'yellow'
        else:
            return 'red'
    
    # Create a new column for colors based on current_score
    data_points['color'] = data_points['current_score'].apply(score_to_color)

    print(data_points)

    # Load US states data
    states = alt.topo_feature(data.us_10m.url, 'states')

    # Create selection for points
    selection = alt.selection_single(fields=['longitude', 'latitude'], on='click')

    # Create base map with darker colors
    base = alt.Chart(states).mark_geoshape(
        fill='black',  # Dark fill for map
        stroke='gray'  # Light gray for state borders
    ).project('albersUsa').properties(
    )

    # Create points with the manual color assignment
    points = alt.Chart(data_points).mark_circle(size=100).encode(
        longitude='longitude:Q',
        latitude='latitude:Q',
        tooltip=['past_score:Q', 'current_score:Q', 'future_score:Q'],
        color=alt.Color('color:N', scale=None),  # Use the color column directly
    ).add_selection(
        selection  # Add click selection
    )

    # Combine base map and points
    chart = (base + points).properties(
        title='Your Plants',
        background="black",  # Dark background for the chart
        padding={'left': 20, 'right': 20, 'top': 20, 'bottom': 20}
    )

    # Render the chart in Streamlit
    with st.expander("SUMMARY OF YOUR PLANTS"):
        st.altair_chart(chart, use_container_width=True)


