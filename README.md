# Firmus Generator

# Table of contents  
1. [Introduction](#introduction) 
2. [Environment Setup](#environment-setup)  
3. [Test](#test)  
3. [Run Locally](#run-locally)  

# Introduction
The marching doubler generator is a Python project that produces a numeric pattern called the marching doubler series. This mathematical series is generated based on two key parameters:

**Run length - The length of each individual run of numbers**

**Total terms - The total number of terms to generate**

Given these two inputs, the project will generate a marching doubler series step-by-step using a generator function. Each element of the series is yielded incrementally.

The core logic lies in the MarchingDoubler class which encapsulates the generation algorithm. The generate_pattern() method yields each term in a lazy fashion.

The main.py script provides a command line interface to generate a series and save it to a file. The OutputManager handles writing the output.

Key features:

- Generates marching doubler series based on run length and total terms
- Lazy generation using Python generators
- Command line interface for easy use
- Output writing to file
- Parameterized tests with Pytest
- Setup instructions for dependencies and virtual env
- The project provides a simple yet extensible implementation to generate marching doubler series on demand. It can serve as a reference and learning resource for mathematical series generation, generators, testing, and command line tools in Python.

## Environment Setup
Clone the project  

~~~bash  
  git clone https://github.com/b1139/Firmus-Generator.git
~~~

Go to the project directory  

~~~bash  
  cd Firmus-Generator
~~~

Setup Python Virtual Environment

It is recommended to use a virtual environment to isolate dependencies.

- To create a virtual environment:

    ```
    python3 -m venv venv
    ```

- Activate the virtual environment:

    ```    
    source venv/bin/activate
    ```

- Requirements are listed in [requirements.txt](VALID_FILE). To install them:

    ```
    pip install -r requirements.txt
    ```

# Test
Tests are located under the `tests` directory and can be run using:

```
pytest test/*
```
> **NOTE:** You should not see any red flags or failure messages when executing test

## Run Locally

The main entry point is [main.py] under project root directory.

To generate a marching doubler series:

Run Length = 4, Total Terms = 16, Output File = output.txt. Below is how to pass command line arguments.

```
python main.py 4 16 output.txt
```

This will generate a series of 16 terms with run length 4 and save to `output.txt`.

Execute ```python main.py --help``` to get to know more options.


**Have a great `pythonic` day**

