# Michael's Angry Dice Code Review
by Tiffany Ralph
August 12, 2015
----------------------------------------

Hi Michael! I'm reviewing this code line by line, looking at how you organized your code and logic, as well how you did things.

To reference a specific line, I will use the shorthand L5, which stands for Line 5. Until I give a new line or function name, the notes I give are in relation to the last given element or structure.

If I use the shorthand 'nit,' that means I'm 'nitpicking' – giving a comment that you should take into consideration, but it's not a hard rule. You could do what my nit suggests, or not, though I feel the nit is a better way.

Please let me know if you have any questions on my comments! 
-----------------------------------------

L2 – Nice reference to the BGG page; Giving credit where it's due.

L7 – You class name should be what the object is, which in this case is not Launch, but AngryDice. Launch would be a better name for the function that starts the game.

L8-10 – This comment is off, as per my note above. This class is AngryDice, which I think you get now, but not when you wrote this assignment.

L14 – I'm not sure why you're making this list. You're storing user's input in the list, and then using it later for tests, but why not just have a string and pass the string around? You don't need to store every input the user ever gives you, which is what this list is doing. Either way, you should, at the very least, leave a comment as to why you have this list and what you're going to do with it, so that people that are looking at your code later can figure it out :)

L50 – nit: This doesn't match the input prompt specified in the assignment

L96 – This isn't actually what this function does. You know what level stage you are in, what you're doing is actually calling that stage's function, right? So test_stage is also sorta a bad name for the function, cause you're not testing the stage, you're just calling the right stage function.

nit: I wouldn't name my functions text_blank, as it implies it's a test function – to test the functionality of your code. check_input would be better, or check_stage.

You have some sparse comments on some functions, but not a lot of comments within the functions themselves explaining what you're doing. Please get in the habit of commenting more :D Your future coworkers and your current instructor will thank you.

You Pass your Intro Python section, though, spoilers, you would have passed with Distinction if you had thoroughly commented your code.

