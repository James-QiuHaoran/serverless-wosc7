# Copyright (c) 2021 University of Illinois, Urbana-Champaign
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import json
import os
import sys

sys.path = ['./', '../'] + sys.path
from GenConfigs import *

"""
Check whether the provided json file is correct
"""
def CheckJSONConfig(json_file):
    if json_file is None:
        return False
    if not os.path.isfile(json_file):
        return False
    return True

"""
Read the json config file and return a dictionary object
"""
def ReadJSONConfig(json_file):
    workload = None
    try:
        with open(json_file) as f:
            workload = json.load(f)
    except:
        print("The JSON config file cannot be read")

    return workload

"""
Writes the workload config to a json file
"""
def WriteJSONConfig(workload, json_file):
    with open(FAAS_ROOT + '/' + json_file, 'w') as outfile:
        json.dump(workload, outfile)
