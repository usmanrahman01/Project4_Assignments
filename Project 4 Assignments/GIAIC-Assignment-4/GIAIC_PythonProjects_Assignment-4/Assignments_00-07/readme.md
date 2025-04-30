🐍 Python Assignments Overview
00 - Introduction & Basic Python Scripts
Start with the basics! Learn Python's syntax, how to write scripts, print output, take user input, and perform simple calculations.

01 - Expressions
Explore mathematical operations, logical expressions, and variable manipulations to perform meaningful computations.

02 - Lists
Understand Python’s versatile list data structure — learn how to create, index, slice, append, and manipulate lists efficiently.

03 - Dictionaries
Master dictionaries to store key-value pairs. Learn how to create, access, update, delete, and loop through dictionary items.

04 - If Statements
Make decisions in your code using conditional logic. Understand how if, elif, and else work in various scenarios.

05 - Loops & Control Flow
Automate repetitive tasks using for and while loops. Learn to control flow with break, continue, and nested loops.

06 - Functions
Organize your code with reusable functions. Learn how to define functions, pass arguments, return values, and structure your logic better.

07 - Information Flow
Grasp how data moves within a program: understand scope, variable lifetimes, function data-passing, and clean coding practices.

💡 Each assignment includes practical exercises designed to solidify your Python foundations.
Happy coding! 🧠🚀

🎨 ANSI Escape Codes for Terminal Formatting
ANSI escape codes are special sequences used to format terminal output. These work on Linux, macOS, and many modern Windows terminals.

✨ Why Use ANSI Codes?
Add colors to your output

Apply bold, italic, or underlined styles

Improve the visual clarity of terminal applications

📋 Basic ANSI Escape Codes
Code	Effect
\033[0m	Reset formatting
\033[1m	Bold text
\033[3m	Italic text
\033[4m	Underlined text
\033[31m	Red text
\033[32m	Green text
\033[33m	Yellow text
\033[34m	Blue text
\033[1;33m	Bold Yellow
\033[1;34m	Bold Blue
💻 Example Usage in Python
python
Copy
Edit
print("\033[1;34mBold Blue Text\033[0m")
print("\033[3;31mItalic Red Text\033[0m")
print("\033[4;32mUnderlined Green Text\033[0m")
Output:
🔵 Bold Blue Text
🔴 Italic Red Text
🟢 Underlined Green Text

❗ Why Reset with \033[0m?
If you forget to reset the style, all text afterward will inherit the last applied format.

Without Reset:
python
Copy
Edit
print("\033[1mBold Text!")
print("Normal Text")  # Still bold!
With Reset:
python
Copy
Edit
print("\033[1mBold Text!\033[0m")
print("Normal Text")  # Back to normal
🎨 More Color Codes
Code	Color
\033[30m	Black
\033[31m	Red
\033[32m	Green
\033[33m	Yellow
\033[34m	Blue
\033[35m	Magenta
\033[36m	Cyan
\033[37m	White
📦 Conclusion
ANSI escape codes make your terminal output more vibrant and readable — ideal for command-line apps, logs, or text-based UI.

📌 Note: Default Windows Command Prompt may not support ANSI codes. Use Windows Terminal or enable ANSI in PowerShell for full support.

Happy coding! ✨💻

