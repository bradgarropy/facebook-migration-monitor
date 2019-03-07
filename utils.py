def pretty_time(seconds):
    """ Converts second to a pretty format.

    Parameters:
        seconds (float): time duration in seconds.

    Returns:
        pretty (str): pretty formatted time.
    """

    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    if days > 0:
        pretty = "%dd %dh %dm %ds" % (days, hours, minutes, seconds)
    elif hours > 0:
        pretty = "%dh %dm %ds" % (hours, minutes, seconds)
    elif minutes > 0:
        pretty = "%dm %ds" % (minutes, seconds)
    else:
        pretty = "%ds" % seconds

    return pretty


def percentage(part, whole):
    """ Calculates a percent.

    Parameters:
        part (int):  numerator.
        whole (int): denominator.

    Returns:
        percentage (float): percent between zero and one hundred.
    """

    percent = float(part) / float(whole) * 100

    return percent
