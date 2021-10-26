# Copyright (c) 2021 University of Illinois, Urbana-Champaign
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import datetime
import logging
import os
import sys

sys.path = ['./', '../'] + sys.path
from GenConfigs import *
sys.path = [FAAS_ROOT + '/synthetic_workload_invoker'] + sys.path
from commons.Logger import ScriptLogger

logger_wlch = ScriptLogger('workload_checker', 'SWI.log')

"""
Check whether the loaded workload config is valid
"""
def CheckWorkloadValidity(workload, supported_distributions):
    logger_wlch.info("Started CheckWorkloadValidity")
    # 1 - check if the workload has been successfully read in ReadJSONConfig
    if workload is None:
        logger_wlch.info('Workload not valid => Terminating')
        return False
    
    # 2 - check for validity of general field
    print('Workload config:\n', workload)
    fields_to_check = [['test_name', str], ['blocking_cli', bool]]
    for field in fields_to_check:
        try:
            # print(field, workload[field[0]])
            if type(workload[field[0]]) is not field[1]:
                test_name('Input of ' + field[0] + ' field should be a ' + str(field[1]))
                return False
        except:
            logger_wlch.error('No ' + field[0] + ' field provided!')
            return False
    
    # 3 - check if invocation scripts exists for all functions/applications in the workload
    application_set = set()
    distribution_set = set()
    for (instance, specs) in workload['instances'].items():
        application_set.add(specs['application'])
        try:
            distribution_set.add(specs['distribution'])
        except:
            pass

    logger_wlch.info('Required applications: ' + str(application_set))
    # all_scripts_available = True

    # for application in application_set:
    #     if not os.path.isfile(FAAS_ROOT + '/invocation-scripts/'+application+'.sh'):
    #         logger_wlch.error(
    #             'No invocation script available in invocation-scripts for the following application: '+application)
    #         all_scripts_available = False

    # if not all_scripts_available:
    #     logger_wlch.info('Incomplete invocation scripts => Terminating')
    #     return False
    # else:
    #     logger_wlch.info('Script files for all applications exist')
    
    # 4 - check for supported distributions
    if not distribution_set.issubset(supported_distributions):
        logger_wlch.error('At least one specified distribution is not supported. Supported distribution(s): '+str(supported_distributions))
        return False
    # 5 - check for valid test duration
    try:
        test_duration_in_seconds = workload['test_duration_in_seconds']
        if test_duration_in_seconds is None:
            logger_wlch.error('Please enter a valid value for test_duration_in_seconds field in the config file.')
            return False
        elif int(test_duration_in_seconds) <= 0:
            logger_wlch.error('test_duration_in_seconds should be greater than zero!')
            return False
    except:
        logger_wlch.error('test_duration_in_seconds field not specified in the json config file')
        return False
    
    # 6 - check that the random_seed field is entered
    try:
        random_seed = workload['random_seed']
    except:
        logger_wlch.error("No random_seed field specified in the config file")
        return False

    return True
