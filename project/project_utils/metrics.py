import pandas as pd
import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls
import plotly.figure_factory as ff

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

def calculate_metrics(y_true, y_pred):
    # accuracy
    accuracy = accuracy_score(y_true, y_pred)

    # precision
    precision = precision_score(y_true, y_pred)

    # recall
    recall = recall_score(y_true, y_pred)

    # f1
    f1 = f1_score(y_true, y_pred)

    trace = go.Table(cells=dict(values=[["Accuracy", "Precision", "Recall", "F1"],
                                        [accuracy, precision, recall, f1]]))

    data = [trace] 
    return py.iplot(data, filename = 'metrics_table')

def calculate_headline_stats(dataframe, filename):
        headline_list = create_headline_word_count_column(dataframe)

        # average length of headlines
        mean = headline_list[1].mean()

        # longest headline
        max = headline_list[1].max()

        # shortest headline
        min = headline_list[1].min()

        # std deviation for headlines
        std_dev = headline_list[1].std()

        trace = go.Table(cells=dict(values=[["Min", "Max", "Mean", "Standard Deviation"],
                                        [min, max, mean, std_dev]]))

        data = [trace] 
        return py.iplot(data, filename=filename)

def create_headline_word_count_column(dataframe):
        headline_list= []
        for column in dataframe.columns:
            if "top" in column:
                sentences = dataframe[column].tolist()
                headline_list += sentences
        
        headline_list = pd.DataFrame(headline_list)
        headline_list = headline_list.replace("[b']", "", regex=True).replace("[-]", " ", regex=True).replace('[^a-zA-Z0-9\s]', '', regex=True)
        headline_list[1] = headline_list[0].apply(lambda x: len(x))
        return headline_list


def draw_headline_distribution(bull_dataframe, bear_dataframe, filename, label):
    bull_headline_list = create_headline_word_count_column(bull_dataframe)
    bear_headline_list = create_headline_word_count_column(bear_dataframe)

    bullish_x = bull_headline_list[1]
    bearish_x = bear_headline_list[1]

    hist_data = [bullish_x, bearish_x]

    group_labels = label

    figure = ff.create_distplot(hist_data, group_labels, show_rug=False)

    return py.iplot(figure, filename=filename)

def draw_word_frequencies(dataframe, title, filename, least=False):
    headline_list = create_headline_word_count_column(dataframe)
    headline_word_counts = headline_list[0].str.split(expand=True).unstack().value_counts(ascending=least)
    data = [go.Bar(
                x = headline_word_counts.index.values[0:25],
                y = headline_word_counts.values[0:25],
                marker= dict(colorscale='Jet',color=headline_word_counts.values[2:100]),
                text='Word Counts')]

    layout = go.Layout(title=title)
    figure = go.Figure(data=data, layout=layout)
    return py.iplot(figure, filename=filename)