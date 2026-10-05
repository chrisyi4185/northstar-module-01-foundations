# Brainstorm: Skyline Online Courses Analytical Questions

## Prompt used

Role: Act as a senior data analyst helping me scope an analytical project.
Task: Brainstorm analytical questions I should consider asking of the dataset described below.
Context: The dataset is for Skyline Online Courses, a fictional small online learning platform. It has 100 rows, one row per enrollment. Columns are:
•	enrollment_id (nominal, unique ID per enrollment)
•	course_name (nominal, categorical: Intro to Analytics, Python for Beginners, SQL Basics, Tableau Fundamentals, Statistics 101)
•	enrollment_year (interval, intiger year between 2022 and 2026 inclusive)
•	final_grade (ordinal, One of F, D, C, B, A)
•	hours_studied (ratio, continuous number of hours spent in the course)
•	completion_status (nominal, categorical: Completed, Dropped, In Progress)
The program is interested in understanding course performance and student behavior. 
Constraints: Only suggest questions that can be answered from the columns listed above. Don't invent additional columns. For each suggested question, identify which columns would be used.
Output Format: A numbered list of 8 to 12 analytical questions. For each question, include a brief description (one sentence) and the relevant columns.


## Tool 1: Claude Output

Here are 11 analytical questions, grouped loosely from simple descriptive questions to more comparative ones. Each uses only the six columns you listed.

Which courses have the highest and lowest completion rates? Compare the share of Completed, Dropped, and In Progress enrollments within each course to see where students stick with it or leave.
Columns: course_name, completion_status
What does the overall grade distribution look like, and how does it differ by course? Count how many enrollments earned each grade (F through A) overall and per course to spot courses that are notably harder or easier.
Columns: final_grade, course_name
Do students who study more hours earn better grades? Compare average or median hours_studied across grade levels to see whether more study time lines up with higher grades.
Columns: hours_studied, final_grade
How do study hours differ between students who complete a course and those who drop it? Compare the distribution of hours_studied for Completed versus Dropped enrollments to see whether dropping tends to happen early, after little effort.
Columns: hours_studied, completion_status
Is there a "tipping point" in study hours where completion becomes much more likely? Bin hours_studied into ranges and look at the completion rate in each bin to find a threshold where outcomes shift.
Columns: hours_studied, completion_status
How have enrollment volumes changed from 2022 to 2026, overall and by course? Count enrollments per year per course to identify which courses are growing, shrinking, or holding steady.
Columns: enrollment_year, course_name, enrollment_id
Has the completion rate changed over time? Track the proportion of Completed and Dropped enrollments by enrollment_year to see whether retention is improving or worsening.
Columns: enrollment_year, completion_status
Have final grades improved or declined across enrollment years? Compare grade distributions by year to check for trends in student performance.
Columns: enrollment_year, final_grade
Which courses require the most study time, and does that explain differences in outcomes? Compare average hours_studied by course, then see whether the more time-intensive courses also have lower completion rates or grades.
Columns: course_name, hours_studied, completion_status, final_grade
Do grades vary by completion status, and are there data quality issues to resolve? Check which grades appear for Dropped and In Progress enrollments (for example, whether those rows have final grades at all), which tells you how to scope any grade analysis to Completed enrollments only.
Columns: final_grade, completion_status
Are there outliers or unusual patterns in hours_studied? Look for enrollments with very high or near-zero hours, especially among those with high grades or Dropped status, to flag data entry errors or distinct student behavior.
Columns: hours_studied, final_grade, completion_status, enrollment_id

A few scoping notes as you plan:

Question 10 is worth answering first, since it determines whether grade-based questions (2, 3, 8) should include all 100 rows or only completed ones.
In Progress enrollments will skew recent years (likely 2026). Questions 7 and 8 should account for that, or you may mistake unfinished enrollments for poor retention.
With only 100 rows, splitting by course and year at the same time leaves very small groups (roughly 20 per course, fewer per course-year). Treat patterns in questions 6 and 9 as directional rather than conclusive.
Final grade is ordinal, so medians or grade-level counts are safer summaries than a plain mean unless you deliberately map grades to numbers.

## Tool 2: ChatGPT Output

Which courses have the highest and lowest completion rates?
Compare the proportion of enrollments marked “Completed” across courses.
Relevant columns: course_name, completion_status
How does completion status vary by enrollment year?
Examine whether the proportions of Completed, Dropped, and In Progress enrollments have changed from 2022–2026.
Relevant columns: enrollment_year, completion_status
Which courses have the highest average final grades?
Compare final-grade distributions or convert the ordinal grades to an appropriate ordered scale to evaluate course-level performance.
Relevant columns: course_name, final_grade
Is the amount of time students study associated with their final grade?
Investigate whether students who spend more hours studying tend to achieve higher grades.
Relevant columns: hours_studied, final_grade
Do students who complete courses study more hours than students who drop them?
Compare study-time distributions across completion statuses.
Relevant columns: hours_studied, completion_status
Which courses have the highest average study time?
Compare the average number of hours studied across the five courses.
Relevant columns: course_name, hours_studied
Is the relationship between study time and final grade consistent across courses?
Determine whether higher study time is associated with higher grades similarly for each course.
Relevant columns: course_name, hours_studied, final_grade
How does the distribution of final grades differ by course?
Compare the proportions of A, B, C, D, and F grades across courses.
Relevant columns: course_name, final_grade
Has average study time changed across enrollment years?
Examine whether the typical number of hours studied per enrollment has increased or decreased from 2022–2026.
Relevant columns: enrollment_year, hours_studied
Has course performance changed over time?
Compare final-grade distributions across enrollment years to identify potential changes in student outcomes.
Relevant columns: enrollment_year, final_grade
Are students with higher study time more likely to complete a course?
Examine whether hours studied differs systematically among Completed, Dropped, and In Progress enrollments.
Relevant columns: hours_studied, completion_status
Which course-year combinations show the strongest or weakest completion performance?
Compare completion status across both courses and enrollment years to identify combinations with notably different outcomes.
Relevant columns: course_name, enrollment_year, completion_status

## Verification

| Check | # | Question | Source | Notes |
| ----- | --- | ------ | ------ | ----- |
| ✓ | 1 | Which courses have the highest and lowest completion rates? | Both | Compare proportions, might need later | 
| ✓ | 2 | How does completion status vary by enrollment year? | Both | Compare proportions over time, might need later |
| ✓ | 3 | Which courses have the highest average final grades? | ChatGPT | Compare distributions or convert to ordered scale for more analysis |
| ✓ | 4 | Is the amount of time students study associated with their final grade? | ChatGPT | Need to convert to ordered scale for calculations |
| ✓ | 5 | Do students who complete courses study more hours than students who drop them? | Both | Compare distributions |
| ✓ | 6 | Which courses have the highest average study time? | Both | Compare means |
| ✓ | 7 | Is the relationship between study time and final grade consistent across courses? | Both | Needs ordered conversion here too |
| ✓ | 8 | How does the distribution of final grades differ by course? | Both | Compare proportions |
| ✓ | 9 | Has average study time changed across enrollment years? | ChatGPT | Means by course |
| ✓ | 10 | Has course performance changed over time? | ChatGPT | Needs ordered conversion |
| ✓ | 11 | Which course-year combinations show the strongest or weakest completion performance? | ChatGPT | Looking for outliers |
| ✓ | 12 | Is there a tipping point in study hours where completion becomes much more likely? | Claude | Looking for a threshold when sorted into ranges |
| ✓ | 13 | How have enrollment volumes changed from 2022 to 2026, overall and by course? | Claude | Comparison, might need later |
| ✓ | 14 | Have final grades improved or declined across enrollment years? | Claude | Comparison, trend line might be useful |
| ✓ | 15 | Do grades vary by completion status, and are there data quality issues to resolve? | Claude | Looking for scope on analysis |
| ✓ | 16 | Are there outliers or unusual patterns in hours_studied? | Claude | Catch data entry errors, distinct behavior |


## Verified Question List

| # | Question |
| --- | ------- |
| 1 | Which courses have the highest and lowest completion rates? |
| 2 | How does completion status vary by enrollment year? |
| 3 | How have enrollment volumes changed from 2022 to 2026, overall and by course? | 
| 4 | Do grades vary by completion status? |
| 5 | Do students who complete courses study more hours than students who drop them? |
| 6 | Has average study time changed across enrollment years? |
| 7 | Is there a tipping point in study hours where completion becomes much more likely? |
| 8 | Which courses have the highest and lowest study times? |
| 9 | Which courses have the highest and lowest average grades? |
| 10 | Is the amount of time studied associated with their final grade? |
| 11 | How does the distribution of final grades differ by course? |
| 12 | Is the relationship between study time and final grade consistent across all courses? |
| 13 | Which course-year combinations show the strongest and weakest performance? |
| 14 | Are there any outliers or unusual patterns that would indicate data entry error or distinct student behavior? |

## Reflection

On review of the questions produced by Claude and ChatGPT there was a lot of overlap, and many of the questions would need the letter grades changed to a numeric format to calculate means and medians. There is a lot of space to look for correlation and causation in this dataset. I kept 14 questions because all of them would give insight to the decision making process, but 14 where I would look for outliers or distinct behavior was the most questionable one because distinct behavior could apply to all of the courses if a specific student was enrolled in all of them at one point and kept the same habits. At this point, it might not be the most time effective solution, but I would want to run all of these questions to dial in my approach. A more specific inquiry from the client would help because student behavior is a very broad topic. 