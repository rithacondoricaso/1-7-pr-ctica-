class Vehiculo:
        def __init__(self, marca, modelo, velocidad):
                self.__marca = marca
                        self.__modelo = modelo
                                self.__velocidad = velocidad

                                    def get_marca(self):
                                            return self.__marca

                                                def get_modelo(self):
                                                        return self.__modelo

                                                            def get_velocidad(self):
                                                                    return self.__velocidad

                                                                        def acelerar(self, cantidad):
                                                                                self.__velocidad += cantidad

                                                                                    def frenar(self, cantidad):
                                                                                            self.__velocidad = max(0, self.__velocidad - cantidad)

                                                                                                def mostrar(self):
                                                                                                        return f"{self.__marca} {self.__modelo} - Velocidad: {self.__velocidad} km/h"


                                                                                                        class Auto(Vehiculo):
                                                                                                            def __init__(self, marca, modelo, velocidad, puertas):
                                                                                                                    super().__init__(marca, modelo, velocidad)
                                                                                                                            self.__puertas = puertas

                                                                                                                                def mostrar(self):
                                                                                                                                        return f"{super().mostrar()} - Puertas: {self.__puertas}"


                                                                                                                                        class Motocicleta(Vehiculo):
                                                                                                                                            def __init__(self, marca, modelo, velocidad, cilindrada):
                                                                                                                                                    super().__init__(marca, modelo, velocidad)
                                                                                                                                                            self.__cilindrada = cilindrada

                                                                                                                                                                def mostrar(self):
                                                                                                                                                                        return f"{super().mostrar()} - Cilindrada: {self.__cilindrada} cc"


                                                                                                                                                                        auto = Auto("Toyota", "Corolla", 60, 4)
                                                                                                                                                                        moto = Motocicleta("Honda", "CB190R", 50, 184)

                                                                                                                                                                        auto.acelerar(20)
                                                                                                                                                                        moto.frenar(10)

                                                                                                                                                                        print("=== EJERCICIO 2: VEHICULOS ===")
                                                                                                                                                                        print(auto.mostrar())
                                                                                                                                                                        print(moto.mostrar())