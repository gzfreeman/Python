# Script Name		: script_listing.py
# Author				: Craig Richards
# Created				: 15th February 2012
# Last Modified		: 29th May 2012
# Version				: 1.2


import os

logdir = os.getenv("logs")
logfile = 'script_list.log'
path = os.getenv("scripts")
#path = (raw_input("Enter dir: "))										  # Ask the user for the directory to scan
logfilename = os.path.join(logdir, logfile)					  	# Set the variable logfilename by joining logdir and logfile together
log = open(logfilename, 'w')												    # Set the variable log and open the logfile for writing

for dirpath, dirname, filenames in os.walk(path):				# Go through the directories and the subdirectories
  for filename in filenames:											    	# Get all the filenames
    log.write(os.path.join(dirpath, filename)+'\n')					# Write the full path out to the logfile

print ("\nYour logfile " , logfilename, "has been created")		# Small message informing the user the file has been created
