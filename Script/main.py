def page_maker(lang):
    file = open(f'{lang}.html', "w")
    file.write(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <title>WebDev_Ka_Adda</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@100;300;400;500;700&display=swap" rel="stylesheet">
</head>
<body class="bg-black text-white" style="font-family: 'Fira Code', monospace;">
<nav class="m-6">
  <div class="bg-gray-800 w-full flex justify-between items-center px-6 py-4 rounded">
    <a href="#">
      <img src="logo.png" class="h-16 w-auto" alt="Logo">
    </a>
    <div class="flex gap-x-12">
      <a href="#" class="font-semibold text-white text-lg">Introduction</a>
      <a href="#" class="font-semibold text-white text-lg">About Me</a>
      <a href="#" class="font-semibold text-white text-lg">Other Websites</a>
      <a href="#" class="font-semibold text-white text-lg">Company</a>
    </div>
    <a href="#" class="font-semibold text-white text-lg">Welcome, User</a>
  </div>
</nav>

<div class="text-center">
  <h1 class="font-bold text-white text-6xl" style="font-family: 'Fira Code', 'JetBrains Mono', monospace;"> {lang} </h1>
</div>
<BR>
    """)
    doc = open(f'Script/{lang}.txt', "r").readlines()
    for line in range(len(doc)-1):
        if line == 0:
            file.write(f'''
    <p class="text-white text-center"> {doc[line].strip()} </p>
    ''')
        elif "===" in doc[line+1]:
            heading = doc[line].strip().replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            file.write(f'''
    <br><br>
    <div class="flex items-center" role="separator" aria-hidden="true">
      <span class="h-px flex-1 bg-gray-500"></span>
      <span class="shrink-0 px-4 text-white font-semibold text-center">{heading}</span>
      <span class="h-px flex-1 bg-gray-500"></span>    
    </div>
    <br><br>
    ''')
        elif "===" in doc[line] or doc[line].strip() == '':
            continue
        else:
            escaped_line = doc[line].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            code_part = escaped_line[:48].strip()
            desc_part = escaped_line[48:].strip()
            file.write(f'''
    <div class="flex flex-row p-4 bg-gray-900 border border-gray-700 rounded-lg mb-2">
        <div class="basis-1/3"><code class="bg-gray-800 p-2 rounded text-green-400 font-mono">{code_part}</code></div>
        <div class="basis-2/3 text-gray-300 pl-4">{desc_part}</div> 
    </div>
''')

    file.write('''
<footer class="mt-8 w-full py-4 border-t border-gray-700 bg-gray-800">
    <div class="max-w-4xl mx-auto text-center">
      <p class="text-sm text-gray-400">Generated from txt files | <a href="index.html" class="text-blue-400 hover:text-blue-300">Back to Home</a></p>
    </div>
</footer>
''')
    file.write("</body></html>")

page_maker("HTML")
page_maker("CSS")
page_maker("JAVASCRIPT")