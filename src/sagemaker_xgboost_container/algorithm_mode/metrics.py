from sagemaker_algorithm_toolkit import metrics as m


# https://docs.aws.amazon.com/sagemaker/latest/dg/xgboost-tuning.html
def initialize():
    return m.Metrics(
        m.Metric(name="validation:auc",
                 direction=m.Metric.MAXIMIZE,
                 regex=".*\\[[0-9]+\\].*#011validation-auc:(\\S+)"),
        m.Metric(name="validation:error",
                 direction=m.Metric.MINIMIZE,
                 regex=".*\\[[0-9]+\\].*#011validation-error:(\\S+)"),
        m.Metric(name="validation:logloss",
                 direction=m.Metric.MINIMIZE,
                 regex=".*\\[[0-9]+\\].*#011validation-logloss:(\\S+)"),
        m.Metric(name="validation:mae",
                 direction=m.Metric.MINIMIZE,
                 regex=".*\\[[0-9]+\\].*#011validation-mae:(\\S+)"),
        m.Metric(name="validation:map",
                 direction=m.Metric.MAXIMIZE,
                 regex=".*\\[[0-9]+\\].*#011validation-map:(\\S+)"),
        m.Metric(name="validation:merror",
                 direction=m.Metric.MINIMIZE,
                 regex=".*\\[[0-9]+\\].*#011validation-merror:(\\S+)"),
        m.Metric(name="validation:mlogloss",
                 direction=m.Metric.MINIMIZE,
                 regex=".*\\[[0-9]+\\].*#011validation-mlogloss:(\\S+)"),
        m.Metric(name="validation:ndcg",
                 direction=m.Metric.MAXIMIZE,
                 regex=".*\\[[0-9]+\\].*#011validation-ndcg:(\\S+)"),
        m.Metric(name="validation:rmse",
                 direction=m.Metric.MINIMIZE,
                 regex=".*\\[[0-9]+\\].*#011validation-rmse:(\\S+)"))