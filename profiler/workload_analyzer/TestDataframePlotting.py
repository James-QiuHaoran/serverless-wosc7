# Copyright (c) 2021 University of Illinois, Urbana-Champaign
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from datetime import timedelta
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sys

sys.path = ['./', '../'] + sys.path

from GenConfigs import *


"""
Plot the test dataframe data
"""
def TestDataframePlotter(save_plot, test_df, test_name='example_test', cgroups_df=None, perf_mon_records=None):
    fig, ax = plt.subplots(nrows=1, ncols=1)
    dims = {
        's': 'start',
        'd': 'duration',
        'wt': 'waitTime',
        'it': 'initTime',
        'l': 'latency'
    }

    test_df['start'] = test_df['start'].div(1000).round(2)
    print(test_df)

    color_palette = sns.color_palette('Set1')
    test_df.plot(kind='scatter', x=dims['s'], y=dims['d'],
                 c=[color_palette[0]], alpha=0.5, ax=ax, label='Run Time', marker='*')
    test_df.plot(kind='scatter', x=dims['s'], y=dims['it'],
                 c=[color_palette[1]], alpha=0.5, ax=ax, label='Initiation Time', marker='^')
    test_df.plot(kind='scatter', x=dims['s'], y=dims['wt'],
                 c=[color_palette[2]], alpha=0.5, ax=ax, label='Wait Time', marker='v')
    test_df.plot(kind='scatter', x=dims['s'], y=dims['l'],
                 c=[color_palette[3]], alpha=0.5, ax=ax, label='Total Latency', marker='o')
    ax.set_xlabel('Invocation Time (s)')
    ax.set_ylabel('Time (ms)')
    
    color_palette = sns.color_palette('Paired')

    if save_plot:
        plt.savefig(FAAS_ROOT + '/experiments/' + test_name + '.png') 
    else:
        plt.show()

    plt.close()

    return True

"""
Plot the performance monitoring records
"""
def PerfMonPlotter(perf_mon_records, time_window = None):
    # for all records, ignoring the time_window
    pqos_records = perf_mon_records['pqos_records']

    palette = sns.color_palette("rocket_r", 16)
    
    # 'timestamp','Core','IPC','LLC Misses','LLC Util (KB)','MBL (MB/s)'
    fig, axs = plt.subplots(ncols=2, nrows=2, sharex=True)
    pqos_records_sum = pqos_records.groupby('timestamp').sum()
    pqos_records_sum.plot(y='IPC', ax=axs[0][0])
    pqos_records_sum.plot(y='MBL (MB/s)', ax=axs[0][1])
    pqos_records_sum.plot(y='LLC Util (KB)', ax=axs[1][0])
    pqos_records_sum.plot(y='LLC Misses', ax=axs[1][1])
    axs[0][0].set_ylim([0,20])

    plt.show()
    plt.close()

    return True
