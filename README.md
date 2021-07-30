# MAZE SOLVER
## Project Description  :
### This project gives the shortest path from the start point of a maze to end point using backtracking algorithm
## Target :
### To write the shortest path in to a file
## Technologies Used :
### Python 3.8
## Dependencies :
### In this project we need to import sys libraray to as this is a command line tool. Using this library we can store and apply functions or manipulate the command line arguments
### The arguments that are accepted in this project are 
### -i inputfilename
### -i outputfilename
## Work Flow :
### Fisrt the user have to create two files like input file and output file. Insert the square for which you have to find the shortest path in the input file, and the output file should be empty. Then run the program using
```bash
python mazesolver.py -i inputfilename -o outputfilename

ex: python mazesolver.py -i inputfile.txt -o outputfile.txt
```
### After running this command automatically the shortest path from the start point of the maze to end point of the maze is written in to the output file. If there is no such shortest path for the maze which the user have given then this program will write "-1" to the output file
## Output :
![image](https://github.com/attainu/python-project-munnuru-srinath-au16/blob/dev/Screenshots/Screenshot%20(155).png)