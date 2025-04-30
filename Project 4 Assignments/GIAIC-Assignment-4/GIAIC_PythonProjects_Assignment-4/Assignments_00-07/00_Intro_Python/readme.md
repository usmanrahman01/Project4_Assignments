🎨 ANSI Escape Codes for Terminal Formatting
ANSI escape codes are special sequences used to control the appearance of text in terminal outputs. They allow you to format text with colors, styles, and cursor positioning, and are widely supported on Linux, macOS, and many modern Windows terminals.

✨ Why Use ANSI Escape Codes?
Add color to highlight outputs

Apply styles like bold, italic, or underlined

Improve readability in command-line applications

Reset formatting to maintain clean output

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
💻 Python Example
python
Copy
Edit
print("\033[1;34mBold Blue Text\033[0m")     # Bold Blue
print("\033[3;31mItalic Red Text\033[0m")    # Italic Red
print("\033[4;32mUnderlined Green Text\033[0m")  # Underlined Green
Example Output:
🔵 Bold Blue Text
🔴 Italic Red Text
🟢 Underlined Green Text

❗ Why Reset with \033[0m?
Failing to reset the formatting may result in the applied styles continuing into subsequent output.

Without Reset:
python
Copy
Edit
print("\033[1mBold Text!")
print("Normal Text")  # This will also appear bold!
With Reset:
python
Copy
Edit
print("\033[1mBold Text!\033[0m")
print("Normal Text")  # Back to normal
🎨 Extended Color Codes
Code	Color
\033[30m	Black
\033[31m	Red
\033[32m	Green
\033[33m	Yellow
\033[34m	Blue
\033[35m	Magenta
\033[36m	Cyan
\033[37m	White
🧠 Conclusion
ANSI escape codes are a simple and powerful way to style terminal outputs. Whether you're building a CLI tool, writing logs, or just making your outputs easier to read, ANSI codes are a valuable tool in your developer toolbox.

📌 Note: The default Windows Command Prompt may not fully support ANSI codes. For best results, use Windows Terminal, PowerShell (with ANSI enabled), or a Unix-based terminal.

Happy Coding! 🚀