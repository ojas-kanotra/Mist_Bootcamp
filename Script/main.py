def page_maker(lang):
    file = open(f'../{lang}.html', "w")
    file.write(f"""
    <!DOCTYPE html>
    <head>
        <title>WebDev</title>
        <link rel="stylesheet" href="style.css">
        <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@300;400;500;600;700&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@100;300;400;500;700&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=VT323&display=swap" rel="stylesheet">
    </head>
    <body>
        <h1>Let us learn '{lang}'</h1>
        <hr><hr>""")

    doc = open(f'../{lang}.txt', "r").readlines()
    for line in range(len(doc)-1):
        if "===" in doc[line+1]:
            file.write(f'<button class="topic"> {doc[line][0:len(doc[line])-1]} </button>\n')
        elif "===" in doc[line] or doc[line].strip() == '':
            continue
        else:
            doc[line] = doc[line].replace("&", "&amp;")
            doc[line] = doc[line].replace("<", "&lt;")
            doc[line] = doc[line].replace(">", "&gt;")
            file.write(f'<button class="command" title="{doc[line][48:]}"><pre><code> {doc[line][0:48].strip()} </code></pre></button>\n')
    file.write("</body></html>")

page_maker("HTML")
page_maker("CSS")
page_maker("JAVASCRIPT")