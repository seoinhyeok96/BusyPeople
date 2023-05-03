import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

from wordcloud import WordCloud

import streamlit as st

df = pd.read_csv('/app/busypeople-stramlit/data/어간.csv')

df.columns = ['index','count']

dict_0 = dict(zip(df['index'], df['count']))

# Create and generate a word cloud image:
wc = WordCloud(
    max_font_size=200,
    background_color='white',
    # relative_scaling=0.5,
    width=800,
    height=400,
    font_path='/app/busypeople-stramlit/font/NanumBarunGothic.ttf'
    )
cloud = wc.generate_from_frequencies(dict(dict_0))

fig, ax = plt.subplots(
    figsize=(12,12)
)

#주석

# Display the generated image:
plt.imshow(cloud, interpolation='bilinear')
plt.axis("off")
plt.show()
st.pyplot(fig)

number = st.slider('Insert a number', min_value=10, step=1)
bar_df = df.sort_values(by=['count'],ascending=False).reset_index(drop=True).iloc[:number]
st.bar_chart(bar_df)


from wordcloud import WordCloud, STOPWORDS
import plotly.graph_objs as go

word_list=[]
freq_list=[]
fontsize_list=[]
position_list=[]
orientation_list=[]
color_list=[]

for (word, freq), fontsize, position, orientation, color in wc.layout_:
    word_list.append(word)
    freq_list.append(freq)
    fontsize_list.append(fontsize)
    position_list.append(position)
    orientation_list.append(orientation)
    color_list.append(color)
    
# get the positions
x=[]
y=[]
for i in position_list:
    x.append(i[0])
    y.append(i[1])
        
# get the relative occurence frequencies
new_freq_list = []
for i in freq_list:
    new_freq_list.append(i*100)

trace = go.Scatter(x=x, 
                    y=y, 
                    textfont = dict(size=new_freq_list,
                                    color=color_list),
                    hoverinfo='text',
                    hovertext=['{0}{1}'.format(w, f) for w, f in zip(word_list, freq_list)],
                    mode='text',  
                    text=word_list
                    )

layout = go.Layout({'xaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False},
                    'yaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False}})

fig = go.Figure(data=[trace], layout=layout)

fig

import plotly.graph_objects as go

fig = go.Figure(data=go.Scatter(x=[1, 2, 3], y=[4, 5, 6], mode='markers', hoverinfo='x+y+z',
                                xaxis='x1', yaxis='y1'))

fig.add_trace(go.Scatter(x=[2, 3, 4], y=[5, 6, 7], mode='markers', hoverinfo='x+y+z',
                          xaxis='x2', yaxis='y2'))

fig.update_layout(xaxis=dict(domain=[0, 0.45]), yaxis=dict(domain=[0, 1]),
                  xaxis2=dict(domain=[0.55, 1]), yaxis2=dict(domain=[0, 1]))

fig

with st.container():
    url = "https://public.tableau.com/views/KBOOPS/1?:language=ko-KR&:showVizHome=no&:embed=true"
    html = f'''
        <iframe src={url} width=1600 height=900></iframe>
    '''
    st.markdown(html, unsafe_allow_html=True)

import streamlit as st
from streamlit_elements import elements, mui
from streamlit_elements import dashboard



with elements("dashboard"):

    with dashboard():
        st.markdown(html, unsafe_allow_html=True)
    # You can create a draggable and resizable dashboard using
    # any element available in Streamlit Elements.
    # First, build a default layout for every element you want to include in your dashboard

    layout = [
        # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
        dashboard.Item("first_item", 0, 0, 2, 2),
        dashboard.Item("second_item", 2, 0, 2, 2, isDraggable=False, moved=False),
        dashboard.Item("third_item", 0, 2, 1, 1, isResizable=False),
    ]

    # Next, create a dashboard layout using the 'with' syntax. It takes the layout
    # as first parameter, plus additional properties you can find in the GitHub links below.

    with dashboard.Grid(layout):
        mui.Paper("First item", key="first_item")
        mui.Paper("Second item (cannot drag)", key="second_item")
        mui.Paper("Third item (cannot resize)", key="third_item")

    # If you want to retrieve updated layout values as the user move or resize dashboard items,
    # you can pass a callback to the onLayoutChange event parameter.

    def handle_layout_change(updated_layout):
        # You can save the layout in a file, or do anything you want with it.
        # You can pass it back to dashboard.Grid() if you want to restore a saved layout.
        print(updated_layout)

    with dashboard.Grid(layout, onLayoutChange=handle_layout_change):
        mui.Paper("First item", key="first_item")
        mui.Paper("Second item (cannot drag)", key="second_item")
        mui.Paper("Third item (cannot resize)", key="third_item")