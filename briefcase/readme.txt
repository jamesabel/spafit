
- currently this is just for Mac (OSX), since pynsist seems to be working for this test case.  We could add
  Windows test of briefcase later if desired.

- I got this error:

  10/23/16 2:16:26.959 PM com.apple.xpc.launchd[1]: (org.example.main.358432[73977]) Service exited with abnormal code: 1

  So have have to run like this to see the error actual error:

  ./macOS/main.app/Contents/MacOS/main > main.log 2>&1
