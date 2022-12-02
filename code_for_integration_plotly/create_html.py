import plotly.io as pio


def write_html(fig, file):
    pio.write_html(fig, file=file, auto_open=True)

