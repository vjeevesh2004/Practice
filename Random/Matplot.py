Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import matplotlib.pyplot as plt
... 
... # Sample data
... subjects = ['Math', 'Science', 'English', 'History', 'Geography']
... student_marks = [85, 78, 92, 74, 88]
... 
... # Adding titles and labels
... plt.title('Student Marks Across Subjects')
... plt.xlabel('Subjects')
... plt.ylabel('Marks')
... 
... plt.plot(subjects, student_marks)
