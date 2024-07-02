import matplotlib.pyplot as plt

courses = ['Data Science', 'Web Development', 'Machine Learning', 'Artificial Intelligence']
students = [120, 80, 150, 90]
plt.bar(courses, students, color='skyblue')
plt.title('Number of Students Enrolled in Each Course')
plt.xlabel('Courses')
plt.ylabel('Number of Students')
plt.show()