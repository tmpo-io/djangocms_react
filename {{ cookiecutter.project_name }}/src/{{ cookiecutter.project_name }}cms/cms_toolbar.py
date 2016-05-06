# -*- coding: UTF-8 -*-
# --------------------

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool

'''
@toolbar_pool.register
class NameToolbar(CMSToolbar):

    def populate(self):

        arees_menu = self.toolbar.get_or_create_menu(
            'arees-app', _('Arees')
        )
        area_menu = arees_menu.get_or_create_menu(
            'area_menu',
            _('Area'),
        )
        url = reverse('admin:arees_area_changelist')
        area_menu.add_sideframe_item(_('List'), url=url)

        url = reverse('admin:arees_area_add')
        area_menu.add_modal_item(_('Add'), url=url)
'''
