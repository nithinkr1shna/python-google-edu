#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

#recursive


#--------------------------------------------------------------
#-------------- file path manipulation-------------------------

def all_files_in_dir(directory):
	files = []
	for dirpath, dirnames, filenames in os.walk(directory):
		files.extend(filenames)
		#break
	return files

def search_for_special_file(special_pattern, files):
	special_files = []
	for file in files:
		if special_pattern in file:
			special_files.append(file)
	return special_files

def special_files(args):
	abs_path = os.getcwd()
	file = search_for_special_file(args[0], all_files_in_dir(args[1]))
	for i in file:
		print abs_path+"/"+i


#--------------------------------------------------------------
#---------------File copying-----------------------------------

def copy_to(src, dest):
	os.makedirs(dest)
	if src[0] == '.':
		for dirpath, dirnames, files in os.walk(src[0]):
			print files, dest, os.getcwd()
			shutil.copy(os.getcwd()+"/"+files, os.getcwd()+"/"+dest)
			break
		
	else:
		for files in os.listdir(src[0]):
			print files, dest, os.getcwd()
			shutil.copy(os.getcwd()+"/"+src[0]+"/"+files, os.getcwd()+"/"+dest)


#---------------------------------------------------------------
#---------------- To zip ---------------------------------------
def to_zip(src , to):
	if src == '.':
		all_files =""
		for x, y, filenames in os.walk(os.getcwd()):
			files = filenames
		for file in files:
			all_files+=" "+file+" "
		print all_files
		result = commands.getoutput('zip {} {}'.format(to,all_files))
	else:
		result = commands.getoutput('zip {} {}'.format(to,src))
	return result



def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
 
  args = sys.argv[1:]
  if not args:
    print "usage:[dir \"specialchar\"][--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  tozip = ''
  if args[0] == '--todir':
    todir = args[1]
    print todir
    del args[0:2]
    src = args
    copy_to(src, todir)

  elif args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]
    print tozip, args
    print to_zip(args[0],tozip)
    #zip file action

  elif len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)
  else:
  	if len(args) >= 2:
  		args = sys.argv[1:]
  		special_files(args)
  	else:
  		print "usage:[dir \"specialchar\"][--todir dir][--tozip zipfile] dir [dir ...]";
  		sys.exit(1)


  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
