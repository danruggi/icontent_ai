import argparse
import sys
import os
import json

def menu():

    conf = {}

    formatter = lambda prog: argparse.HelpFormatter(prog,max_help_position=52)
    parser = argparse.ArgumentParser(description="###### AI CONTENT CREATOR ######", prog='PROG', formatter_class=formatter)

    ### optionals
    group_commons = parser.add_argument_group("[parse/crawl] Common Argumental Options")
    group_commons.add_argument('-pools', type=int, default=1, help="[CRAWL/PARSE] CPU number")

    group_commons.add_argument('-file', type=str, default="", help="[CRAWL] Input CSV File")
    group_commons.add_argument('-one', type=str, default="", help="[CRAWL] Input Just One Domain to Scrape")
    
    subparser = parser.add_subparsers(dest='command', title='Available commands')
    
    crawl_parser = subparser.add_parser('crawl', help="[crawl] Get landings, robots, sitemaps and all internal urls");
    
    # parse_parser = subparser.add_parser('parse', help="[spider] All Parsing");
    subparser.add_parser('parse-conn', help="Parse connection metadata to output/*csv")
    subparser.add_parser('parse-json', help="Parse all application/jsons to output/*csv")
    subparser.add_parser('parse-emails', help="Extract all emails address out output/email.csv")

    cparse_parsers = subparser.add_parser('parse-custom', help="[spider] All Custom Parsing Modules");
    cparse_subparsers = cparse_parsers.add_subparsers(dest='command_custom', title='Available commands')

    path = sys.path[0]
    custom_parsers =  os.scandir(os.path.join(path, 'pools', 'parser_custom'));
    custom_parsers_dict = dict()
    for cp in custom_parsers:
        try:
            with open(os.path.join(cp.path, 'settings.json')) as fp:
                tc = json.load(fp)
            cparse_subparsers.add_parser(tc['command'], help=tc['help'])
        except Exception as e:
            print("Custom Parser error", cp.name, e)

    args = parser.parse_args()

    if args.command is None:
        print("ERROR: Please specify a command; \n\n\t ./ispider --help for help\n")
        sys.exit()
    if args.command == 'parse-custom' and args.command_custom is None:
        print("ERROR: Please specify a CUSTOM command; \n\n\t ./ispider parse-custom --help for help, to show all valid modules\n")
        sys.exit()

    conf['POOLS']=args.pools;

    conf['FILE']=args.file;
    conf['ONE']=args.one;

    conf['METHOD'] = args.command;
    conf['METHOD_CUSTOM'] = None;
    try:
        conf['METHOD_CUSTOM'] = args.command_custom;
    except:
        pass
    return conf
