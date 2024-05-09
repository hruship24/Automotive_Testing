import argparse
import subprocess


def run_tests(report_type):
    if report_type == 'html':
        subprocess.run(['pytest',' --html=claim_process_system_report.html'])
        print("file html")
    elif report_type == 'verbose':
        subprocess.run(['pytest', '-v'])
    else:
        subprocess.run(['pytest'])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process insurance claim system reports.')
    parser.add_argument('--html-report', action='store_true', help='Generate HTML report')
    parser.add_argument('--verbose', action='store_true', help='Run tests in verbose mode')

    args = parser.parse_args()

    if args.html_report:
        run_tests('html')
    elif args.verbose:
        run_tests('verbose')
    else:
        run_tests(None)
