# python_smart_calc
This program is created for dealing with simple equations containing brackets, and supports the following operators:
+, -, *, /, %, ^. User can also declare his own variables (e.g. a = 5). My goal was to create calculator without using
eval method, so it can be considered as safe. It was also my first attempt to create something using regular expressions.
To compute given equations, program convert regular notation to reversed polish notation by using algorithm placed in 
utils folder.
Please read about program limitations below to avoid errors:

- Input need to be typed with INTEGERS, floating point numbers will not work (still, result can be shown as float).
- variable name can contain ONLY letters, and it's case sensitive.
- If you need to use brackets, remember to close them, as without it program may work incorrectly or error may be printed out.
- For raising to power, you need to use '^' operator. Double star (**) won't work.

Use /exit command if you want to close application.
