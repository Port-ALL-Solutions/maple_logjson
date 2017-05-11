import json
import re
import sys

ansi_escape = re.compile(r'\x1b[^m]*m')
lastinfo = ""
data = []
error = False
errlog = open("err.log", "w")
newlog = open("clean.log", "w")




with open(sys.argv[1]) as json_file:  
    for line in json_file:
        logline = json.loads(line)['log']
        if logline[:4] == '2017':
            logline = ansi_escape.sub('', logline)[26:]
        newlog.write(logline)
        if logline[:4] != 'INFO':
            if lastinfo:
                errlog.write("===================================================================================\r\n")
                errlog.write(lastinfo)
                lastinfo = False
            errlog.write(logline)
            error = True
        else:
            if error:
                errlog.write(logline)
                errlog.write("===================================================================================\r\n")
            lastinfo = logline
            error = False
            
errlog.close()
newlog.close()