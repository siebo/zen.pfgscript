# -*- coding: utf-8 -*-

from Products.CMFCore.utils import getToolByName
from zen.pfgscript import logger


def setupVarious(context):
    if context.readDataFile('zen.pfgscript_various.txt') is None:
        return
    portal = context.getSite()
    setup_type(portal)


def setup_type(portal):
    types = getToolByName(portal, 'portal_types')
    if 'FormFolder' in types.objectIds():
        folder = types['FormFolder']
        allowed_content_types = set(folder.allowed_content_types)
        allowed_content_types.add('ScriptField')
        folder.allowed_content_types = tuple(allowed_content_types)
        logger.info("ScriptField registered as PloneFormGen possible field")
