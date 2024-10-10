## Explicación del Script

### Importación de Bibliotecas:
- **yaml**: Para leer y analizar archivos YAML.
- **json**: Para trabajar con datos JSON.
- **SchemaBuilder de genson**: Para construir esquemas JSON de manera incremental.

### Lectura del Archivo YAML:
- Abre el archivo `archivo.yaml` y carga su contenido en una estructura de datos de Python utilizando `yaml.safe_load`.

### Creación del Generador de Esquemas:
- Inicializa un generador de esquemas JSON (`SchemaBuilder`) y añade el esquema base de JSON Schema Draft-07.

### Añadir Datos YAML al Generador de Esquemas:
- Añade los datos del archivo YAML al generador de esquemas para construir el esquema JSON.

### Obtener el Esquema JSON Generado:
- Convierte los datos añadidos en un esquema JSON utilizando `builder.to_schema()`.

### Función para Añadir Validaciones Adicionales:
- Define una función `add_validations` que añade validaciones adicionales a las propiedades del esquema JSON.
- La función maneja diferentes tipos de datos (`string`, `number`, `array`, `object`) y añade validaciones específicas para cada tipo.

### Añadir Validaciones a la Raíz del Esquema:
- Llama a la función `add_validations` para añadir validaciones adicionales al esquema JSON generado.

### Formatear el Esquema JSON para que sea más Legible:
- Convierte el esquema JSON en una cadena con formato legible utilizando `json.dumps` con indentación y claves ordenadas.

### Guardar el Esquema JSON en un Archivo:
- Abre un archivo para escribir (`esquema.json`) y guarda el esquema JSON formateado en él.

Este script debería generar un esquema JSON detallado y legible a partir de un archivo YAML, incluyendo validaciones adicionales para diferentes tipos de datos.
