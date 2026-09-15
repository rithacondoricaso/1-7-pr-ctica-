class Persona:
        def __init__(self, nombre, edad):
                    self.__nombre = nombre
                            self.__edad = edad

                                def get_nombre(self):
                                            return self.__nombre

                                                def get_edad(self):
                                                            return self.__edad

                                                                def presentarse(self):
                                                                            return f"Soy {self.__nombre} y tengo {self.__edad} años."


                                                                            class Estudiante(Persona):
                                                                                    def __init__(self, nombre, edad, carrera):
                                                                                                super().__init__(nombre, edad)
                                                                                                        self.__carrera = carrera

                                                                                                            def get_carrera(self):
                                                                                                                        return self.__carrera

                                                                                                                            def presentarse(self):
                                                                                                                                        return f"Soy {self.get_nombre()}, tengo {self.get_edad()} años y estudio {self.__carrera}."


                                                                                                                                        class Profesor(Persona):
                                                                                                                                                def __init__(self, nombre, edad, materia):
                                                                                                                                                            super().__init__(nombre, edad)
                                                                                                                                                                    self.__materia = materia

                                                                                                                                                                        def get_materia(self):
                                                                                                                                                                                    return self.__materia

                                                                                                                                                                                        def presentarse(self):
                                                                                                                                                                                                    return f"Soy {self.get_nombre()}, tengo {self.get_edad()} años y enseño {self.__materia}."


                                                                                                                                                                                                    estudiante = Estudiante("Rodrigo", 20, "Informática")
                                                                                                                                                                                                    profesor = Profesor("Carlos", 35, "Programación")

                                                                                                                                                                                                    print("=== EJERCICIO 1: PERSONAS ===")
                                                                                                                                                                                                    print(estudiante.presentarse())
                                                                                                                                                                                                    print(profesor.presentarse())