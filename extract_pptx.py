import zipfile, xml.etree.ElementTree as ET
def extract_text_from_pptx(pptx_file):
    try:
        with zipfile.ZipFile(pptx_file, 'r') as zf:
            slide_files = [f for f in zf.namelist() if f.startswith('ppt/slides/slide') and f.endswith('.xml')]
            slide_texts = {}
            for sf in slide_files:
                slide_num = int(''.join(filter(str.isdigit, sf.split('/')[-1])))
                xml_content = zf.read(sf)
                tree = ET.fromstring(xml_content)
                namespaces = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}
                texts = [node.text for node in tree.findall('.//a:t', namespaces) if node.text]
                slide_texts[slide_num] = ' '.join(texts)
            for num in sorted(slide_texts.keys()):
                print(f'Slide {num}:\n{slide_texts[num]}\n')
    except Exception as e:
        print('Error:', e)

extract_text_from_pptx('/Users/shivangigautam/Pablo/dr_sharma/Website.pptx')
