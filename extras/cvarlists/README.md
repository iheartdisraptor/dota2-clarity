This folder contains a history of cvarlists (console variables). This is useful
to detect when Valve adds new and useful console commands. This is how it works:

Every major patch, generate a new list of all the console variables using:

    cvarlist log cvarlist-log.txt

Use a diff program to generate the changes from one patch to another. Online
diff programs are available, e.g. http://www.diffchecker.com.
