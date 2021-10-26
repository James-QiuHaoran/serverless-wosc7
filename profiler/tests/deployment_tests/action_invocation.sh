# Copyright (c) 2021 Princeton University
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

# This script reads the WSK_PATH from the GenConfigs.py in the root directory.
# Make sure that it is correctly set before running this test.  
WSK_PATH=$(grep -r "WSK_PATH" ../../GenConfigs.py | cut -d' ' -f 3)
WSK_PATH=${WSK_PATH:1:-1}

echo '### ACTION INVOCATION TEST ###'

TEST_STATUS='PASS'

# check that those actions are created
if $WSK_PATH action invoke base64_nodejs -i -r | grep 's_decode';
then echo '>> base64_nodejs successfully created';
else echo '>> base64_nodejs not created'; TEST_STATUS='FAIL';
fi
if $WSK_PATH action invoke base64_python -i -r | grep 's_decode';
then echo '>> base64_python successfully created'; 
else echo '>> base64_python not created'; TEST_STATUS='FAIL';  
fi
if $WSK_PATH action invoke base64_ruby -i -r | grep 's_decode';
then echo '>> base64_ruby successfully created'; 
else echo '>> base64_ruby not created'; TEST_STATUS='FAIL';  
fi
if $WSK_PATH action invoke base64_swift -i -r | grep 's_decode';
then echo '>> base64_swift successfully created'; 
else echo '>> base64_swift not created'; TEST_STATUS='FAIL';  
fi

echo $TEST_STATUS
