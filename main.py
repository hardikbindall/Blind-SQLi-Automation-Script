import argparse
from modules.scanner import scan_for_vuln
from modules.extractor import extract_data
from modules.secure_advisor import give_recommendations
from result_writer import write_result

def main():
    parser = argparse.ArgumentParser(description="Blind SQLi Automation Tool")
    subparsers = parser.add_subparsers(dest="command")

    scan_parser = subparsers.add_parser("scan")
    scan_parser.add_argument("url", help="Target URL to scan")

    extract_parser = subparsers.add_parser("extract")
    extract_parser.add_argument("url", help="Target vulnerable URL")

    secure_parser = subparsers.add_parser("secure")
    secure_parser.add_argument("url", help="Target URL to analyze for securing")

    args = parser.parse_args()

    if args.command == "scan":
        result = scan_for_vuln(args.url)
        write_result("Scan Results", result)

    elif args.command == "extract":
        result = extract_data(args.url)
        write_result("Extracted Data", result)

    elif args.command == "secure":
        result = give_recommendations(args.url)
        write_result("Security Recommendations", result)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()