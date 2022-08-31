#get from https://stackoverflow.com/questions/54785152/replace-tab-with-space-in-entire-text-file-python/54785524
inputFile = open('Tab_replace_test_file.py', 'r') 
exportFile = open('Tab_replace_test_file_copy.py', 'w')
for line in inputFile:
   new_line = line.replace('\t', '    ')
   exportFile.write(new_line) 

inputFile.close()
exportFile.close()