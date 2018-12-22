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