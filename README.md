# WebDev_ka_Adda - Interactive Web Development Cheat Sheets

A comprehensive, beginner-friendly interactive website featuring cheat sheets for **HTML**, **CSS**, and **JavaScript**. Perfect for absolute beginners learning web development!

## What This Project Does

This project creates an interactive learning platform where beginners can:
- **Learn web development fundamentals** in a structured, progressive way
- **Hover over code examples** to see detailed explanations via tooltips
- **Navigate easily** between HTML, CSS, and JavaScript concepts
- **Reference commands quickly** with clear, simple descriptions

## Project Structure

### Core Files
- **`index.html`** - Main homepage with navigation to all cheat sheets
- **`style.css`** - Styling and animations for the entire website
- **`HTML.html`**, **`CSS.html`**, **`JAVASCRIPT.html`** - Generated interactive cheat sheet pages

### Content Files  
- **`HTML.txt`** - HTML commands
- **`CSS.txt`** - CSS properties
- **`JAVASCRIPT.txt`** - JavaScript concepts 

### Generation Script
- **`main.py`** - Python script that converts .txt files into interactive HTML pages

## How It Works

1. **Content Creation**: Knowledge is stored in structured .txt files with:
   - First line: Topic description
   - Lines above `====`: Section titles
   - Each command: Spaced exactly 48 characters from start for descriptions

2. **HTML Generation**: `main.py` processes .txt files and converts. 
    - Currently, you need to run the `main.py` locally in order to get the HTML JAVASCRIPT CSS files updated. 


3. **Interactive Display**: Generated HTML files provide:
   - Clean, professional interface
   - Instant access to explanations
   - Easy navigation between concepts

## Updating Content

To modify or add content:
1. Edit the respective `.txt` file (HTML.txt, CSS.txt, or JAVASCRIPT.txt)
2. Run `main.py` to regenerate the HTML files
3. Refresh your browser to see changes

---

### Check out the website below: 

https://ojas-kanotra.github.io/Mist_Bootcamp/HTML.html

---

### Thanks you :>
