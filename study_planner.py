from datetime import datetime


# -------------------------
# Task Class - Creates a task blueprint, can use it to create multiple tasks (each task object represents smth student needs to do)
# -------------------------
class Task:
    def __init__(self, taskId, title, description, deadline, status="Incomplete"):
        self.__taskId = taskId
        self.__title = title
        self.__description = description
        self.__deadline = deadline
        self.__status = status
        self.__studySession = None  # Will later link to a StudySession object
        self.__subject = None  # Link the task back to a subject (e.g. Math, Science, etc.)

    #-------------------------
    # Getter Methods - Return values like taskId, title, description, deadline, status (One of the important OOP principles is Encapsulation, so I used getter methods to access private attributes safely)
    #-----------------------
    def getTaskId (self):
        return self.__taskId
    def getTitle(self):
        return self.__title
    def getDescription(self):
        return self.__description
    def getDeadline(self):
        return self.__deadline
    def getStatus(self):
        return self.__status
    def getStudySession(self):
        return self.__studySession

    def getSubject(self):
        return self.__subject
    
    #-------------------------
    #Setter Methods - Update values for attributes (e.g.title, description, deadline, status)
    #-------------------------
    def setDeadline(self,newDeadline):
         self.__deadline = newDeadline
         return f"Deadline for task '{self.__title}' updated to {newDeadline}."
    def setSubject(self, subject):
        """Links the task to a subject."""
        self.__subject = subject
    
    def setStudySession(self,session):
        """Links task to a study session."""
        self.__studySession = session
    
    def setStatus(self, status):
        self.__status = status
        return f"Task status updated to '{self.__status}'."

    def setTitle(self, title):
        self.__title = title
        return f"Task title updated to '{self.__title}'."

    def setDescription(self, description):
        self.__description = description
        return f"Task description updated to '{self.__description}'."


    #-------------------------
    # Utility Methods - Mark task as complete, checks whether the deadline has passed, update task details (Extra helpful features for students to manage their tasks effectively)

    def markComplete(self):
        """Marks the task as complete."""
        self.__status = "Complete"
        return f"The task '{self.__title}' has been marked as complete."
    def isOverdue(self):
        """Checks if the task is overdue."""
        today = datetime.today()
        deadline_dt = datetime.strptime(self.__deadline, "%Y-%m-%d")
        return today > deadline_dt
    
    def displayTask(self):
        """Returns the task details in string format"""
        return f"Task:{self.__title} | Deadline: {self.__deadline} | Status: {self.__status}"

    def updateDeadline(self, newDeadline):
        """Updates deadline for the task, based on student's preference and returns a confirmation message"""
        self.__deadline = newDeadline
        return f"The deadline for task '{self.__title}' has been updated to {newDeadline}."

    


# -------------------------
# StudySession Class
# -------------------------
class StudySession:
    """
    Represents a study session associated with a specific task.
    """
    def __init__(self, sessionId, date, duration, task):
        """Initialises a study session with a unique session ID, date, duration, and the associated task.
        Args:
        sessionId: Unique identifier for study session
        date(str):Date of study session in 'YYYY-MM-DD' format
        duration(float): Duration of study session in hours
        task(Task): The task associated with the study session
        """
        
        self.__sessionId = sessionId
        self.__date = date
        self.__duration = duration
        self.__task = task

    #-------------------------
    #Getter Methods - Return values like sessionId, date, duration, task
    #-------------------------
    def getSessionId(self):
        return self.__sessionId
    
    def getDate(self):
        return self.__date
    
    def getDuration(self):
        return self.__duration
    def getTask(self):
        return self.__task
    
    #-------------------------
    #Setter Methods - Update values for attributes (date, duration, task)
    def setDate(self,newDate):
        self.__date = newDate

    def setDuration(self,duration):
        self.__duration = duration

    def setTask(self, task):
        self.__task = task

    #-------------------------
    # Utility Methods - Schedule study session, cancel study session, update study session details (Extra helpful features for students to manage their schedules efficiently)
    def schedule(self):
        return f"Study session for task '{self.__task.getTitle()}' scheduled on '{self.__date}' for '{self.__duration}' hours."

    def cancel(self):
        return f"Study session for task '{self.__task.getTitle()}' on '{self.__date}' has been cancelled."

    def update(self, newDate, newDuration):
        self.__date = newDate
        self.__duration = newDuration
        return f"Study session for task '{self.__task.getTitle()}' updated to '{self.__date}' for '{self.__duration}' hours."


# -------------------------
# Reminder Class
# -------------------------
class Reminder:
    """Represents a reminder linked to a specific task, with a message and scheduled date/time."""  
    def __init__(self, reminderId, message, dateTime, task):
        """Initialises a reminder with a unique reminder ID, message, scheduled date/time, and the associated task."""
        self.__reminderId = reminderId
        self.__message = message
        self.__dateTime = dateTime
        self.__task = task

    #-------------------------
    #Getter Methods - Return values like reminderId, message, dateTime, task
    def getReminderId(self):
        return self.__reminderId

    def getMessage(self):
        return self.__message

    def getDateTime(self):
        return self.__dateTime

    def getTask(self):
        return self.__task
    
    #-------------------------
    #Setter Methods - Update values for attributes (message, dateTime, task)
    def setMessage(self, message):
        self.__message = message

    def setDateTime(self, dateTime):
        self.__dateTime = dateTime

    def setTask(self, task):
        self.__task = task

    #-------------------------
    # Utility Methods - Schedule reminder and notify student for a task
    def schedule(self, dateTime=None):
        if dateTime:
            self.__dateTime = dateTime
        return f"Reminder for task '{self.__task.getTitle()}' at '{self.__dateTime}' has been scheduled."

    def sendReminder(self):
        """Returns reminder message for the specific task at the scheduled date/time."""
        return f"Reminder: '{self.__message}' for task '{self.__task.getTitle()}' at '{self.__dateTime}'"


# -------------------------
# Subject Class
# -------------------------
class Subject:
    """Represents a subject that contains many tasks, with a name and priority level."""
    def __init__(self, subjectId, name, priority=1):
        self.__subjectId = subjectId
        self.__name = name
        self.__priority = priority
        self.__tasks = []

    #-------------------------
    #Getter Methods - Return values like subjectId, name, priority, tasks
    def getSubjectId(self):
        return self.__subjectId
    def getName(self):
        return self.__name
    def getPriority(self):
        return self.__priority
    def getTasks(self):
        return self.__tasks
    
    #-------------------------
    #Setter Methods - Update values for attributes (name, priority) 
    def setName(self,name):
        self.__name = name

    def setPriority(self, priority):
        self.__priority = priority
        return f"Priority for subject '{self.__name}' set to {priority}."

    #-------------------------
    # Utility Methods - Add task to subject and link task back to subject #
    def addTask(self, task):
        """Adds a task to the subject and links the task back to this subject. Returns a confirmation message."""
        task.setSubject(self) # Link the task back to this subject
        self.__tasks.append(task) #The task is added to the subject's internal task list (which explains the 2 loops in lines 289 to 291, where we loop through subjects and then tasks within each subject to get all tasks for the student)
        return f"Task '{task.getTitle()}' added to subject '{self.__name}'."

    

# -------------------------
# Student Class
# -------------------------
class Student:
    """
    Represents  a student who manages multiple subjects"
    Stores student ID, name, email and list of subjects"""
    def __init__(self, studentId, name, email):
        self.__studentId = studentId
        self.__name = name
        self.__email = email
        self.__subjects = []
    
    #-------------------------
    #Getter methods - Return values like studentId, name, email, subjects
    def getStudentId(self):
        return self.__studentId
    def getName(self):
        return self.__name
    def getEmail(self):
        return self.__email
    def getSubjects(self):
        return self.__subjects

    #-------------------------
    #Setter Methods - Update values for attributes (name, email)
    def setName(self, name):
        self.__name = name

    def setEmail(self, email):
        self.__email = email

    #-------------------------
    # Utility Methods - Returns confirmation message when subject is added to student's planner

    def addSubject(self, subject):
        self.__subjects.append(subject)
        return f"Subject '{subject.getName()}' added to {self.__name}'s planner."
    
    def getTasks(self):
        """Returns a list of all tasks across all subjects for the student."""
        tasks = []
        for subject in self.__subjects:
            tasks.extend(subject.getTasks())
        return tasks

    def getSimpleSchedule(self):
        """Generates a simple list for all students' tasks, with their details"""
        #Create an empty list called schedule, we will put all the task info inside this list
        schedule = []
        #Loop through the subjects the student has
        for subject in self.__subjects:
        #Loop through the tasks for each subject,add task details (title, subject name, deadline, status) to the schedule list
            for task in subject.getTasks():
                schedule.append(f"{task.getTitle()} (Subject: {subject.getName()}) - Deadline: {task.getDeadline()} - Status: {task.getStatus()}")
        return schedule
    

# -------------------------
# Planner Class
# -------------------------
class Planner:
    """Represents a planner that generates schedules, handles task prioritisation and suggest study sessions for student"""
    def __init__(self, student):
        self.__student = student

    #-------------------------
    #Getter Methods - Return values like student
    def getStudent(self):
        return self.__student
    
    #-------------------------
    # Utility Methods - Generate schedule for all tasks, prioritise tasks based on subject priority and
    def generateSchedule(self):
        """Generates a detailed schedule of all tasks and study sessions."""
        schedule = []
        for task in self.__student.getTasks():
            studySession = task.getStudySession() if hasattr(task, 'getStudySession') else None
            if studySession:
                schedule.append(studySession.schedule())
            else:
                subject = task.getSubject() if hasattr(task, 'getSubject') else None
                subjectName = subject.getName() if subject else "Unknown Subject"
                schedule.append(f"Task '{task.getTitle()}' (Subject: {subjectName}) has no scheduled study session yet.")
        return schedule


    def prioritizeTasks(self):
            """Returns tasks sorted by subject priority, status and deadline."""
            #This method sorts the student's task based on priority, status and deadline
            #Gets all task the student has
            all_tasks = self.__student.getTasks() 
            
            #Orders task based on status (incomplete tasks come before complete tasks)
            def status_order(status):
                #Marks task incomplete with 0, and complete with 1, so that incomplete tasks are sorted first.
                return 0 if status == "Incomplete" else 1 # Incomplete first
            
            #Make a new sorted list of tasks based on priority, status and deadline, using the current list all_tasks
            sorted_tasks = sorted(
                all_tasks,
                #key=lambda Tells python how to decide the order when sorting the list of tasks, looks at priority first, then status then deadline
                key=lambda t: ( #t: Looks at one task at a time
                    t.getSubject().getPriority(),#Get priority method from Subject class, lower number means higher priority will be sorted first
                     status_order(t.getStatus()), #Get status of tasks first (From Task Class), those that are incomplete (0) will be sorted before complete (1)
                    datetime.strptime(t.getDeadline(), "%Y-%m-%d"), #Looks at the task's deadline (Task Class), convert it into datetime format, earlier deadlines come first#
                   
                )
            )
            return sorted_tasks


    def suggestStudySession(self, default_duration=2, start_date=None):
            """Automatically suggests study sessions for tasks without a session."""
            if start_date is None:
                start_date = datetime.today().strftime('%Y-%m-%d')
            suggestions = []
            for task in self.__student.getTasks():
                if not task.getStudySession():  # Uses getter method
                    session = StudySession(
                        sessionId=f"SS-{task.getTaskId()}",
                        date=start_date,
                        duration=default_duration,
                        task=task
                    )
                    task.setStudySession(session)  # Link the session to the task
                    suggestions.append(session.schedule())
            return suggestions


# -------------------------
# TEST CODE
# -------------------------
# Create student
