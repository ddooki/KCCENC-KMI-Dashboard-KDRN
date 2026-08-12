import base64

with open('construction_compliance_dashboard.html', 'rb') as f:
    raw = f.read()

b64 = base64.b64encode(raw).decode('utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Replace content inside <script id="gunchuk-doc" type="text/plain">...</script>
import re
index_content = re.sub(
    r'<script id="gunchuk-doc" type="text/plain">.*?</script>',
    f'<script id="gunchuk-doc" type="text/plain">\n{b64}\n</script>',
    index_content,
    flags=re.DOTALL
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_content)

print('Embedded updated construction_compliance_dashboard into index.html successfully!')
