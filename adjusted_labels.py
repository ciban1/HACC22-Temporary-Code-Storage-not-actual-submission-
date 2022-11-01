def make_graph_eye_friendly(figure):
    x_tick_amount = len(figure.get_axes()[0].get_xticks())
    if x_tick_amount > 10:
        figure.autofmt_xdate()
        for i in range(x_tick_amount):
            figure.set_figwidth(figure.get_figwidth() + 0.15)
        for tick in figure.get_axes()[0].xaxis.get_major_ticks():
            tick.label.set_fontsize(10 - 0.05 * x_tick_amount)
