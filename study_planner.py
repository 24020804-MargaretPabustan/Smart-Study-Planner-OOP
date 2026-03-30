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

    #Marks status of task as "Complete"
    def markComplete(self):
        self.status = "Complete"
        return f"The task '{self.title}' has been marked as complete."
    #Updates deadline of task to new deadline specified by user
    def updateDeadline(self, newDeadline):
        self.deadline = newDeadline
        return f"The deadline for task '{self.title}' has been updated to {newDeadline}."
    #Displays current status of task
    def getStatus(self):
        return f"The current status of task '{self.title}' is {self.status}"
    
# -------------------------
# StudySession Class
# -------------------------
class StudySession:
    def __init__(self,sessionId,date,duration,task):
        self.__sessionId = sessionId
        self.__date = date
        self.__duration = duration
        self.__task = task

    #Schedule the study session for the task, based on given date and duration.
    def schedule(self):
        return f"Study session for task '{self.__task.title}' scheduled on '{self.__date}' for '{self.__duration}' hours."
    
    #If applicable, cancel scheduled study session for the task.
    def cancel(self):
        return f"Study session for task {self.__task.title} on '{self.__date}' has been cancelled."
    
    #Update the study session schedule based on student's preference
    def update(self,newDate,newDuration):
        self.__date = newDate
        self.__duration = newDuration
        return f"Study session for task '{self.__task.title}' has been updated to '{self.__date}' for '{self.__duration}' hours."

#Code Reminder Class here---#        

# -------------------------
# Subject Class
# -------------------------
class Subject:
    def __init__(self, subjectId, name, priority=1):
        self.subjectId = subjectId
        self.name = name
        self.priority = priority
        self.tasks = []  # A subject has many tasks

    #Add item to task list
    def addTask(self, task):
        self.tasks.append(task)
        return f"Task '{task.title}' added to subject '{self.name}'."

    #Returns list of tasks
    def getTasks(self):
        return self.tasks

    #Sets priority of subject, so students can easily keep track of the most important subjects
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
        self.subjects = []  # Student has many subjects

    #Adding a subject to student's planner
    def addSubject(self, subject):
        self.subjects.append(subject)
        return f"Subject '{subject.name}' added to {self.name}'s planner."

    def getSubjects(self):
        return self.subjects

    # Collect all tasks across all subjects
    def getTasks(self):
        all_tasks = []
        for subject in self.subjects:
            all_tasks.extend(subject.getTasks())
        return all_tasks

    # Get a simple schedule (just list of task titles)
    def getSchedule(self):
        schedule = []
        for subject in self.subjects:
            for task in subject.getTasks():
                schedule.append(f"{task.title} (Subject: {subject.name})")
        return schedule


# -------------------------
# TEST CODE
# -------------------------

