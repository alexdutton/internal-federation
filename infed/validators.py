import os.path

import defusedxml.lxml
import lxml.etree
from django.core.exceptions import ValidationError, SuspiciousOperation


class LocalResolver(lxml.etree.Resolver):
    file_mappings = {
        'http://www.w3.org/TR/2002/REC-xmldsig-core-20020212/': '/usr/share/xml/pskc/',
        'http://www.w3.org/TR/2002/REC-xmlenc-core-20021210/': '/usr/share/xml/pskc/',
        'http://www.w3.org/2001/xml.xsd': '/usr/share/xml/xml.xsd',
        '/usr/share/xml/shibboleth/xmldsig-core-schema.xsd': '/usr/share/xml/xmltooling/xmldsig-core-schema.xsd',
    }

    def resolve(self, url, id, context):
        print("Resolving", url, id, context)
        for url_prefix, path_prefix in self.file_mappings.items():
            if url_prefix.endswith('/') and url.startswith(url_prefix):
                path = os.path.join(path_prefix, url[len(url_prefix):])
                if not os.path.normpath(path).startswith(path_prefix):
                    raise SuspiciousOperation("Attempting to load schema from outside path")
            elif not url_prefix.endswith('/') and url == url_prefix:
                path = path_prefix
            else:
                continue

            print("Found", path)
            return self.resolve_filename(path, context)


def validate_metadata(xml):
    schema_parser = lxml.etree.XMLParser()
    schema_parser.resolvers.add(LocalResolver())

    with open('/usr/share/xml/opensaml/saml-schema-metadata-2.0.xsd', 'rb') as f:
        schema = lxml.etree.parse(f, parser=schema_parser)
        schema = lxml.etree.XMLSchema(schema)

    try:
        xml = defusedxml.lxml.fromstring(xml, parser=lxml.etree.XMLParser(schema=schema,
                                                                          resolve_entities=False))
    except lxml.etree.XMLSyntaxError as e:
        raise ValidationError(str(e)) from e

    if xml.tag != '{urn:oasis:names:tc:SAML:2.0:metadata}EntityDescriptor':
        raise ValidationError("Root element must be md:EntityDescriptor")