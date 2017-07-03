""""Write a program that takes the output from `git log` command and prints the
# # commit, Author, and Date fields for each commit as CSV."""


input_csv = """commit ecee9eea029dd33d93bed897933d2d01c8c1668b
Author: Benjy Weinberger <benjyw@gmail.com>
Date:   Mon Jun 12 14:09:23 2017 -0700

commit 663512c5a3b0a26ffcde8a78d4fe75a1f3df88ea
Author: John Sirois <john.sirois@gmail.com>
Date:   Mon Jun 12 13:39:36 2017 -0700

commit a5131b372e0442a2bfc49808a0095b91be481222
Author: Benjy Weinberger <benjyw@gmail.com>
Date:   Mon Jun 12 10:06:06 2017 -0700"""


"""
>>> read_input(input_csv)
Commit, Author, Date
ecee9eea029dd33d93bed897933d2d01c8c1668b, Benjy Weinberger <benjyw@gmail.com>, Mon Jun 12 14:09:23 2017 -0700
663512c5a3b0a26ffcde8a78d4fe75a1f3df88ea, John Sirois <john.sirois@gmail.com>, Mon Jun 12 13:39:36 2017 -0700
a5131b372e0442a2bfc49808a0095b91be481222, Benjy Weinberger <benjyw@gmail.com>, Mon Jun 12 10:06:06 2017 -0700

"""


def read_input(input_text):
    
    # each_line = []
    print "Commit, Author, Date"
    
    lines = input_csv.strip().split("\n")

    csv_lines = "" 

    for chars in lines:
        new_lines = chars.split(" ", 1) #this splits the first char off
               
        if new_lines[0] == "commit":

            csv_lines += new_lines[1].strip() + ", "

        if new_lines[0] == "Author:":

            csv_lines += new_lines[1].strip() + ", "

        if new_lines[0] == "Date:":

            csv_lines += new_lines[1].strip() + "\n"


    print csv_lines

            
            
if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!"