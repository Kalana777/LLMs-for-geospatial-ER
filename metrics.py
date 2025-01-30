from sklearn.metrics import precision_score, recall_score, f1_score


def calculate_metrics(predictions, labels, avg):
    # Convert "Yes" to 1 and "No" to 0 for predicted labels
    # predicted = [1 if label == "Yes" else 0 if label == "No" else 3 for label in predictions]

    # Ensure ground truth is already in binary format
    # ground_truth = [1 if label == "Yes" else 0 if label == "No" else 3 for label in labels]
    # Calculate metrics
    precision = precision_score(labels, predictions, average=avg)
    recall = recall_score(labels, predictions, average=avg)
    f1 = f1_score(labels, predictions, average=avg)

    return {
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1
    }


def calculate_metrics2(y_pred, valid_y_tensor):
    tot_p = 0
    true_p = 0
    pred_p = 0

    # y_pred = [
    #     1 if label == "same_as" or "same" else 2 if label == "part_of" else 3 if label == "serves" else 0 if label == "unknown" else 4
    #     for label in predictions]

    for i in range(len(y_pred)):

        if valid_y_tensor[i] > 0:
            tot_p += 1

            if y_pred[i] == valid_y_tensor[i]:
                true_p += 1

        if y_pred[i] > 0:
            pred_p += 1

    f1 = 0.0
    prec = 0.0
    rec = 0.0

    if tot_p and pred_p:
        rec = true_p / tot_p
        prec = true_p / pred_p

        if rec > 0 or prec > 0:
            f1 = 2 * prec * rec / (prec + rec)

    print('P: ' + str(round(prec, 4)) + '  |  R: ' + str(round(rec, 4)) + '  |  F1: ' + str(round(f1, 4)))

    return {
        'precision': prec,
        'recall': rec,
        'f1': f1
    }


def calc_mets_my(predictions, labels):

    tp=0
    fp=0
    fn=0
    tn=0
    for pred,lab in zip(predictions, labels):
        if lab==1 and pred==1:
            tp=tp+1
        elif lab==0 and pred==0:
            tn=tn+1
        elif lab==1:
            fn=fn+1
        elif lab==0:
            fp=fp+1

    prec = tp/(tp+fp)
    rec = tp/(tp+fn)

    return {
        "Precision": prec,
        "Recall": rec,
        "F1 Score": (2*prec*rec)/(prec+rec)
    }




