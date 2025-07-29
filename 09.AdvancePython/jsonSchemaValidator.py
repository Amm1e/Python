import json
import jsonschema
from jsonschema import Draft4Validator

# Replace this with your full schema
with open("Schema.jsv","rt")as f:
    schema = json.load(f)
    # Validate the schema
    try:
        Draft4Validator.check_schema(schema)
        print("✅ Schema is valid.")
    except jsonschema.exceptions.SchemaError as e:
        print("❌ Schema is invalid:")
        print(e)
