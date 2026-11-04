# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('js/translations.js', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace("Intake 127 • JMC", "Term 127 • BCTT")
text = text.replace("Intake 127", "Term 127")

with open('js/translations.js', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated js/translations.js: replaced JMC and Intake with BCTT and Term 127!")
