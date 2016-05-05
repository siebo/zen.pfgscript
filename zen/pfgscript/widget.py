# -*- coding: utf-8 -*-


from Products.Archetypes.Widget import TypesWidget
from Products.Archetypes.Registry import registerWidget
from AccessControl import ClassSecurityInfo


class JSWidget(TypesWidget):
    """ Widget that display a JS on edit
    """

    _properties = TypesWidget._properties.copy()
    _properties.update(
        {'macro': 'widget_js',
         })

    security = ClassSecurityInfo()

# Register the widget with Archetypes
registerWidget(JSWidget,
               title = 'JavaScript widget',
               description= ('Renders a JavaScript on edit',),
               used_for = ('Products.Archetypes.Field.TextField',)
               )
