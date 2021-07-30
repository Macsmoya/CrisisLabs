import plotly.express as px
import plotly.express as px
df = px.data.gapminder().query("continent=='Europe'")
print(df)
fig = px.line_3d(df, x="gdpPercap", y="pop", z="year", color='country')
fig.show()
