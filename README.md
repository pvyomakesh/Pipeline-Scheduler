# Pipeline Scheduler Project
## Project Overview
This Python-based project simulates a pipeline scheduler for a 5-stage FDEMW scalar processor. It's aimed at understanding and implementing programmatic scheduling of instruction sets, typically performed manually or in hardware description languages.

## Features
* Simulates instruction scheduling on a 5-stage scalar pipeline.
* Processes various instruction types, including R, I, L, and S, with potential forwarding paths.
* Uses test data for debugging and validation purposes.
## Getting Started
### Prerequisites
* Python (version specified in the makefile)
* GNU Make
### Running the Program
To run the project:

1. Copy Test Data: Place your test data into the test.in file.
2. Build and Execute: Run the command:
make test\
This will execute the program using test.in as input and produce an out.txt file with the output.

## Test and Debugging
The project includes a set of test input files and their corresponding expected output files:

### Input Files
Located in the [Test Inputs Files](Test_Input_Files) folder:

seq0.txt
seq1.txt
seq2.txt
... and so on.
Output Files
Located in the test_outputs folder:

seq0.out.txt
seq1.out.txt
seq2.out.txt
... and so on.
These files contain the expected results for each corresponding input file.
