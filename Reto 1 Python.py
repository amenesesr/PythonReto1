acuprod = int(0)
total = int(0)
parcial = int(0)
cod2 = int(0)
prod = ['PANTALON DE HOMBRE     ','CAMISA MANGA CORTA     ','CAMISETA POLO          ','CAMISETA CUELLO REDONDO','MEDIAS TOBILLERAS      ','OTRO PRODUCTO          ']
valores = [45000,35000,27000,12000,3000]
lprod = 'N/A'
valprod = int(0)
conttr = int (0)


#proyecto Matrices
fproducto = []
fcantidad = []
fvaloruni = []
ftotal = []
fcodigo= []
contador = int(0)
contador2 = int(0)
#fin proyecto Matrices

def subtotal(cant, valprod):
    tot_parcial = int(cant * valprod)
    return tot_parcial

print('   ░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓██████████████████▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒░░░░░░░░░')
print('   ▒                                                                      ▒')
print('   ▓  ░░▒▒▓▓██  BIENVENIDO AL SISTEMA DE FACTURACION EL BOSQUE  ██▓▓▒▒░░  ▓')
print('   █                                                                      █')
print('   ▓                              ░░▒▒▓▓██   Powered By MINTIC  ██▓▓▒▒░░  ▓')
print('   ▒                                                                      ▒')
print('   ░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓██████████████████▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒░░░░░░░░░')
print('')
nombre=input(print('Bienvenido al sistema de facturacion, por favor digite su nombre:'))
print('')
print('')
while True:
    conttr = conttr + 1
    print('   ░░░░░░▒▒▒▒▒▒▓▓▓▓▓▓████████████▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░')
    print('   ▒                   ░▒▓█▓▒░                    ▒')
    print('   ▓       ░▒▓█   P R O D U C T O S    █▓▒░       ▓')
    print('   ▒                   ░▒▓█▓▒░                    ▒')
    print('   ░░░░░░▒▒▒▒▒▒▓▓▓▓▓████████████▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░░')
    print('   ▒                                              ▒')
    print('   ▒    ☺ PANTALON DE HOMBRE     CODIGO   123     ▒')
    print('   ▓    ☻ CAMISA MANGA CORTA     CODIGO   345     ▓')
    print('   █    ☺ CAMISETA POLO          CODIG0   456     █')
    print('   ▓    ☻ PRODUCTOS SIN CODIGO   CODIGO   0       ▓')
    print('   ▒                                              ▒')
    print('   ░░░░░░▒▒▒▒▒▒▓▓▓▓▓████████████▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░░')
    print('')
    cod = int(input(print(nombre,'por favor digite el codigo del producto: ')))
    print('')
    if cod==123:
        valprod = valores[0]
        cant = int(input(print(nombre,'por favor digite la cantidad de ',prod[0],' : ')))
        parcial = int(subtotal(cant, valprod))
        acuprod = acuprod + cant
        lprod = prod[0]
        #matriz
        fproducto.append(lprod)
        fcantidad.append(cant)
        ftotal.append(parcial)
        fvaloruni.append(valprod)
        fcodigo.append(cod)
        contador = contador + 1
        #fin matriz
    elif cod==345:
        valprod = valores[1]
        cant = int(input(print(nombre,'por favor digite la cantidad de ',prod[1],' : ')))
        parcial = int(subtotal(cant, valprod))
        acuprod = acuprod + cant
        lprod = prod[1]
        #matriz
        fproducto.append(lprod)
        fcantidad.append(cant)
        ftotal.append(parcial)
        fvaloruni.append(valprod)
        fcodigo.append(cod)
        contador = contador + 1
        #fin matriz
    elif cod==456:
        valprod = valores[2]
        cant = int(input(print(nombre,'por favor digite la cantidad de ',prod[2],' : ')))
        parcial = int(subtotal(cant, valprod))
        acuprod = acuprod + cant
        lprod = prod[2]
        #matriz
        fproducto.append(lprod)
        fcantidad.append(cant)
        ftotal.append(parcial)
        fvaloruni.append(valprod)
        fcodigo.append(cod)
        contador = contador + 1
        #fin matriz
    elif cod==0:
        print('')
        print('   ░░░░░░▒▒▒▒▒▒▓▓▓▓▓▓████████████▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░')
        print('   ▒                    ░▒▓█▓▒░                   ▒')
        print('   █     P R O D U C T O S  S I N  C O D I G O    █')
        print('   ▒                    ░▒▓█▓▒░                   ▒')
        print('   ░░░░░░▒▒▒▒▒▒▓▓▓▓▓▓████████████▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░')
        print('   ▒                                              ▒')
        print('   ▓      ☺  CAMISETA CUELLO REDONDO    [ 1 ]     ▓')
        print('   █      ☻  MEDIAS TOBILLERAS          [ 2 ]     █')
        print('   ▓      ☺  OTRO PRODUCTO              [ 3 ]     ▓')
        print('   ▒                                              ▒')
        print('   ░░░░░░▒▒▒▒▒▒▓▓▓▓▓▓████████████▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░')
        print('')
        cod2=int(input(print(nombre,'por favor digite el codigo: ')))
        print('')
        if cod2==1:
            valprod = valores[3]
            cant = int(input(print(nombre,'por favor digite la cantidad de ',prod[3],' : ')))
            parcial = int(subtotal(cant, valprod))
            acuprod = acuprod + cant
            lprod = prod[3]
            #matriz
            fproducto.append(lprod)
            fcantidad.append(cant)
            ftotal.append(parcial)
            fvaloruni.append(valprod)
            fcodigo.append("N/A")
            contador = contador + 1
            #fin matriz
        elif cod2==2:
            valprod = valores[4]
            cant = int(input(print(nombre,'por favor digite la cantidad de ',prod[4],' : ')))
            parcial = int(subtotal(cant, valprod))
            acuprod = acuprod + cant
            lprod = prod[4]
            #matriz
            fproducto.append(lprod)
            fcantidad.append(cant)
            ftotal.append(parcial)
            fvaloruni.append(valprod)
            fcodigo.append("N/A")
            contador = contador + 1
            #fin matriz
        elif cod2==3:
            cant = int(input(print(nombre,'por favor digite la cantidad de ',prod[5],' : ')))
            print('')
            valprod = int(input(print(nombre,'por favor digite el valor del producto: ')))
            parcial = int(subtotal(cant, valprod))
            acuprod = acuprod + cant
            lprod = prod[5]
            #matriz
            fproducto.append(lprod)
            fcantidad.append(cant)
            ftotal.append(parcial)
            fvaloruni.append(valprod)
            fcodigo.append("N/A")
            contador = contador + 1
            #fin matriz
        else:
            print('   ░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓████████████████▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░')
            print('   ░                                                             ░')
            print('   ▒               ░░▒▒▓▓██   E R R O R !  ██▓▓▒▒░░              ▒')
            print('   ▓                                                              ')
            print('   █           L A   E N T R A D A  "', cod2,'"  N O   E S        ')
            print('   █                                                              ')
            print('   ▓          V A L I D A   P A R A    E L    S I S T E M A       ')
            print('   ▒                                                             ▒')
            print('   ░                                                             ░')
            print('   ░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓████████████████▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░')
            print('')
            print('Lo siento',nombre,'el valor ',cod2,'no es reconocido por el sistema')
            conttr = conttr - 1
            cant = 0
            valprod = 0
            parcial = 0
            lprod = 0
    else:
        print('   ░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓████████████████▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░')
        print('   ░                                                             ░')
        print('   ▒               ░░▒▒▓▓██   E R R O R !  ██▓▓▒▒░░              ▒')
        print('   ▓                                                              ')
        print('   █            E L    C O D I G O  ', cod,'  N O   E S           ')
        print('   █                                                              ')
        print('   ▓         V A L I D O   P A R A    E L    S I S T E M A        ')
        print('   ▒                                                             ▒')
        print('   ░                                                             ░')
        print('   ░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓████████████████▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░')
        print('')
        print('Lo siento',nombre,'el valor ',cod,'no es reconocido por el sistema')
        conttr = conttr - 1
        cant = 0
        valprod = 0
        parcial = 0
        lprod = 0
    total = total + parcial
    print('')
    print('   ╔══════════════════╦═════════════════════════════════════════════════════════════════════')
    print('   ║                  ║                                                                     ')
    print('   ║     ░▒▓█▓▒░      ║  El producto comprado es                :   ', lprod                 )
    print('   ║ S U B T O T A L  ║  La cantidad de productos parciales es  :   ', cant                  )
    print('   ║     ░▒▓█▓▒░      ║  El valor unitario del producto         : $ ', valprod               )
    print('   ║                  ║  El Valor de los productos parciales es : $ ', parcial               )
    print('   ║                  ║                                                                     ')
    print('   ╠══════════════════╬═════════════════════════════════════════════════════════════════════')
    print('   ║                  ║                                                                     ')
    print('   ║     ░▒▓█▓▒░      ║  La cantidad total de productos es      :   ', acuprod               )
    print('   ║    T O T A L     ║  El valor de la venta total es          : $ ', total                 )
    print('   ║     ░▒▓█▓▒░      ║  El numero total de transacciones es    :   ',conttr                 )
    print('   ║                  ║                                                                     ')
    print('   ╚══════════════════╩═════════════════════════════════════════════════════════════════════')
    print('')
    print('')
    factura = int(input(print(nombre,'su producto a sido registrado ¿Desea registrar otro producto? 1 = SI - 2 = NO')))
    if factura == 2 :
        break
    print('')
    print('') #EN TEORIA LO ANTERIOR SOLO LO VE LA PERSONA QUE EJECUTA EL APLICATIVO, LO QUE VIENE
              #DE AQUI EN ADELANTE ES LA FACTURA QUE SE LE ENTREGARIA AL CLIENTE
print('') #Matrices Presentacion
print('               G R A C I A S  P O R  S U  C O M P R A ♥                  ')
print('')
print('══════════════════════════════════════════════════════════════════════════════════════════')
print('CODIGO     PRODUCTO                        VALOR UNITARIO    CANTIDAD    TOTAL')
print('══════════════════════════════════════════════════════════════════════════════════════════')
for contador2 in range (contador):
    print(fcodigo[contador2],'      ',fproducto[contador2],'      $',fvaloruni[contador2],'            ',fcantidad[contador2],'        $',ftotal[contador2])
print('──────────────────────────────────────────────────────────────────────────────────────────')
print('                                                       TOTAL ',acuprod,'        $',total)
print('══════════════════════════════════════════════════════════════════════════════════════════')
#Fin Matrices Presentacion
print('')
print('                                                                         ')
print('   ╔══════════════╦═══════════════════════════════════════════════════════')
print('   ║              ║                                                       ')
print('   ║  T O T A L   ║   La cantidad total de productos es :  ', acuprod      )
print('   ║   ░▒▓█▓▒░    ║   El valor total de la compra es    : $', total        )
print('   ║              ║                                                       ')
print('   ╚══════════════╩═══════════════════════════════════════════════════════')
print('                                                                          ')
print('                                                                          ')
print('Usted fue atendido por atendido por',nombre)
print('                                                                         ')
print('                                                                         ')
print('                                                                         ')
print(' Hecho por Alejandro Meneses Roldan ♠                                    ')
print(' Proyecto MINTIC 2022 UNIVERSIDAD EL BOSQUE                              ')
