import chart_studio.plotly as py
import chart_studio.tools as tls




def upload_chart(fig, filename):
    py.plot(fig, filename = filename, auto_open=True)

def generate_iframe(url):
    return tls.get_embed(url)



