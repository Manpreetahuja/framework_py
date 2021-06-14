import sys
import os
import subprocess
from behave.__main__ import main as behave_main
from . import utils

from behave import runner_util as ru



def run_scenario(scenario):
    config= utils.read_yaml()
    report_folder=config.get('execution').get('report_folder')
    report_format=config.get('execution').get('report_format')
   
    command = f"{os.getcwd()}/features/sprint1 -f {report_format} -o {report_folder} -n {scenario}"
    print(command)
    behave_main(command)

def run_tag(tag):
    config=utils.read_yaml()
    report_folder=config.get('execution').get('report_folder')
    report_format=config.get('execution').get('report_format')

    command = f"{os.getcwd()}/features/sprint1 -f {report_format} -o {report_folder} -t {tag}"
    print(command)
    behave_main(command)



def runtest(args):
    try:
        print(f"Arguments : {(args)}")
        exmod=args[1]
        print("twinkle", args)
        if (len(args)==2 and (exmod == 's')):
            print('Please enter the scenario name as the second parameter')
       
        elif len(args)>2 and exmod=='s':
            scenario=args[2]
            print("scenariomanpreet")
            run_scenario(scenario)
        
        elif len(args)>2 and exmod=='t':
            tag=args[2]
            print("djwalebabu", tag )
            run_tag(tag)
    except:
        print("Error occured by running this suite")




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