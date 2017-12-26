import os
import os.path 
from pprint import pprint
import re
import sys


DNI_NIE_REGEX = re.compile(r"[XYZ0-9]\d{7}[A-Z]")
NOMBRE_REGEX = re.compile(r"^Nombre\n\n(.+)\n\n(.+)\n\n(.+)", re.M)
CENTRO_ORDEN_REGEX = re.compile(r"\d{1,2}\n\n(.+)\n", re.M)

CHOICES_HORARIO = {
    "Horario de mañana": "M",
    "Horario de tarde": "T",
}


"""
Las páginas autogeneradas de preferencias tienen nombres diferentes
para ciertos emplazamientos (centros) que difieren de aquellos
utilizados para la administración, en caso de que los nombres difieran
se usan las siguientes substituciones
"""
a = "a"
CHOICES_CENTRO = {
 "Edificio de Servicios al Alumnado de Anchieta": "Edificio de servicios al alumnado de Anchieta (bajo supervisión de la "
 "OSL)",
 "Edificio de Servicios al Alumnado de Guajara": "Edificio de servicios al alumnado de Guajara (bajo supervisión de la OSL)",
 a: "Escuela Superior de Ingeniería y Tecnología",
 a: "Extensión de Enfermería en la isla de La Palma",
 "Facultad de Derecho/Sección de Ciencias Políticas y Sociales": "Facultad de Derecho / Sección de Ciencias Políticas y Sociales",
 a: "Facultad de Economía, Empresa y Turismo ",
 a: "Facultad de Economía, Empresa y Turismo (Campus del Sur, Adeje)",
 a: "Facultad de Educación",
 "Oficina del Software Libre": "Escuela Superior de Ingeniería y Tecnología (bajo supervisión de la OSL)",
 a: "Sección de Arquitectura Técnica",
 a: "Sección de Bellas Artes",
 a: "Sección de Biología",
 a: "Sección de Ciencias de la Información",
 a: "Sección de Farmacia",
 a: "Sección de Filología",
 a: "Sección de Filosofía",
 "Sección de Física/Sección Matemáticas": "Sección de Física / Sección de Matemáticas",
 a: "Sección de Geografía e Historia",
 a: "Sección de Ingeniería Agraria",
 a: "Sección de Medicina, Enfermería y Fisioterapia",
 a: "Sección de Náutica, Máquinas y Radioelectrónica Naval",
 a: "Sección de Psicología y Logopedia",
 a: "Sección de Química"
}


def txt_filter(filename):
    return filename[-4:] == ".txt"


def parser(relative_txt_path: str) -> dict:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    TXT_FILE_DIR = os.path.join(BASE_DIR, relative_txt_path)
    file_names = list(filter(txt_filter, [os.path.join(TXT_FILE_DIR, f) for f in os.listdir(TXT_FILE_DIR)]))

    info_dict = {}

    # Construímos el diccionario de preferencias
    for file_name in file_names:
        alu_dict = {}
        with open(file_name, "r") as f:
            file_content = f.read()
            a = DNI_NIE_REGEX.search(file_content)
            dni = a.group(0)
            nombre_apellidos = NOMBRE_REGEX.search(file_content)
            nombre = nombre_apellidos.group(3)
            apellido1 = nombre_apellidos.group(1)
            apellido2 = nombre_apellidos.group(2)
            alu_dict["nombre"] = nombre
            alu_dict["apellido1"] = apellido1
            alu_dict["apellido2"] = apellido2
            preferencias = []
            for found in CENTRO_ORDEN_REGEX.findall(file_content):
                if "Página" not in found:
                    try:
                        centro, horario = found.split(". ")
                        if centro in CHOICES_CENTRO:
                            centro = CHOICES_CENTRO[centro]
                        preferencias.append({"centro": centro, "horario": CHOICES_HORARIO[horario]})
                    except Exception as e:
                        pass
            alu_dict["preferencias"] = preferencias[:-1]
            info_dict[dni] = alu_dict
            
    pprint(info_dict, width=160)


if __name__ == "__main__":
    parser(sys.argv[1])

