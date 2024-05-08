//tipos de datos en js
var nombre = 'Florencia';//tipo string
console.log(typeof nombre);
//tipo number
var numero = 3000;
console.log(numero);
//tipo object
var objeto = {
  nombre: 'Florencia',
  apellido: 'Lizardo',
  telefono: '12344567'
}

console.log(objeto);

// tipos de datos: boolean
var bandera = true;
console.log(bandera);

// tipos de datos: funciones(nos per ite reutilizar lineas de codigo)

function miFuncion(){
}

console.log(typeof miFuncion);

//tipo de dato symbol
var simbolo = Symbol('Mi simbolo');
console.log(typeof simbolo);

//tipos de datos: clases (una clase es una funcion)
class Persona {
  constructor(nombre, apellido){
    this.nombre = nombre;
    this.apellido = apellido;
  }
}

console.log(Persona);

//tipos de datos: undefined (cuando no esta inicializada)
 var x;
 console.log(x);

 //null: ausencia de valor. no es un tipo de dato como tal, sino que es considerado de tipo object
 var y = null;
console.log(typeof y);

//tipo de dato: array(es de tipo object) y empty
var autos = ['Citroen', 'Audi', 'Fiat'];
console.log(autos);
console.log(typeof autos);

var z = '';//empty
console.log(z);
console.log(typeof z);


