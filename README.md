# Smart-Study-Planner-OOP Project Overview
An object-oriented, user-friendly study planner that allows students to manage tasks, schedule study sessions and track progress efficiently.

This project demonstrates the practical application of Object-Oriented Programming (OOP) in organising and managing students' study sessions in a practical context such as:

1. Classes and Objects (Student, Subject, Task, StudySession, Reminder, Planner)
2. Encapsulation (The use of private attributes)


This planner is designed to simulate real-world task management for students in a console-based Python Application.

# Key Objectives
- Help students prioritise tasks and subjects efficiently
- Automatically suggest study sessions
- Track progress with reminders 

# Features
-  Add subjects and tasks with deadlines
- Mark tasks as complete and update deadlines
- Schedule, update and cancel study sessions
- Display reminders for tasks at specific timings
- Generate a simple schedule for all tasks
- Prioritize tasks based on subject priority, status and deadlines
- Detect any overdue tasks which keeps students on track with their schedule

# Class Overview

1. Student - Keeps track of student's subjects and tasks
- Attributes: studentId, name, email, subjects
- Methods: addSubject(), getSubjects(), getTasks(), getSchedule()

2. Subject - Represents a subject and its tasks
- Attributes: subjectId, name, priority, tasks
- Methods: addTask(), getTasks(), setPriority()

3. Task - Represents a student's task
- Attributes: taskId, title, description, deadline, status, studySession
- Methods: markComplete(), updateDeadline(), getStatus()

4. StudySession - Schedules and tracks study sessions
- Attributes: sessionId, date, duration, task
- Methods: schedule(), update(), cancel()

5. Planner - Suggests study sessions and prioritizes tasks
- Attributes: student
- Methods: suggestStudySession(), prioritizeTasks(), generateSchedule()

6. Reminder - Notifies students about upcoming tasks
- Attributes: reminderId, message, dateTime, task
- Methods: sendReminder(), schedule()


# Installation/Usage

1. Ensure that Python 3.x is installed

2. Clone this repository:
https://github.com/24020804-MargaretPabustan/Smart-Study-Planner-OOP

3. Navigate to the project directory:
cd Smart-Study-Planner-OOP

4. Run the main script:
python study_planner.py











