import sys, re, ast

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/apply_full_100_accurate_images.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
fixed_count = 0

for idx, line in enumerate(lines):
    # Match key-value string lines like:
    #         'title': 'some text here',
    # or      'subtitle': 'some text',
    # Note: the key is in single quotes, colon, then value in single quotes ending with ',
    m = re.match(r"^(\s+'[a-zA-Z_]+':\s*)'(.*)'(,?)\s*$", line)
    if m:
        prefix = m.group(1)
        val = m.group(2)
        suffix = m.group(3)
        # Check if val has unescaped single quotes
        # Replace unescaped single quotes with \' or convert outer quotes to json/triple or escape
        # Better: let's replace inner unescaped ' with \'
        # But wait, what if val already has \' or ""?
        # A clean way: replace any ' that is not preceded by \ with \'
        new_val = re.sub(r"(?<!\\)'", r"\'", val)
        if new_val != val:
            fixed_count += 1
            line = f"{prefix}'{new_val}'{suffix}\n"
    new_lines.append(line)

new_content = ''.join(new_lines)
try:
    ast.parse(new_content)
    print(f"Fixed {fixed_count} lines! AST parse succeeded.")
    with open('scratch/apply_full_100_accurate_images.py', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Saved scratch/apply_full_100_accurate_images.py successfully!")
except SyntaxError as e:
    print(f"Still syntax error at line {e.lineno}: {e.msg}")
    err_lines = new_content.splitlines()
    print("Err line:", err_lines[e.lineno - 1])
