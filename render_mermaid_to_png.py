import sys
import os
import json
import asyncio
from pathlib import Path

try:
    from pyppeteer import launch
except ImportError:
    print("pyppeteer is required. Install with: pip install pyppeteer")
    sys.exit(1)

MERMAID_CDN = "https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
  <meta charset=\"utf-8\">
  <script src=\"{mermaid_cdn}\"></script>
  <style>
    body {{ margin: 0; padding: 0; }}
    #container {{ display: flex; justify-content: center; align-items: center; height: 100vh; }}
  </style>
</head>
<body>
  <div id=\"container\">
    <div class=\"mermaid\" id=\"mermaid\"></div>
  </div>
  <script>
    mermaid.initialize({{ startOnLoad: false }});
    const code = `{mermaid_code}`;
    mermaid.render('theGraph', code, (svgCode) => {{
      document.getElementById('mermaid').innerHTML = svgCode;
    }});
  </script>
</body>
</html>
"""

def read_puppeteer_config():
    config_path = Path('puppeteer-config.json')
    if config_path.exists():
        with open(config_path, 'r') as f:
            return json.load(f)
    return {}

def main():
    if len(sys.argv) < 2:
        print("Usage: python render_mermaid_to_png.py <path-to-file.mmd>")
        sys.exit(1)
    mmd_path = Path(sys.argv[1])
    if not mmd_path.exists():
        print(f"File not found: {mmd_path}")
        sys.exit(1)
    output_png = mmd_path.with_suffix('.png')
    with open(mmd_path, 'r', encoding='utf-8') as f:
        mermaid_code = f.read().replace('`', '\\`').replace('\\', '\\\\')
    html = HTML_TEMPLATE.format(mermaid_cdn=MERMAID_CDN, mermaid_code=mermaid_code)
    tmp_html = mmd_path.parent / (mmd_path.stem + '_tmp_render.html')
    with open(tmp_html, 'w', encoding='utf-8') as f:
        f.write(html)
    puppeteer_config = read_puppeteer_config()
    async def render():
        browser = await launch(headless=True, args=puppeteer_config.get('args', []))
        page = await browser.newPage()
        await page.goto(f'file://{tmp_html}', {'waitUntil': 'networkidle0'})
        await page.waitForSelector('svg')
        element = await page.querySelector('svg')
        bounding_box = await page.evaluate('(el) => { const r = el.getBoundingClientRect(); return {x: r.x, y: r.y, width: r.width, height: r.height}; }', element)
        await element.screenshot({
            'path': str(output_png),
            'omitBackground': True,
            'clip': bounding_box
        })
        await browser.close()
        os.remove(tmp_html)
        print(f"PNG generated: {output_png}")
    try:
        asyncio.get_event_loop().run_until_complete(render())
    except Exception as e:
        print(f"Error rendering Mermaid diagram: {e}")
        if tmp_html.exists():
            os.remove(tmp_html)
        sys.exit(1)

if __name__ == '__main__':
    main() 