from plotly.offline import plot
from .models import Account

import plotly.graph_objects as go


# reading data from db 
def prepare_db_data(plotly_values: list, plotly_labels: list):
    # NOTE :
    """
    I did not want to read all data because they are all 
    the same data which is being created automatic every time
    you login, the reason why i am only getting first object
    in the database and display it on PLOTLY GRAPH
    """
    # getting fist object from db
    _data = Account.objects.all().first()

    # check if object exists
    if _data:
        # getting data and split them by comman separate
        weekly_day = _data.weekly_day_record.split(',')
        transaction = _data.trasaction_day_record.split(',')

        # check weekly data type and append to the list
        if type(weekly_day) == list:
            for day in weekly_day:
                plotly_labels.append(day)

         # check transaction data type and append to the list
        if type(transaction) == list:
            for amount in transaction:
                plotly_values.append(amount)


def pie_chart():
    # intialize plotly value array and label array
    plotly_values = []
    plotly_labels = []

    # gettting data
    prepare_db_data(plotly_values, plotly_labels)

    # preparing plotly graph 
    plotly_graph = {
       'data':  {
            "values": plotly_values,
            "labels": plotly_labels,
            "domain": {"column": 0},
            "name": "Weekly Day",
            "hoverinfo":"label+percent+name",
            "hole": .4,
            "type": "pie"
        },
    }
    plot_div = plot(plotly_graph, output_type='div',filename='donut')

    return plot_div


def bar_chart():
    # intialize plotly value array and label array
    plotly_values = []
    plotly_labels = []

    # gettting data
    prepare_db_data(plotly_values, plotly_labels)

    plot_div = plot(go.Figure([go.Bar(x=plotly_labels, y=plotly_values)]), output_type='div',filename='donut')

    return plot_div
