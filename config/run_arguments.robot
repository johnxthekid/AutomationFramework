#--timestampoutputs
# --rerunfailed     .\report\output\output.xml
--outputdir  .\report
--loglevel  trace
--variable  BROWSER:chrome
--variable  RUN_LOCATION:local

# --include     run_tags
# --exclude     run_tags

# --suite       browser
# --suite       sample_suite

#pabot --pabotlib --resourcefile .\config\value_set.dat --timestampoutputs --outputdir  .\report\parallel --loglevel trace --suite  browser --suite sample_suite test
#pabot --pabotlib --resourcefile .\config\value_set.dat -A .\config\run_arguments.robot --suite  browser --suite sample_suite test
