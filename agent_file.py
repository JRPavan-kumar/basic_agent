# -------------------------------
# Student Database (Sample Data)
# -------------------------------
STUDENT_DATABASE = {
    "S101": {"name": "Rahul", "marks": 82},
    "S102": {"name": "Priya", "marks": 91},
    "S103": {"name": "Kiran", "marks": 67},
    "S104": {"name": "Anjali", "marks": 38}
}


# -------------------------------
# Student Agent (Read-Only)
# -------------------------------
class StudentAgent:

    def get_student(self, student_id):
        if student_id not in STUDENT_DATABASE:
            raise ValueError(f"Student ID '{student_id}' not found.")

        student = STUDENT_DATABASE[student_id]

        if "name" not in student or "marks" not in student:
            raise ValueError("Student details are incomplete.")

        return student


# -------------------------------
# Evaluation Agent
# -------------------------------
class EvaluationAgent:

    def evaluate(self, student):

        marks = student["marks"]

        if marks >= 90:
            return "A+"
        elif marks >= 75:
            return "A"
        elif marks >= 60:
            return "B"
        elif marks >= 40:
            return "C"
        else:
            return "Fail"


# -------------------------------
# Output Agent
# -------------------------------
class OutputAgent:

    def display(self, student, grade):

        print("\n----- Student Report -----")
        print("Name  :", student["name"])
        print("Marks :", student["marks"])
        print("Grade :", grade)


# -------------------------------
# Tool Manager
# -------------------------------
class ToolManager:

    VALID_TOOLS = ["StudentAgent"]

    def use_tool(self, tool_name):

        if tool_name not in self.VALID_TOOLS:
            raise Exception(f"Tool '{tool_name}' is not available.")

        return StudentAgent()


# -------------------------------
# Main Function
# -------------------------------
def run_agent(student_id, tool_name):

    try:

        tool = ToolManager().use_tool(tool_name)

        student = tool.get_student(student_id)

        grade = EvaluationAgent().evaluate(student)

        OutputAgent().display(student, grade)

    except Exception as e:
        print("\nERROR:", e)
run_agent("S101", "StudentAgent")
STUDENT_DATABASE["S105"] = {
    "name": "Ramesh"
}

run_agent("S105", "StudentAgent")
run_agent("S101", "AttendanceAgent")