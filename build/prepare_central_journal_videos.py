from pathlib import Path
import re

path = Path('index.html')
text = path.read_text(encoding='utf-8')

# Central-site exception only: course sites retain Certificates.
text = text.replace(
    '<a href="#certificates" data-view="certificates">✦<br>Certificates</a>',
    '<a href="#journal" data-view="journal">✎<br>Journal</a><a href="#videos" data-view="videos">▶<br>Videos</a>',
    1,
)

css = '''
.central-course-links{grid-column:2;grid-row:1/3;display:flex;flex-wrap:wrap;justify-content:flex-end;gap:8px;align-self:center}.central-course-links .button{grid-column:auto;grid-row:auto;margin:0}.central-course-links .button.secondary-link{background:#f2e7cf;color:var(--ink)}.media-list{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px;margin-top:24px}.media-card{border:1px solid var(--line);border-top:6px solid var(--accent,var(--burgundy));border-radius:16px;padding:22px;background:#fff}.media-card h2{margin:0 0 8px}.media-card p{color:var(--muted)}.media-card .button{margin:5px 7px 0 0}@media(max-width:900px){.central-course-links{grid-column:1;grid-row:auto;justify-content:flex-start}.media-list{grid-template-columns:1fr}}
'''
if '.central-course-links{' not in text:
    text = text.replace('</style>', css + '</style>', 1)

faith_old = '<a class="button" href="https://wally189.github.io/The-Faith-Experiment/">Open course →</a>'
faith_new = '<div class="central-course-links"><a class="button" href="https://wally189.github.io/The-Faith-Experiment/">Course →</a><a class="button secondary-link" href="#journal">Journal →</a><a class="button secondary-link" href="#videos">Videos →</a><a class="button secondary-link" href="https://wally189.github.io/The-Faith-Experiment/#certificates">Certificates →</a></div>'
latin_old = '<a class="button" href="https://wally189.github.io/the-latin-experiment/">Open course →</a>'
latin_new = '<div class="central-course-links"><a class="button" href="https://wally189.github.io/the-latin-experiment/">Course →</a><a class="button secondary-link" href="#journal">Journal →</a><a class="button secondary-link" href="#videos">Videos →</a><a class="button secondary-link" href="https://wally189.github.io/the-latin-experiment/#certificates">Certificates →</a></div>'
text = text.replace(faith_old, faith_new, 1).replace(latin_old, latin_new, 1)

replacement = '''<section class="view" id="journal" data-section hidden>
<h1>Journal</h1>
<p class="lede">The journal records the real learning journey across The Catholic Experiment: work completed, questions raised, corrections made and reflections on the method.</p>
<div class="notice"><strong>Programme record, not assessment:</strong> certificates remain on each individual course site. This page gathers the wider learning record.</div>
<div class="media-list">
<article class="media-card" style="--accent:var(--blue)"><span class="status active">Faith and Formation</span><h2>The Faith Experiment journal</h2><p>Entries relating to doctrine, formation, source checking and the development of the Faith course.</p><a class="button" href="https://wally189.github.io/The-Faith-Experiment/#journal">Open Faith journal →</a><a class="button" href="https://wally189.github.io/The-Faith-Experiment/">Open course →</a></article>
<article class="media-card" style="--accent:var(--burgundy)"><span class="status active">Sacred Languages</span><h2>The Latin Experiment journal</h2><p>Entries recording lessons, handwriting, vocabulary, grammar, corrections and progress through the Latin course.</p><a class="button" href="https://wally189.github.io/the-latin-experiment/#journal">Open Latin journal →</a><a class="button" href="https://wally189.github.io/the-latin-experiment/">Open course →</a></article>
</div>
</section>
<section class="view" id="videos" data-section hidden>
<h1>Videos</h1>
<p class="lede">Videos accompany the written record by showing the work, explaining the method and reflecting honestly on progress. They support the courses but do not replace the books, lessons or handwritten study.</p>
<div class="media-list">
<article class="media-card" style="--accent:var(--blue)"><span class="status active">Faith and Formation</span><h2>The Faith Experiment videos</h2><p>Video reflections and demonstrations connected with the Faith course will be collected here as they are published.</p><a class="button" href="https://wally189.github.io/The-Faith-Experiment/#videos">Open Faith videos →</a><a class="button" href="https://wally189.github.io/The-Faith-Experiment/">Open course →</a></article>
<article class="media-card" style="--accent:var(--burgundy)"><span class="status active">Sacred Languages</span><h2>The Latin Experiment videos</h2><p>Lesson demonstrations, reading practice and reflections connected with the Latin course will be collected here.</p><a class="button" href="https://wally189.github.io/the-latin-experiment/#videos">Open Latin videos →</a><a class="button" href="https://wally189.github.io/the-latin-experiment/">Open course →</a></article>
</div>
</section>'''

pattern = re.compile(r'<section class="view" id="certificates" data-section hidden>.*?</section>', re.S)
text, count = pattern.subn(replacement, text, count=1)
if count != 1:
    raise RuntimeError(f'Expected one Certificates section, replaced {count}')

required = ['data-view="journal"', 'data-view="videos"', 'id="journal"', 'id="videos"', 'The Faith Experiment/#certificates', 'the-latin-experiment/#certificates']
missing = [item for item in required if item not in text]
if missing:
    raise RuntimeError(f'Missing expected central navigation content: {missing}')

path.write_text(text, encoding='utf-8')
