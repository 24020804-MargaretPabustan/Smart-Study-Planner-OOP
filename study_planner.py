from datetime import datetime

# -------------------------
# Task Class
# -------------------------
class Task:
    def __init__(self, taskId, title, description, deadline, status="Incomplete"):
        self.taskId = taskId
        self.title = title
        self.description = description
        self.deadline = deadline
        self.status = status
        self.studySession = None  # Will hold StudySession
        self.subject = None  # Link back to Subject

    def markComplete(self):
        self.status = "Complete"
        return f"The task '{self.title}' has been marked as complete."

    def updateDeadline(self, newDeadline):
        self.deadline = newDeadline
        return f"The deadline for task '{self.title}' has been updated to {newDeadline}."

    def getStatus(self):
        return f"The current status of task '{self.title}' is {self.status}"


# -------------------------
# StudySession Class
# -------------------------
class StudySession:
    def __init__(self, sessionId, date, duration, task):
        self.sessionId = sessionId
        self.date = date
        self.duration = duration
        self.task = task

    def schedule(self):
        return f"Study session for task '{self.task.title}' scheduled on '{self.date}' for '{self.duration}' hours."

    def cancel(self):
        return f"Study session for task '{self.task.title}' on '{self.date}' has been cancelled."

    def update(self, newDate, newDuration):
        self.date = newDate
        self.duration = newDuration
        return f"Study session for task '{self.task.title}' updated to '{self.date}' for '{self.duration}' hours."


# -------------------------
# Reminder Class
# -------------------------
class Reminder:
    def __init__(self, reminderId, message, dateTime, task):
        self.reminderId = reminderId
        self.message = message
        self.dateTime = dateTime
        self.task = task

    def schedule(self, dateTime):
        self.dateTime = dateTime
        return f"Reminder for task '{self.task.title}' at '{self.dateTime}' has been scheduled."

    def sendReminder(self):
        return f"Reminder: '{self.message}' for task '{self.task.title}' at '{self.dateTime}'"


# -------------------------
# Subject Class
# -------------------------
class Subject:
    def __init__(self, subjectId, name, priority=1):
        self.subjectId = subjectId
        self.name = name
        self.priority = priority
        self.tasks = []

    def addTask(self, task):
        task.subject = self  # Link task to this subject
        self.tasks.append(task)
        return f"Task '{task.title}' added to subject '{self.name}'."

    def getTasks(self):
        return self.tasks

    def setPriority(self, priority):
        self.priority = priority
        return f"Priority for subject '{self.name}' set to {priority}."


# -------------------------
# Student Class
# -------------------------
class Student:
    def __init__(self, studentId, name, email):
        self.studentId = studentId
        self.name = name
        self.email = email
        self.subjects = []

    def addSubject(self, subject):
        self.subjects.append(subject)
        return f"Subject '{subject.name}' added to {self.name}'s planner."

    def getSubjects(self):
        return self.subjects

    def getTasks(self):
        all_tasks = []
        for subject in self.subjects:
            all_tasks.extend(subject.getTasks())
        return all_tasks

    def getSchedule(self):
        schedule = []
        for subject in self.subjects:
            for task in subject.getTasks():
                if task.studySession:
                    schedule.append(task.studySession.schedule())
                else:
                    schedule.append(f"Task '{task.title}' (Subject: {subject.name}) has no scheduled study session yet.")
        return schedule


# -------------------------
# Planner Class
# -------------------------
class Planner:
    def __init__(self, student):
        self.student = student

    def generateSchedule(self):
        schedule = []
        for task in self.student.getTasks():
            if hasattr(task, "studySession") and task.studySession is not None:
                schedule.append(task.studySession.schedule())
            else:
                schedule.append(f"Task '{task.title}' (Subject: {task.subject.name}) has no scheduled study session yet.")
        return schedule

    def prioritizeTasks(self):
        all_tasks = self.student.getTasks()
        sorted_tasks = sorted(all_tasks, key=lambda t: (t.subject.priority, t.deadline))
        return sorted_tasks

    def suggestStudySession(self, default_duration=2, start_date=None):
        if start_date is None:
            start_date = datetime.today().strftime('%Y-%m-%d')
        suggestions = []
        for task in self.student.getTasks():
            if not task.studySession:
                task.studySession = StudySession(
                    sessionId=f"SS-{task.taskId}",
                    date=start_date,
                    duration=default_duration,
                    task=task
                )
                suggestions.append(task.studySession.schedule())
        return suggestions


# -------------------------
# TEST CODE
# -------------------------
# Create student
student1 = Student(1, "Alice", "alice@email.com")

# Create subjects
math = Subject(101, "Mathematics", priority=2)
science = Subject(102, "Science", priority=1)

# Add subjects to student
student1.addSubject(math)
student1.addSubject(science)

# Create tasks
task1 = Task(201, "Finish Algebra Homework", "Chapter 5 exercises", "2026-04-05")
task2 = Task(202, "Prepare Science Presentation", "Volcano experiment", "2026-04-07")

# Add tasks to subjects
math.addTask(task1)
science.addTask(task2)

# Create planner
planner = Planner(student1)

# Suggest study sessions automatically
planner.suggestStudySession(default_duration=2)

# Generate schedule
print("=== Schedule ===")
for s in planner.generateSchedule():
    print(s)

# Prioritize tasks
print("\n=== Prioritized Tasks ===")
for t in planner.prioritizeTasks():
    print(f"{t.title} (Subject: {t.subject.name}, Priority: {t.subject.priority})")