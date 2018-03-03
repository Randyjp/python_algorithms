def generate_histogram_data(events):
    # TODO: Your work goes here.
    HistogramData = {}
    count_valid = 0
    # fill hours
    for hour in range(24):
        HistogramData[hour] = 0

    for event in events:
        if check_valid_email(event['recipient_email']):
            if HistogramData.get(event['hour'], -1) >= 0:
                HistogramData[event['hour']] += 1
                count_valid += 1

    if count_valid < 5:
        return None

    HistogramData = normalize_historgram(HistogramData)

    return HistogramData


def normalize_historgram(hist):
    maximus = max(hist.values())
    minimum = min(hist.values())

    for key, value in hist.items():
        hist[key] = normalize(value, minimum, maximus)

    return hist


def normalize(value, min, max):
    normal = (value - min) / (max - min)
    return round(normal, 2)


def check_valid_email(email):
    if len(email) > 40:
        return False

    valid_domains = ['googlemail.com', 'gmail.com']
    domain = email.split('@')[1]

    return True if domain in valid_domains else False


#testing code
# events = [{'hour': 1, 'recipient_email': 'foo@gmail.com'}, {'hour': 1, 'recipient_email': 'foo@gmail.com'},
#         {'hour': 2, 'recipient_email': 'bar@gmail.com'}, {'hour': 2, 'recipient_email': 'bar@gmail.com'},
#         {'hour': 3, 'recipient_email': 'baz@gmail.com'}]

events = []
print(generate_histogram_data(events))
