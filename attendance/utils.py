import os
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.conf import settings

from xhtml2pdf import pisa

#this code fetches static link for media like images to display them in the pdf
def fetch_resources(uri, rel):
    mUrl = settings.MEDIA_URL
    mRoot = settings.MEDIA_ROOT
    sUrl = settings.STATIC_URL
    sRoot = settings.STATIC_ROOT

    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri

    if not os.path.isfile(path):
        raise Exception('Media uri must start with %s or %s' %(sUrl, mUrl))
    return path

    


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    response = HttpResponse(content_type='application/pdf')
    response['content-Disposition'] ='attachment;'
    # result = BytesIO()

    pdf = pisa.CreatePDF(
        html,dest=response, link_callback=fetch_resources)
    if pdf.err:
        return HttpResponse('we had some errors')
    return response
  
    # #this part creates the pdf
    # pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), dest=result, 
    #                                                      encoding='UTF-8', 
    #                                                      link_callback=fetch_resources,
    #                                                        path='attendance/static')
    # if not pdf.err:
    #     return HttpResponse(result.getvalue(), content_type='application/pdf')
    # return None