## SPAFIT - Small Python Application Freezer/Installer Test ##
| Tool | Win | Mac | Issue |
|------|-----|-----|-------|
| briefcase | :no_entry_sign: Not Supported | :x: FAIL | https://github.com/jamesabel/spafit/blob/master/test_briefcase_mac/briefcase_mac_1_error.log<br>https://github.com/jamesabel/spafit/blob/master/test_briefcase_mac/briefcase_mac_2_error.log |
| cx_freeze | :x: FAIL | :x: FAIL | https://github.com/jamesabel/spafit/blob/master/test_cx_freeze_win/cx_freeze_win_1_error.log<br>https://github.com/jamesabel/spafit/blob/master/test_cx_freeze_win/cx_freeze_win_2_error.log<br>https://github.com/jamesabel/spafit/blob/master/test_cx_freeze_mac/cx_freeze_mac_1_error.log |
| osnap | :white_check_mark: PASS | :white_check_mark: PASS |  |
| py2app | :no_entry_sign: Not Supported | :x: FAIL | https://github.com/jamesabel/spafit/blob/master/test_py2app_mac/py2app_1_error.log<br>https://github.com/jamesabel/spafit/blob/master/test_py2app_mac/py2app_mac_1_error.log |
| py2exe | :x: FAIL | :no_entry_sign: Not Supported | https://github.com/jamesabel/spafit/blob/master/test_py2exe_win/py2exe_1_error.log<br>https://github.com/jamesabel/spafit/blob/master/test_py2exe_win/py2exe_2_error.log |
| pyinstaller | :x: FAIL | :x: FAIL | https://github.com/jamesabel/spafit/blob/master/test_pyinstaller_win/pyinstaller_win_1_error.log<br>https://github.com/jamesabel/spafit/blob/master/test_pyinstaller_win/pyinstaller_win_2_error.log<br>https://github.com/jamesabel/spafit/blob/master/test_pyinstaller_mac/pyinstaller_mac_1_error.log |
| pynsist | :white_check_mark: PASS | :no_entry_sign: Not Supported |  |

Notes
- Generally tried to use Python 3.5.  If a tool failed with 3.5 I tried 3.4.  However, no tool that failed on 3.5 then passed on 3.4.
    
