var num1 = 10
var num2 = 15

function detect(){
    return 'Você passou no teste!'
}
function maior(x1,x2){
    if (num1 > num2) {
        return 'O primeiro valor é maior!'
    }
    if (num1 < num2) {
        return 'O segundo valor é maior!'
    }
    if (num1 == num2) {
        return 'Os valores são iguais!'
    }
}

const teste = (status)=> 'O status referente ao seu teste foi: ' + status


resultado = teste('Aprovado')
console.log(resultado)
resultado = maior(num1,num2)
console.log(resultado)
resultado = detect()
console.log(resultado)
