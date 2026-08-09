import io

# Warm cream palette
BG_CREAM = '#FBF3E3'          # warm cream background
GLASS_CREAM = 'rgba(255, 250, 235, 0.9)'   # glass card cream

# (file, old_string, new_string) replacements
repls = [
    # ---- arduinoexpo.html ----
    ('public/arduinoexpo.html',
     "[data-theme='light'] body {\n            background-color: #f8f8f8 !important;",
     "[data-theme='light'] body {\n            background-color: " + BG_CREAM + " !important;"),
    ('public/arduinoexpo.html',
     "[data-theme='light'] .glass-card-neon {\n            background: rgba(255, 255, 255, 0.8) !important;",
     "[data-theme='light'] .glass-card-neon {\n            background: " + GLASS_CREAM + " !important;"),

    # ---- jso.html ----
    ('public/jso.html',
     '--bg-primary: #f8f8f8;',
     '--bg-primary: ' + BG_CREAM + ';'),
    ('public/jso.html',
     '--glass: rgba(255, 255, 255, 0.95);',
     '--glass: ' + GLASS_CREAM + ';'),

    # ---- modelothon.html ----
    ('public/modelothon.html',
     '--bg-deep:#f5f5f5;',
     '--bg-deep:' + BG_CREAM + ';'),
    ('public/modelothon.html',
     '--glass:rgba(0,0,0,0.05);',
     '--glass:' + GLASS_CREAM + ';'),

    # ---- exquizit.html ----
    ('public/exquizit.html',
     '--bg-deep: #f8f8f8;',
     '--bg-deep: ' + BG_CREAM + ';'),
    ('public/exquizit.html',
     '--glass: rgba(255, 255, 255, 0.9);',
     '--glass: ' + GLASS_CREAM + ';'),

    # ---- mun.html ----
    ('public/mun.html',
     '--bg-primary:#f8f8f8;',
     '--bg-primary:' + BG_CREAM + ';'),
    ('public/mun.html',
     '--bg-secondary:rgba(0,0,0,0.05);',
     '--bg-secondary:' + GLASS_CREAM + ';'),
]

for fname, old, new in repls:
    c = io.open(fname, encoding='utf-8').read()
    if old in c:
        c = c.replace(old, new, 1)
        io.open(fname, 'w', encoding='utf-8').write(c)
        print('OK  ', fname, '->', new.split(';')[0])
    else:
        print('MISS', fname, 'pattern not found:', old[:60])
