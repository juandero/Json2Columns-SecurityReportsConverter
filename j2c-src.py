import argparse
import sys
import textwrap
from pathlib import Path

# from src import 

def InitArgParser():
    """
        Initialization of the arguments parser
    """
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description=textwrap.dedent(
                                     """\
                                     Json2Columns - Security Reports Converter
                                     -----------------------------------------
                                     Just a CLI application to convert the json format output reports of different security tools.
                                     Currently with support the convertion to CSV and XLSX formats.
                                     """))
    parser.add_argument('app_name', help='Name of the Sec Tool that generated the original json report.', choices=['safety', 'bandit'])
    parser.add_argument('-f', '--format', help='Format to which to convert the original report.', choices=['csv', 'xls'], required=True)
    parser.add_argument('path_report', help='Path of the original json report to convert.')
    return parser

def FileValidation(path_report):
    fpath = Path(path_report)
    
    if not fpath.exists():
        print(f"The file {path_report} does not exists.")
        print("Please enter a valid path to the json report that will be converted.")
        sys.exit(1)

    if not fpath.is_file():
        print(f"The path entered {path_report} does not consist of a valid file.")
        print("Please enter a valid path to the json report that will be converted.")
        sys.exit(1)

def FormatConverter(app_name,format,path_report):
    
    print('Name of the sec tool used to generate the original report:', app_name)
    print('Format to which to convert:', format)
    print('Path location of the original report:', path_report)

    return

def main():
    
    parser = InitArgParser()
    args = parser.parse_args()

    FileValidation(args.path_report)
    FormatConverter(args.app_name,args.format,args.path_report)

if __name__ == "__main__":
    main()