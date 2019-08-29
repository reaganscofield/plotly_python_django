from plotly.offline import plot
from .models import Account

def pie_chart():
    # intialize plotly value array and label array
    plotly_values = []
    ploltly_labels = []

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
                ploltly_labels.append(day)

         # check transaction data type and append to the list
        if type(transaction) == list:
            for amount in transaction:
                plotly_values.append(amount)

    # preparing plotly graph 
    plotly_graph = {
       'data':  {
            "values": plotly_values,
            "labels": ploltly_labels,
            "domain": {"column": 0},
            "name": "Weekly Day",
            "hoverinfo":"label+percent+name",
            "hole": .4,
            "type": "pie"
        },
    }
    plot_div = plot(plotly_graph, output_type='div',filename='donut')

    return plot_div