# parser script v1

from resume_parser import resumeparse
import pandas as pd
from os import walk
#directory info
output_file='outputs/parsedData.xls'
resume_dir='resume_here'
log_file='logs/log.txt'
logmsg=[]

print('\n\n!-----------------------Parsing data!---------------------------!!\n\n')
#list to store file names in resumes folder
f = []
for (dirpath, dirnames, filenames) in walk('resume_here'):
    f.extend(filenames)
    break;
print("Input files: ")
print(f)
print('\n')
    
#data gathering
datalist=[]
failure_count=0
for filename in f:
    fpth =   "resume_here/"+filename
    print('Parsing: '+fpth)
    try:
        data = resumeparse.read_file(fpth)
        data['filename']=fpth
        datalist.append(data);
        msg='-->Successfully Parsed: '+fpth+'\n'
        print(msg)
        logmsg.append(msg)
    except:
        msg='\n!!>Error: Resume parsing failed for:' + fpth + '\n'
        print(msg)
        logmsg.append(msg)
        failure_count=failure_count+1

failed_msg='Failure count:' +   str(failure_count) 
logmsg.append(failed_msg)
print("\n\nFailure count: "+   str(failure_count) )

#parsing data for excel gen
df = pd.DataFrame(datalist)
df.to_excel(output_file)


# write logs
with open(log_file, 'w+') as filehandle:
    for msg in logmsg:
        filehandle.write('%s\n' % msg)

print('\n Plese find the output Excel file in: ' + output_file )

print('\n\n!-----------------------completed!---------------------------!!')