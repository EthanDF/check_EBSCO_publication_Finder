# check_EBSCO_publication_Finder

script that will take in a CSV file of:

ISSN or Publication Title, vendor name, Coverage Start Date, Coverage End Date

Then will search on FAU's Publication Finder to try to verify the existance of the result.

At this point, it only verifies that any result is find. If no Result is found the results will be "TRUE" in the 2nd column.

Requires:
* csv
* time
* codecs
* selenium 
* chrome driver
