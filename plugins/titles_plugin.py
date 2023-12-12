from apispec.ext import marshmallow


class OpenAPITitleAppender(marshmallow.OpenAPIConverter):
    def schema2jsonschema(self, schema):
        json_schema = super(OpenAPITitleAppender, self).schema2jsonschema(schema)
        schema_name = schema.__class__.__name__
        if schema_name.endswith("Schema"):
            schema_name = schema_name[: -len("Schema")]
        json_schema["title"] = schema_name
        return json_schema


class TitlesPlugin(marshmallow.MarshmallowPlugin):
    Converter = OpenAPITitleAppender
