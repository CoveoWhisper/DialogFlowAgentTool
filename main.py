import argparse
from dialogflow_service import DialogFlowService

parser = argparse.ArgumentParser()
parser.add_argument("--action", help="Action to perform. Possible values are : import, export or restore\nNOTE: the argument --file should be used with import.")
parser.add_argument("--file", help="Zip containing the agent to import")
args = parser.parse_args()

dialogflowservice = DialogFlowService()

if args.action == "import":
    if args.file:
        file = args.file
        dialogflowservice.importAgent(file)
    else:
        print("Parameter --file [agent zip file] need to be used with the import action.\nUse main -h for more details.")
	
if args.action == "export":
    dialogflowservice.exportAgent()
	
if args.action == "restore":
    if args.file:
        file = args.file
        dialogflowservice.restoreAgent(file)
    else:
        print("Parameter --file [agent zip file] need to be used with the import action.\nUse main -h for more details.")
	
if not args.action and not args.file:
    print(parser.print_help())
    parser.exit(1)