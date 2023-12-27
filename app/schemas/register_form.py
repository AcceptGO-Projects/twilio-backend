from pydantic import BaseModel, EmailStr, constr

class RegisterForm(BaseModel):
    nombre: constr(strip_whitespace=True, min_length=1)
    correo_electronico: EmailStr
    pais: constr(strip_whitespace=True, min_length=2)
    telefono: constr(strip_whitespace=True, min_length=1)
    experiencia: constr(strip_whitespace=True)
    busqueda: constr(strip_whitespace=True)
    carrera: constr(strip_whitespace=True)
    mensaje: constr(strip_whitespace=True, min_length=1)
    acepta_notificaciones: bool
