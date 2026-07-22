# Hadoop Streaming Word Count using Animal Dataset

## Project Title

Animal Word Count using Hadoop Streaming (Python)

---

## Project Description

This project demonstrates the implementation of the Hadoop Streaming MapReduce framework using Python. The application counts the number of occurrences of different animal names present in an input text file. The project consists of four Python programs: Mapper, Partitioner, Reducer, and Main. The Mapper converts the input into key-value pairs, the Partitioner groups similar keys, and the Reducer calculates the total frequency of each animal.

This project helps understand the working of the MapReduce programming model in a simple and efficient manner.

---

## Objectives

- To understand the Hadoop Streaming MapReduce workflow.
- To implement Mapper, Partitioner, and Reducer using Python.
- To count the occurrences of animal names from a text file.
- To understand how intermediate data is processed and reduced.
- To simulate Hadoop Streaming using Python.

---

## Software Requirements

- Operating System: Windows 10/11
- Python Version: Python 3.x
- Visual Studio Code
- PowerShell or Command Prompt

---

## Project Structure

```
AnimalWordCount/
│
├── input.txt
├── mapper.py
├── partitioner.py
├── reducer.py
├── main.py
├── map_output.txt
├── sorted_output.txt
├── final_output.txt
└── README.md
```

---

## Input File (input.txt)

```
cat dog cat
lion tiger dog
elephant lion
dog rabbit cat
tiger elephant dog
rabbit rabbit lion
elephant dog tiger
cat lion rabbit
rabbit elephant cat
dog dog tiger
```

---

## Explanation of Files

### 1. input.txt

This file contains the input data. Each line consists of animal names separated by spaces.

Example:

```
cat dog cat
lion tiger dog
```

---

### 2. mapper.py

The Mapper reads the input file line by line. It separates each word and emits it in the form:

```
AnimalName    1
```

Example Output:

```
cat     1
dog     1
cat     1
lion    1
```

Purpose:

- Reads the input.
- Splits each line into words.
- Generates key-value pairs.

---

### 3. partitioner.py

The Partitioner receives the Mapper output and assigns records into different partitions based on the first letter of the animal name.

Example:

```
0    cat      1
0    dog      1
1    rabbit   1
1    tiger    1
```

Purpose:

- Groups similar keys.
- Simulates Hadoop partitioning.

---

### 4. reducer.py

The Reducer receives the sorted mapper output and combines all identical keys by adding their counts.

Example:

Input:

```
cat     1
cat     1
cat     1
cat     1
```

Output:

```
cat     4
```

Purpose:

- Groups identical keys.
- Calculates total frequency.
- Produces the final output.

---

### 5. main.py

The Main program executes the complete workflow.

Functions performed:

- Runs mapper.py
- Stores mapper output in map_output.txt
- Sorts mapper output
- Saves sorted output in sorted_output.txt
- Runs reducer.py
- Stores final result in final_output.txt

Terminal Output:

```
Processing Completed!
Check final_output.txt
```

---

## Workflow

```
input.txt
      │
      ▼
 mapper.py
      │
      ▼
map_output.txt
      │
      ▼
Sorting
      │
      ▼
sorted_output.txt
      │
      ▼
partitioner.py (Optional Demonstration)
      │
      ▼
reducer.py
      │
      ▼
final_output.txt
```

---

## How to Run the Project

### Step 1

Open the project folder in Visual Studio Code.

### Step 2

Open Terminal.

### Step 3

Run the following command:

```
py main.py
```

### Step 4

After execution, open:

```
final_output.txt
```

to see the result.

---

## Expected Output

```
cat         4
dog         6
elephant    4
lion        4
rabbit      5
tiger       4
```

---

## Advantages

- Easy to understand MapReduce.
- Simple implementation using Python.
- Demonstrates Hadoop Streaming concepts.
- Efficient word counting process.
- Useful for beginners learning Big Data.

---

## Applications

- Word Count Analysis
- Log File Analysis
- Text Mining
- Data Analytics
- Search Engine Indexing
- Big Data Processing

---

## Learning Outcomes

After completing this project, students will be able to:

- Understand the MapReduce architecture.
- Write Mapper, Partitioner, and Reducer programs.
- Process large text datasets.
- Execute Hadoop Streaming concepts using Python.
- Understand the complete data flow from input to output.

---

## Conclusion

This project successfully demonstrates the implementation of the Hadoop Streaming Word Count algorithm using Python. The Mapper reads animal names and converts them into key-value pairs, the Partitioner organizes similar keys, and the Reducer computes the total occurrences of each animal. The final output accurately displays the frequency of every animal in the dataset. This project provides a practical understanding of the MapReduce programming model and serves as a strong foundation for learning Big Data and Hadoop technologies.
