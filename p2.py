import sys

def test(did_pass):
    """ Print the result of a test. """
    linenum = str(sys._getframe(1).f_lineno)
    
    if did_pass:
        msg = "Test at line " + linenum + " ok."
    else:
        msg = "Test at line " + linenum + " FAILED."

    print(msg)


def rev_pair(word, array):
    #Invertir la palabra recibida como argumento
    invertido = word[::-1]
    
    #Iterar sobre los elementos del arreglo recibido
    for p in array:
        #Comparar si un elemento del array es igual a la versión invertida de la palabra
        if(str(p) == invertido):
            return True
    
    return False


def test_suite():
    test(rev_pair("los", ("casa", "lsiengp", "sol", "petidngua")))
    test(not rev_pair("kayak", ("par", "inverso", "no", "existe")))


#Ejecución del test
test_suite()