import os.path
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.conf import settings

from xhtml2pdf import pisa
def fetch_resources(uri, rel):
	sUrl = (settings.STATIC_URL, "")
	sRoot = settings.STATIC_ROOT
	path = os.path.join(sRoot, uri.replace(sUrl))
	return path
	


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
  
    #this part creates the pdf
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), dest=result, 
    													   encoding='UTF-8', 
    													   link_callback=fetch_resources)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None