import yaml, json, re

with open("cv.yaml", 'r') as f:
    cvdata = yaml.safe_load(f)

print(json.dumps(cvdata, indent=1, default=str))

def clean_text(t):
    ## italics
    t = re.sub("<i>", "\\\\textit{", t)
    t = re.sub("</i>", "}", t)
    return t

tex_content = []
tex_content.append("""\\documentclass{article}
\\usepackage[T1]{fontenc}
\\usepackage[utf8]{inputenc}
\\usepackage[USenglish]{babel}
\\usepackage[super]{nth}
\\usepackage{datetime}
\\usepackage{enumitem}
\\usepackage{geometry}
\\usepackage[strict,autostyle]{csquotes}
\\usepackage[final, tracking=true, kerning=true]{microtype}
\\usepackage{tabto}
\\usepackage{hyperref}
\\usepackage{soul}
\\usepackage[style=iso]{datetime2}
\\usepackage{fancyhdr}


\\geometry{
    letterpaper,
    left=1.5cm,
    right=1.5cm,
    top=2cm,
    bottom=2cm
 }
 
\\pagenumbering{gobble}
\\setlength{\\parindent}{0pt}

\\hypersetup{
    colorlinks  = true,
    urlcolor    = blue,
    citecolor   = black,
    linkcolor   = blue,
    pdfauthor   = {cv-resume automated tool},
    pdftitle    = {Curriculum Vitae},
    pdfsubject  = {Curriculum Vitae},
    pdfpagemode = UseNone
}

% how far to tab for list items with left-aligned date: different fonts need different widths
\\newcommand{\\listtabwidth}{1.7cm}

% define space between list items
\\newcommand{\\listitemspace}{0.25em}


\\newcommand\\blfootnote[1]{%
  \\begingroup
  \\renewcommand\\thefootnote{}\\footnote{#1}%
  \\addtocounter{footnote}{-1}%
  \\endgroup
}

% make unordered lists without bullets and use compact spacing
\\renewenvironment{itemize}
{\\begin{list}{}{\\setlength{\\leftmargin}{0em}
                \\setlength{\\parskip}{0em}
                \\setlength{\\itemsep}{\\listitemspace}
                \\setlength{\\parsep}{\\listitemspace}}}
{\\end{list}}

% make tabbed lists so content is left-aligned next to years
\\TabPositions{\\listtabwidth}
\\newlist{tablist}{description}{3}
\\setlist[tablist]{leftmargin=\\listtabwidth,
    labelindent=0em,
    topsep=0em,
    partopsep=0em,
    itemsep=\\listitemspace,
    parsep=\\listitemspace,
    font=\\normalfont}

\\newdateformat{monthyeardate}{\\monthname[\\THEMONTH] \\THEYEAR}

\\fancypagestyle{firstpage}
{
    \\fancyhead[L]{Curriculum Vitae}
    \\fancyhead[R]{last revised \\today}
}

\\begin{document}
\\thispagestyle{firstpage}
\\raggedright{}
""")

## NAME
tex_content.append("""
\\huge{{\\textbf{{{0}}}}}
\\normalsize
""".format(cvdata['header']['name']))

## AFFILIATION
tex_content.append(
"""
\\vspace{{.75em}}
\\begin{{minipage}}[t]{{0.700\\textwidth}}
    {}\\\\
    {} \\\\
    {}
\\end{{minipage}}
\\begin{{minipage}}[t]{{0.275\\textwidth}}
    \\flushright{{}}
    {}\\\\
    {}\\\\
    {}
\\end{{minipage}}
""".format(
    cvdata['header']['bio'][0],
    cvdata['header']['bio'][1],
    cvdata['header']['bio'][2],
    cvdata['header']['email'],
    cvdata['header']['phone'],
    cvdata['header']['website']
)
)

## EDUCATION
tex_content.append("\\section*{\\normalsize{EDUCATION}}\n\\begin{tablist}\n" + "\n".join(["\t\item[{}] \\tab{{}}{}".format(eduitem, clean_text('\\newline{}'.join(cvdata['education'][eduitem]))) for eduitem in cvdata['education']]) + "\n\\end{tablist}\n")


tex_content.append("""
\\end{document}
""")
with open("generated_main.tex", "w") as f:
    f.writelines(tex_content)
