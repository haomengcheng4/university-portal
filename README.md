Technical Specification for University Portal Development
Technologies Used
• The application must be strictly written in one of the following languages: C#, Java, Python, or PHP.
• The DBMS for the application should be MsSql/MySql/Postgres.
General Information
Develop an application that provides the following functionality:
• User authentication, authorization, and registration (login – student ID number + year of admission, password – generated and sent to the email upon request);
• User role-based access control;
• Implementation of a schedule display system in the context of: (groups/classrooms/teachers);
• Implementation of student actions:
o View academic performance by subjects + highlight debts;
o Request a certificate of enrollment at the university;
o Request a retake referral with the ability to navigate from the subject debt page;
o Submit an application for an increased scholarship with the attachment of a set of certificates, diplomas, and other documents.
• Implementation of teacher actions:
o View academic performance by subjects in the form of a grade sheet;
o Fill out the grade sheet for a subject during the examination period;
o Publish an announcement for a specific group or all students (unavailable due to a business trip, class rescheduling, event announcement).
• Formation and maintenance of a database of registered users, roles, classes, subjects, classrooms, grades, applications, etc.
• Provision of an API for server clients.
The database should contain the following information:
• Registered users;
• Classrooms;
• Subjects;
• Classes;
• Groups;
• Applications;
• Grades;
• Documents;
• etc.

Requirements:
• The project must compile and run without errors.
• Ensure automatic generation and initial population of the database.
• Do not store the database connection string in the code; use configuration files.
• Implement user model validation (login and password must not be empty and must not be the same).
• Implement user authorization based on roles.
• Implement user authentication using one of the following methods (JWT token, cookies, claims, roles).
• The "Users" table must contain: username and password.
Constraints:
• An unlimited number of files can be uploaded with an application.
• The total file size must not exceed 250 MB (the API should handle exceeding the limit gracefully).
• Files for announcements must be in .pdf, .doc, or .jpg formats.
Will be a plus:
• Use migrations for changing the database structure and populating data.
• Use built-in model validation mechanisms.
• Store passwords in the database in encrypted form.
• Implement database interaction in the application through an ORM.
• Clean code (API logic and database operations in separate classes and services).
• Use design patterns.
• Implement unit tests.
 
Submission Format
It is necessary to provide a link to the explanatory note file (up to 5 pages) in *.pdf format, indicating the executor and a brief description of the completed task. The text of the explanatory note must contain a link to an open repository on https://github.com or a link to an archive with the prepared solution for the completed task (Yandex Disk, Mail.ru Cloud, etc.).
The archive and repository must contain a readme file with instructions for building the project, launching the application, and a description of any non-obvious decisions.
ATTENTION
You can submit a solution that implements only part of the described functionality. Such a solution will also be evaluated, and the participant will receive points.

