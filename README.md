# CS50Flix
### Video Demo: https://youtu.be/F5jocse0xnI
### Description:
The project is a Netflix clone for programming and computer science courses.

It's called CS50Flix.

It was developed in Python with Django on the backend, and on the frontend I used HTML with Tailwind for the CSS, and a little of JavaScript.

I decided to use Django to try out another framework, as we had already used Flask during the course.

Unlike Flask, Django already comes with a completely ready-made development framework, which we are obliged to follow.

I used SQLite as the database.

This was my initial planning outline:
 1. Homepage
 2. Login / Create account (User and Authentication):
    2.1. Email;
    2.2. Username;
    2.3. Password;
    2.4. Watched videos;
    2.5. Edit profile;
 3. Courses:
    3.1. Thumb;
    3.2. Title;
    3.3. Description;
    3.4. Category;
    3.5. Number of views;
    3.6. Creation date;
    3.7. Lectures:
        3.7.1. Videos (youtube link);
        3.7.2. Title;
        3.7.3. Course;
 4. Search bar
 
 I created 10 HTML files and put them in the templates folder.
 
 I created 1 CSS file and put him in the static/css folder.
 
 All the images are in the static/images folder.
 
 I also edited the settings, admin, urls, views, models, forms, apps and some other files.
 
On the homepage we have the option to login or create an account, if you haven't already.

Putting the email, the site checks if that email is already registered. If yes, it redirects to login. If not, it redirects to the account creation page.

All the forms have validations, to ensure that the data is correct.

Once logged in, the homepage randomly displays course suggestions.

It also shows new courses added to the platform, the most popular ones, and courses already watched, in carousel style.

There is a search box for courses, an edit profile page and a logout button.

On the edit profile page you can change the name, email and password.

When you click on a course you are redirected to the course page and there you have all the lectures. Clicking on the lecture opens the video player (YouTube) and you can watch the lecture.

All steps:
1. Site Planning.
2. Starting the project in Django.
3. Initial structure.
4. Creating the first APP.
5. Creating the superuser and doing the migrations.
6. Connecting new project APP.
7. Editing the settings file.
8. Creating the course template.
9. Adding the template in the admin.
10. Configuring static and media folders.
11. Creating the first page.
12. Creating website templates and template structure.
13. Creating the base HTML and connecting the templates.
14. Creating the navbar and editing the HTML with Tailwind.
15. Editing the homepage.
16. Deciding between Function Based Views and Class Based Views.
17. Passing parameters to html pages with context.
18. Transforming views into classes.
19. Creating a view for each course.
20. Creating dynamic links.
21. Editing Lecture Model.
22. Connecting foreign key.
23. Listing the lectures.
24. Full screen video player.
25. Passing custom variables to views and all templates.
26. Creating context managers.
27. Creating views counter.
28. Editing the courses details page.
29. Editing the courses home page.
30. Making dynamic edits with JavaScript.
31. Creating the search field.
32. Creating custom users.
33. Creating the list of watched courses.
34. Registering the movies watched in the database dynamically.
35. Blocking pages for users who have not logged in.
36. Customizing the navigation bar for logged in users.
37. Creating the log out process.
38. Finalizing log in and log out pages.
39. Creating account creation page.
40. Creating dynamic redirection of users.
41. Creating page to edit profile.
42. Final adjustments.

There is still a lot to improve, but for me as a programming beginner, having managed to do something like this was already a great accomplishment.

I'm very proud and very happy. And I owe everything to the CS50.

And that's it.

I am Aldo Nunes and this is CS50!
