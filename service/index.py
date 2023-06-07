## EN EL SERVICE DEBEMOS CREAR UN ARCHIVO POR CADA MODELO O NECESIDAD.
## SE ENCARGA DE RECIBIR DATA DEL CONTROLLER PARA PODER ESCRIBIRLA EN LA DB
## O SE ENCARGA DE OBTENER LA DATA DE LA DB

class Factura {
  static generar(mesaID, meseroID, totalAPagar){
    postgresql.post(mesa)
  }

  static getFactura(id){
    postgresql.where('id', '==', id).get()
  }
}