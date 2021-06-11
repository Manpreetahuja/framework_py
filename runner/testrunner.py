import sys
import subprocess
from behave.__main__ import main as behave_main
from . import utils
import os
from behave import runner_util as ru



def run_scenario(scenario):
    config= utils.read_yaml()
    report_folder=config.get('execution').get('report_folder')
    report_format=config.get('execution').get('report_format')
   
    command = f"{os.getcwd()}/features/sprint1 -f {report_format} -o {report_folder} -n '{scenario}'"
    print(command)
    behave_main(command)


def runtest(args):
    print(f"Arguments : {(args)}")
    exmod=args[1]
    if (len(args)==2 and (exmod == 's')):
        print('Please enter the scenario name as the second parameter')
        


    
    elif len(args)>2 :
        run_scenario(args[2])


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