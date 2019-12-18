import numpy as np
import plotly.graph_objects as go


x =  np.array([1,2,3,4,5])
y = np.array([3,2,1,3,5])

fig = go.Figure(
    data=go.Bar(x=x,y=y),
    layout_title_text = "test bar graph",
    # textposition="auto",
    # name="Data y",
    # marker_color="pink"
    )

fig2 = go.Figure(
    data = go.Scatter(
        x=x,
        y=y,
        mode='lines'

    )
)

fig3 = go.Figure(
    data = go.Pie(
        labels=x,
        values=y
    ),
    layout_title_text ="contoh diagram pie"
)
# fig.write_html('first_figure.html', auto_open=True)
# fig2.write_html('figure2.html', auto_open=True)
fig3.write_html('figure3.html', auto_open=True)