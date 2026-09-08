import re

with open('src/App.vue', 'r') as f:
    content = f.read()

old_str = '<div v-if="activeMarker && activeMarker.id !== 4 && activeMarker.id !== 14 && activeMarker.id !== 13 && activeMarker.id !== 1" class="marker-modal-backdrop" @click.self="activeMarker = null">'
new_str = '<div v-if="activeMarker && activeMarker.htmlContent" class="marker-modal-backdrop" @click.self="activeMarker = null">'

content = content.replace(old_str, new_str)

with open('src/App.vue', 'w') as f:
    f.write(content)

