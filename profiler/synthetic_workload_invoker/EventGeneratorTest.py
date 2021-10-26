# Copyright (c) 2021 University of Illinois, Urbana-Champaign
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import sys

sys.path = ['./', '../'] + sys.path
from GenConfigs import *
sys.path = [FAAS_ROOT + '/synthetic_workload_invoker'] + sys.path
from EventGenerator import GenericEventGenerator
from commons.JSONConfigHelper import ReadJSONConfig
from WorkloadChecker import CheckWorkloadValidity

# global variables
supported_distributions = {'Poisson', 'Uniform'}

def main():
    # config_path = '/home/haoranq4/hqiu-owk/extended-faas-profiler/workload_configs.json'
    config_path = '/home/haoranq4/hqiu-owk/extended-faas-profiler/workload_configs_template.json'
    workload = ReadJSONConfig(config_path)
    print('[DEBUG] JSON file loaded')
    
    # abort the function if the json file not valid
    if not CheckWorkloadValidity(workload=workload, supported_distributions=supported_distributions):
        print('Workload configuration not valide! Test failed!')
        exit()
    print('[DEBUG] JSON file validated')

    [all_events, event_count] = GenericEventGenerator(workload)
    print('All events:', all_events)
    print('Total # of events:', event_count)

if __name__ == "__main__":
    main()
