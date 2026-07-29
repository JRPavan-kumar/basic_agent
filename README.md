# Student Agent Project

## Overview

This project is a simple Python example that shows how a basic agent-like workflow can be built using separate classes. It demonstrates how to:

- store sample student data,
- fetch a student by ID,
- evaluate marks and assign a grade,
- print a student report,
- handle errors gracefully.

## What the program does

When you run the script, it performs the following steps:

1. Looks up a student from the sample database.
2. Checks whether the student's information is complete.
3. Calculates the grade based on the marks.
4. Prints the student report.
5. If the student is missing or the tool name is invalid, it shows an error message.

## Project files

- [agent_file.py](agent_file.py): contains the main logic and classes.
- [test_agent.py](test_agent.py): contains unit tests for the project.

## Main components

- `STUDENT_DATABASE`: stores sample student records.
- `StudentAgent`: retrieves a student by ID.
- `EvaluationAgent`: converts marks into a grade.
- `OutputAgent`: displays the report.
- `ToolManager`: validates the requested tool.
- `run_agent()`: connects the workflow together.

## How to run the program

1. Open a terminal in the project folder.
2. Run the following command:

```powershell
python agent_file.py
```

If `python` does not work, try:

```powershell
py agent_file.py
```

## What you should expect

The program will show:

- a successful report for a valid student such as `S101`,
- an error for incomplete student data,
- an error for an invalid tool such as `AttendanceAgent`.

## How to test the project

Run the unit tests with:

```powershell
python -m unittest -v
```

This checks whether the code behaves correctly for valid and invalid cases.

## Procedure to understand the flow

1. Start with the student database.
2. Use `StudentAgent` to fetch the student.
3. Send the student details to `EvaluationAgent` to get the grade.
4. Use `OutputAgent` to print the final result.
5. If any issue occurs, `run_agent()` catches it and prints an error.

## Tips

- Make sure your terminal is inside the project folder before running the commands.
- If you get a folder error, check the current directory with:

```powershell
pwd
```

- If needed, change to the project folder first:

```powershell
cd "c:\Users\RSMDH-LPT-GEN-21\Downloads\Week1_2_GPT_assignment\Week1&2-GPT-assignment"
```

## Learning purpose

This project is intended to help beginners understand:

- simple class-based design,
- basic error handling,
- how small agent-like components can work together,
- how to test Python code with `unittest`.
