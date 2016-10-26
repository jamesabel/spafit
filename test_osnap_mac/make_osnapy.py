
# this has to be separate so we can execute it as sudo

import sys

sys.path.insert(0,'..')
import spafit.osnap_test_util as osnap_test_util

osnap_test_util.make_osnapy(True)

