
import os
import shutil

python_path = '/usr/bin/python'

# backup the original python
shutil.copyfile(python_path, python_path + '.bak')

# create the new python script to block the usage
with open(python_path, 'w') as f:
    f.write('#!/usr/bin/env python\n')
    f.write('import os\n')
    f.write('if "VIRTUAL_ENV" in os.environ:\n')
    f.write('    os.execl(os.environ["VIRTUAL_ENV"] + "/bin/python", *sys.argv)\n')
    f.write('else:\n')
    f.write('    print "ERROR: You must use a virtual environment to run python!"\n')
    f.write('    sys.exit(1)\n')

# set execute permission
os.chmod(python_path, 0755)
