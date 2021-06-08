import sys
import subprocess
from behave.__main__ import main as behave_main

def main():
    print(f"Arguments count: {len(sys.argv)}")
    args=sys.argv
    # for f in sys.argv:
    #     print(f.index+" "+f)
    behave_main("features/sprint1" )

if __name__ == "__main__":
    main()