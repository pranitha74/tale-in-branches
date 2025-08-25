import glob, re
from pathlib import Path


root = Path(__file__).resolve().parents[1]
book_path = root / 'book.html'
chapters_dir = root / 'chapters'


chapters = sorted(chapters_dir.glob('*.html'))
parts = []
for p in chapters:
parts.append(p.read_text(encoding='utf-8').strip())


injected = "\n\n".join(parts)
html = book_path.read_text(encoding='utf-8')


new_html = re.sub(
r"<!-- ✨ CHAPTERS-START -->.*?<!-- ✨ CHAPTERS-END -->",
f"<!-- ✨ CHAPTERS-START -->\n{injected}\n<!-- ✨ CHAPTERS-END -->",
html,
flags=re.S,
)
book_path.write_text(new_html, encoding='utf-8')
print(f"Injected {len(chapters)} chapter(s) into book.html")
