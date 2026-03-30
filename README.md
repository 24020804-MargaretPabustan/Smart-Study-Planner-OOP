# Smart-Study-Planner-OOP Project Overview
An object-oriented, user-friendly study planner that allows students to manage tasks, schedule study sessions and track progress efficiently.

This project demonstrates the practical application of Object-Oriented Programming (OOP) in organising and managing students' study sessions in a practical context such as:

1. Classes and Objects (Student, Subject, Task, StudySession, Reminder, Planner)
2. Encapsulation (The use of private attributes)


This planner is designed to simulate real-world task management for students in a console-based Python Application.


# Class Overview

1. Student - Keeps track of student's subjects and provides methods to retrieve all tasks and view schedule
- Attributes: studentId, name, email, subjects
- Methods: addSubject(), getSubjects(), getTasks(), getSchedule()

2. Subject - Represents subjects that the student is studying, contains a list of tasks, priority level and methods to add tasks and set priority level
- Attributes: subjectId, name, priority, tasks
- Methods: addTask(), getTasks(), setPriority()

3. Task - Represents a specific task student is working on, methods mark the task complete, update deadlines and check current status of tasks
- Attributes: taskId, title, description, deadline, status, studySession
- Methods: markComplete(), updateDeadline(), getStatus()

4. StudySession - Allows students to schedule study sessions (Schedule, Update, Cancel sessions)
- Attributes: sessionId, date, duration, task
- Methods: schedule(), update(), cancel()



