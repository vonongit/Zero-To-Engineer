### Day 10 Task: Write a Python script that fetches data from multiple API endpoints and combines the results

Here's the scenario: A senior engineer asks you to pull user data and their associated posts from the API and display them together. Right now you can fetch users — but each user also has posts stored at a separate endpoint. She wants a report that shows each user's name alongside how many posts they've written.

The users endpoint you already know: https://jsonplaceholder.typicode.com/users

Posts for a specific user are at: https://jsonplaceholder.typicode.com/posts?userId=1 — where the number at the end is the user's ID.

Your script should fetch all users, then for each user fetch their posts, and print a summary showing each user's name and their post count.

What you'll need to figure out: You already know how to make a single API request. The new challenge is making multiple requests in a loop — one per user — and combining data from two different endpoints. Think about how your existing get_data() function can be reused here rather than rewritten.