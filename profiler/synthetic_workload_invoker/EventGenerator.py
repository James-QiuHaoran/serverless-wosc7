# Copyright (c) 2021 University of Illinois, Urbana-Champaign
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import datetime
import logging
import numpy as np
import random
import time

from commons.Logger import ScriptLogger

logger_eg = ScriptLogger('event_generator', 'SWI.log')

"""
Creates a list of invocation inter-arrivals
""" 
def CreateEvents(instance, dist, rate, duration, seed=None):
    inter_arrivals = []
    if rate == 0:
       return inter_arrivals

    if dist == "Uniform":
        random.seed(seed)
        shift = random.random()/rate
        inter_arrivals = int(duration*rate)*[1.0/rate]
        inter_arrivals[0] += shift
    elif dist == "Poisson":
        np.random.seed(seed)
        beta = 1.0/rate
        # creating inter arrival times using an Exponential process
        # make sure longer than duration (will be cut to duration with EnforceActivityWindow)
        inter_arrivals = list(np.random.exponential(scale=beta, size=int(1.5*duration*rate)))

    return inter_arrivals

"""
Create a list of invocation inter-arrivals within [start, end]
"""
def CreateEventsWithStartEnd(instance, dist, rate, start, end, seed=None):
    duration = end - start + 1
    inter_arrivals = []

    if rate == 0:
        return inter_arrivals

    if dist == "Uniform":
        random.seed(seed)
        shift = random.random()/rate
        inter_arrivals = int(duration*rate)*[1.0/rate]
        inter_arrivals[0] += shift
    elif dist == "Poisson":
        np.random.seed(seed)
        beta = 1.0/rate
        # creating inter arrival times using an Exponential process
        inter_arrivals = list(np.random.exponential(scale=beta, size=int(duration*rate)))

    return inter_arrivals

"""
Enforce the activity window defined in the config file for the created instance events
"""
def EnforceActivityWindow(start_time, end_time, instance_events):
    events_iit = []
    events_abs = [0] + instance_events
    event_times = [sum(events_abs[:i]) for i in range(1, len(events_abs)+1)]
    event_times = [e for e in event_times if (e > start_time) and (e < end_time)]
    try:
        events_iit = [event_times[0]] + [event_times[i]-event_times[i-1] for i in range(1, len(event_times))]
    except:
        pass
    return events_iit

"""
Generate a list of invocation times for each application instance given the workload config
"""
def GenericEventGenerator(workload):
    logger_eg.info("Started generic event generator")
    test_duration_in_seconds = workload['test_duration_in_seconds']

    all_events = {}
    event_count = 0

    random_seed = workload['random_seed']
    logger_eg.info('Found random_seed from config: ' + str(random_seed))
    # use hash of the current time stamp as the random seed
    # random_seed = int(time.time())

    for (instance, desc) in workload['instances'].items():
        if 'interarrivals_list' in desc.keys():
            # inter-arrivals specified in the config
            instance_events = desc['interarrivals_list']
            logger_eg.info('Reading the invocation time trace for ' + instance)
            # enforcing maximum test duration
            list_len = 0
            cutoff_index = None
            for i in range(len(instance_events)):
                list_len += instance_events[i]
                if list_len > test_duration_in_seconds:
                    cutoff_index = i
                    break
            if cutoff_index is not None:
                instance_events = instance_events[:cutoff_index]
        else:
            # activity window and distribution specified in the config
            # instance_events = CreateEvents(instance=instance, dist=desc['distribution'], rate=desc['rate'], duration=test_duration_in_seconds, seed=random_seed)
            instance_events = CreateEventsWithStartEnd(instance=instance, dist=desc['distribution'], rate=desc['rate'], start=desc['activity_window'][0], end=desc['activity_window'][1], seed=random_seed)
            try:
                start_time = desc['activity_window'][0]
                end_time = desc['activity_window'][1]
                # instance_events = EnforceActivityWindow(start_time, end_time, instance_events)
                instance_events = [start_time] + instance_events
                event_times = [sum(instance_events[:i]) for i in range(1, len(instance_events))]
                # print('[DEBUG] event times (' + str(len(event_times)) + '):\n', event_times)
            except:
                instance_events = EnforceActivityWindow(0, workload['test_duration_in_seconds'], instance_events)
        all_events[instance] = instance_events
        event_count += len(instance_events)

    logger_eg.info("Returning workload event list")

    return [all_events, event_count]
