"""Exact font (subset) per glyph position, read from the content stream with pdfminer."""
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFTextDevice
from pdfminer.pdfpage import PDFPage

class _Dev(PDFTextDevice):
    def __init__(self, rsrc):
        super().__init__(rsrc); self.items = []
    def render_char(self, matrix, font, fontsize, scaling, rise, cid, ncs, graphicstate):
        self.items.append((matrix[4], matrix[5], font.fontname))
        return font.char_width(cid) * fontsize * scaling

def page_fontmaps(path):
    """-> list per page of [(x, y_top_based, fontname)]"""
    rsrc = PDFResourceManager(caching=True); out = []
    with open(path, 'rb') as fp:
        for page in PDFPage.get_pages(fp):
            dev = _Dev(rsrc); PDFPageInterpreter(rsrc, dev).process_page(page)
            h = page.mediabox[3] - page.mediabox[1]
            out.append([(x - page.mediabox[0], h - (y - page.mediabox[1]), f) for x, y, f in dev.items])
    return out
