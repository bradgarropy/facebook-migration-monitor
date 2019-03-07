# standard imports
import logging
import random
import time

# custom imports
import utils


def get_service_status(host, port):
    """ Get the status of a service.

    Parameters:
        host (str): dns or ip address.
        port (int): service port number.

    Returns:
        status (bool): true if operational, false otherwise.
    """

    # simulate request
    delay = random.uniform(0.000, 0.500)
    time.sleep(delay)

    # mock status
    status = random.choice([True, False])

    return status


def get_migration_status(host, old_port, new_port):
    """ Get the migration status of a service.

    Parameters:
        host (str):     dns or ip address.
        old_port (int): old service port number.
        new_port (int): new service port number.

    Returns:
        status (str): migrated, unmigrated, duplicate, dead, or unknown.
    """

    old_status = get_service_status(host, old_port)
    new_status = get_service_status(host, new_port)

    if not old_status and not new_status:
        status = "dead"
    elif not old_status and new_status:
        status = "migrated"
    elif old_status and not new_status:
        status = "unmigrated"
    elif old_status and new_status:
        status = "duplicate"

    return status


def progress(index, hosts, average_duration):
    """ Logs monitoring progress.

    Parameters:
        index (int):              iteration index.
        hosts (list):             list of hosts.
        average_duration (float): average monitor duration in seconds.

    Returns:
        None
    """

    total = len(hosts)
    completed = index + 1
    remaining = total - completed
    percent = utils.percentage(completed, total)

    eta = utils.pretty_time(average_duration * remaining)

    logging.info(
        "Monitor is %.4s%% (%s/%s) complete. Approximately %s remaining.",
        percent, completed, total, eta
    )

    return


def output(migration_status):
    """ Create output files.

    Parameters:
        migration_status (dict): migration status dictionary.

    Returns:
        None
    """

    for host, status in migration_status.items():
        file_name = "%s.txt" % status
        with open(file_name, "a") as f:
            f.write(host)

    return


def summary(migration_status, duration):
    """ Logs summary information.

    Parameters:
        migration_status (dict): migration status dictionary.
        duration (int):          duration in seconds.

    Returns:
        None
    """

    completed = migration_status.values().count("migrated") + \
        migration_status.values().count("duplicate") + \
        migration_status.values().count("dead")

    total = len(migration_status)
    complete = utils.percentage(completed, total)

    logging.info("")
    logging.info("Checked %s hosts in %s.", total, utils.pretty_time(duration))
    logging.info("Migration is %.4s%% complete.", complete)
    logging.info("")

    logging.info("== Breakdown ==")
    statuses = set(migration_status.values())

    for status in statuses:
        count = migration_status.values().count(status)
        percent = utils.percentage(count, total)

        logging.info("%.4s%% (%s/%s) %s", percent, count, total, status)

    return


def monitor(old_port, new_port, path):
    """ Run migration monitor.

    Parameters:
        old_port (int): old service port number.
        new_port (int): new service port number.
        path (str):     path to hosts file.

    Returns:
        None
    """

    migration_status = {}

    # read hosts
    with open(path) as f:
        hosts = f.readlines()

    start = time.time()
    average_duration = 0.0

    # get migration status
    for index, host in enumerate(hosts):
        iteration_start = time.time()

        status = get_migration_status(host, old_port, new_port)
        migration_status[host] = status

        # update average duration
        iteration_end = time.time()
        iteration_duration = iteration_end - iteration_start
        average_duration = (average_duration + iteration_duration) / 2

        # calculate progress
        progress(index, hosts, average_duration)

    # calculate duration
    end = time.time()
    duration = end - start

    # create output
    output(migration_status)

    # summary
    summary(migration_status, duration)

    return
