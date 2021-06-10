import sys
import subprocess
from behave.__main__ import main as behave_main
from . import utils
import os



def run_scenario(scenario):
    config= utils.read_yaml()
    report_folder=config.get('execution').get('report_folder')
    report_format=config.get('execution').get('report_format')
    #print(report_folder,report_format)
    command = f"behave -f {report_format} -o {report_folder} -n '{scenario}'"
    print(command)
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

def main():
    
    print(f"Arguments : {(sys.argv)}")
    exmod=sys.argv[1]
    if (len(sys.argv)==2 and (exmod == 's')):
        print('Please enter the scenario name as the second parameter')
        


    
    elif len(sys.argv)>2 :
        run_scenario(sys.argv[2])
    
    # for f in sys.argv:
    #     print(f.index+" "+f)
    #behave_main("features/sprint1" )

if __name__ == "__main__":
    main()