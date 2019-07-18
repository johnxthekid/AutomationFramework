--timestampoutputs
# --rerunfailed     .\report\output\output.xml
--outputdir  .\report\output\run1
--loglevel  trace

--variable  BROWSER:chrome

# --include     run_tags
# --exclude     run_tags

 --suite  browser

#pabot --verbose -A .\config\test_arg.robot test
#pabot --verbose -A .\config\run_arguments.robot test
#pabot --verbose --argumentfile1 .\config\test_arg.robot --argumentfile2 .\config\run_arguments.robot test
#pabot --pabotlib --verbose --resourcefile .\config\value_set.dat test\browser
