# cv
Repository for my CV, typeset in LaTeX.

## Design
This template was designed to be relatively simple to use, such that someone with minimal TeX knowledge could pick up the file, edit it, and compile to PDF. 

## How To Use
This is a brief description on various elements of the CV TeX code.
### Education
Each line in the education section has three parts: degree type, description, and year.
These are separated by & symbols.

### List Items
Here is an example of an item in a "tablist"
```
\item[2023] \tab{}\enquote{Title} at the Venue. University, Location. October 13.
```

### Ordinal Numbers
`\nth{5}` should be used instead of 5th. This works for an `x`.

### Bold / Italics
Text should be bolded using `\textbf{Text here}`. `\textit{Text here}` will italicize text.
