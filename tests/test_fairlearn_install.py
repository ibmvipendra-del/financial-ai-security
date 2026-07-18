from fairlearn.metrics import MetricFrame
from fairlearn.metrics import selection_rate
from sklearn.metrics import accuracy_score


def main():

    # Protected attribute
    gender = [
        "Male",
        "Female",
        "Male",
        "Female",
        "Male",
        "Female",
    ]

    # Ground truth
    y_true = [
        1,
        1,
        0,
        0,
        1,
        1,
    ]

    # AI predictions
    y_pred = [
        1,
        1,
        0,
        1,
        1,
        1,
    ]

    metric_frame = MetricFrame(

        metrics={
            "accuracy": accuracy_score,
            "selection_rate": selection_rate,
        },

        y_true=y_true,

        y_pred=y_pred,

        sensitive_features=gender,

    )

    print("=" * 60)
    print("FAIRLEARN INSTALLATION SUCCESSFUL")
    print("=" * 60)

    print("\nOverall Metrics")
    print(metric_frame.overall)

    print("\nMetrics by Gender")
    print(metric_frame.by_group)


if __name__ == "__main__":
    main()