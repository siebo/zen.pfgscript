"""Definition of the Script Field content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content.base import registerATCT

from Products.PloneFormGen.content.fieldsBase import *
from Products.PloneFormGen import FGStringField
from Products.PloneFormGen.interfaces import IPloneFormGenField

from zen.pfgscript.interfaces import IScriptField
from zen.pfgscript.config import PROJECTNAME


class ScriptField(FGStringField):
    """Javascript Field"""
    implements(IPloneFormGenField, IScriptField)

    schema = BaseFieldSchemaStringDefault.copy()

    del schema['hidden']
    del schema['serverSide']

    # hide references & discussion
    finalizeFieldSchema(schema, folderish=True, moveDiscussion=False)

    # Standard content type setup
    portal_type = meta_type = 'ScriptField'
    archetype_name = 'Javascript Field'
    content_icon = 'PasswordField.gif'
    typeDescription= 'Javascript field'

    def __init__(self, oid, **kwargs):
        """ initialize class """

        BaseFormField.__init__(self, oid, **kwargs)

        # set a preconfigured field as an instance attribute.
        #
        # We use our own widget 
        self.fgField = StringField('fg_string_field',
            searchable=0,
            required=0,
            write_permission = View,
            validators=(),
            widget=PasswordWidget(
                macro='pfg_script',
                populate = True,
                postback = True,
            ),
        )

registerATCT(ScriptField, PROJECTNAME)
