"""Definition of the Script Field content type
"""

from zope.interface import implements
from Products.CMFCore import permissions
from AccessControl import ClassSecurityInfo
from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content.base import registerATCT
from Products.ATContentTypes.content.schemata import ATContentTypeSchema

from Products.PloneFormGen.content.fieldsBase import BaseFormField
from Products.PloneFormGen.content.fieldsBase import BaseFieldSchema
from Products.PloneFormGen.content.fieldsBase import finalizeFieldSchema
from Products.PloneFormGen.content.fieldsBase import BareFieldSchema
from Products.PloneFormGen.content.fields import PlainTextField
from Products.PloneFormGen.interfaces import IPloneFormGenField

from zen.pfgscript.interfaces import IScriptField
from zen.pfgscript.config import PROJECTNAME
from zen.pfgscript.widget import JSWidget


ScriptFieldSchema = BareFieldSchema.copy() + atapi.Schema((

    atapi.TextField(
        'scriptSource',
        searchable=0,
        required=1,
        default="""<script>
</script>
""",
        widget=atapi.TextAreaWidget(
            label=u'JavaScript source',
            ),

        )
    ))


class ScriptField(BaseFormField):
    """Javascript Field"""
    implements(IScriptField)

    security = ClassSecurityInfo()
    schema = ScriptFieldSchema.copy()

    # hide references & discussion
    finalizeFieldSchema(schema, folderish=True, moveDiscussion=False)

    # Standard content type setup
    portal_type = meta_type = 'ScriptField'
    archetype_name = 'JavaScript Field'
    content_icon = 'PasswordField.gif'
    typeDescription = 'JavaScript field'

    def __init__(self, oid, **kwargs):
        """ initialize class """

        BaseFormField.__init__(self, oid, **kwargs)

        # set a preconfigured field as an instance attribute
        self.fgField = PlainTextField(
            'fg_script_field',
            searchable=0,
            required=0,
            write_permission=permissions.View,
            validators=('isNotTooLong', ),
            default_content_type = 'text/plain',
            allowable_content_types = ('text/plain',),
            widget = JSWidget()
            )

    security.declareProtected(permissions.View, 'isBinary')
    def isBinary(self, key):
        return False

    security.declareProtected(permissions.View, 'getContentType')
    def getContentType(self, key=None):
        return 'text/plain'

registerATCT(ScriptField, PROJECTNAME)
