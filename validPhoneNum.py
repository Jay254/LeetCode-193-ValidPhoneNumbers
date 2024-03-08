# Read from the file file.txt and output all valid phone numbers to stdout.

 ## SHELL COMMAND
#grep -P '^(\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4})$' file.txt

# grep: Command-line utility for searching plain-text data sets for lines that match a regular expression.

# -P: Enable Perl-compatible regular expressions (PCRE) for more advanced pattern matching.

# '^': Match the beginning of a line.

# (': Start of a group.

# '\(': Match an opening parenthesis.

# '\d{3}': Match exactly three digits.

# '\)': Match a closing parenthesis.

# ' ': Match a space.

# '\d{3}': Match exactly three digits.

# '-': Match a hyphen.

# '\d{4}': Match exactly four digits.

# '|': Alternation operator (matches either the pattern on its left or the pattern on its right).

# '\d{3}-\d{3}-\d{4}': Pattern for the second format.

# ')': End of the group.