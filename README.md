# Unix-Shell
  Implemented following things
1- implemented 4 of the external commands.
2- This is a mini terminal, which executes 4 commands and 4 switches in each of the commands.

1- wc:
		print newline, word, and byte counts for each file. The options below may be used to select which counts are printed
    -c  print the byte counts
    -l  print the newline counts
    -w  print the word counts
2- grep:
		print lines matching a pattern. The options below may be used to match pattern
    -i  Ignore case distinctions, so that characters that differ only in case match each other
    -v  Invert the sense of matching, to select non-matching lines
    -x  Select  only  those  matches  that  exactly match the whole line
    -c  Suppress normal output; instead print a count of matching lines for each input file.
3- head:
		output the first part of files. The options below may be used alone or with combinations
    -c  print the first NUM bytes of each file; with the leading '-', print all but the last NUM bytes of each file
    -n  print the first NUM lines instead of the first 10; with the leading '-', print all but the last NUM lines of each file.
    -q  never print headers giving file names
    -v  always print headers giving file names
4- tail:
		output the last part of files. The options below may be used alone or with combinations
    -c  output the last NUM bytes; or use -c +NUM to output starting with byte NUM of each file.
    -n  output the last NUM lines, instead of the last 10; or use -n +NUM to output starting with line NUM.
    -q  never print headers giving file names.
    -v  always print headers giving file names.
5- cd:
		change path of the directory you are currently working in.
