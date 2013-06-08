from zope.formlib import form
from zope.interface import implements

from plone.app.portlets.portlets import base
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFPlone import PloneMessageFactory as _

from interfaces import IAccreditationPortlet

class Assignment(base.Assignment):
    implements(IAccreditationPortlet)

class AddForm(base.AddForm):
    form_fields = form.Fields(IAccreditationPortlet)
    label = _(u"Add Accreditation Portlet")
    description = _(u"This portlet displays an Accreditation logo.")
    
    def create(self, data):
        return Assignment()

class Renderer(base.Renderer):
    _template = ViewPageTemplateFile('portlet.pt')

    def __init__(self, *args):
        base.Renderer.__init__(self, *args)

    def render(self):
        return self._template()
