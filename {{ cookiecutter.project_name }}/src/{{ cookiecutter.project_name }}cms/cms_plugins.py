# -*- coding: UTF-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

'''
class SectionPlugin(CMSPluginBase):
    model = Section
    name = _("Landing Section")
    allow_children = True
    render_template = 'cms/plugins/section.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance, 'placeholder': placeholder, })
        return context


plugin_pool.register_plugin(SectionPlugin)
'''
