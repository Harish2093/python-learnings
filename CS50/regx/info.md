. any character except a newline
* 0 or more repetitions
+ 1 or more repetitions
? 0 or 1 repetitions
{m} m repetitions
{m, n} m-n repetitions




\d Decimal digit
\D not a decimal digit
\s Whitespace character
\S not a whitespace character
\w word character--- as well as numbers and the underscore
\W not a word character

A|B either A or B
(...) a group
(?:...) non capturing version

Flags:
1. re.IGNORECASE
2. re.MULTILINE
3. re.DOTALL