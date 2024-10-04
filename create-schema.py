import yaml
import json
from genson import SchemaBuilder

# Leer archivo YAML
# Abre el archivo YAML y carga su contenido en una estructura de datos de Python.
with open('archivo.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

# Crear el generador de esquemas
# Inicializa un generador de esquemas JSON y añade el esquema base de JSON Schema Draft-07.
builder = SchemaBuilder()
builder.add_schema({"$schema": "http://json-schema.org/draft-07/schema#"})

# Añadir datos YAML al generador de esquemas
# Añade los datos del archivo YAML al generador de esquemas para construir el esquema JSON.
builder.add_object(yaml_data)

# Obtener el esquema JSON generado
# Convierte los datos añadidos en un esquema JSON.
json_schema = builder.to_schema()

# Función para añadir validaciones adicionales al esquema JSON
def add_validations(schema):
    # Verifica si el esquema tiene propiedades
    if "properties" in schema:
        # Itera sobre cada propiedad en el esquema
        for key, value in schema["properties"].items():
            # Añade validaciones para cadenas de texto
            if value["type"] == "string":
                value["minLength"] = 1  # Longitud mínima de la cadena
                value["maxLength"] = 255  # Longitud máxima de la cadena
                value["pattern"] = "^[a-zA-Z0-9_ ]*$"  # Patrón de ejemplo para la cadena
            # Añade validaciones para números
            elif value["type"] == "number":
                value["minimum"] = 0  # Valor mínimo permitido
                value["maximum"] = 10000  # Valor máximo permitido
            # Añade validaciones para listas
            elif value["type"] == "array":
                value["minItems"] = 1  # Número mínimo de elementos en la lista
                value["maxItems"] = 100  # Número máximo de elementos en la lista
                # Aplica validaciones a los elementos de la lista si existen
                if "items" in value:
                    add_validations(value["items"])
            # Añade validaciones para objetos (mapas)
            elif value["type"] == "object":
                # Llama recursivamente a la función para añadir validaciones a las propiedades del objeto
                add_validations(value)

# Añadir validaciones a la raíz del esquema
# Llama a la función para añadir validaciones adicionales al esquema JSON generado.
add_validations(json_schema)

# Formatear el esquema JSON para que sea más legible
# Convierte el esquema JSON en una cadena con formato legible, con indentación y claves ordenadas.
formatted_json_schema = json.dumps(json_schema, indent=4, sort_keys=True)

# Guardar el esquema JSON en un archivo
# Abre un archivo para escribir y guarda el esquema JSON formateado en él.
with open('esquema.json', 'w') as file:
    file.write(formatted_json_schema)

print("Esquema JSON generado y guardado en 'esquema.json'")
