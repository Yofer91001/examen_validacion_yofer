#include <iostream>

using namespace std;

//Prototipo de la función Fibonacci
void fibonacci(int);

int main(){
  int n;
  cout << "Ingrese n: ";
  cin >> n;
  
  //Ejecutar la función
  fibonacci(n);

  //Prueba con 8
  fibonacci(8);


  return 0;
}

void fibonacci(int n){
  
  if(n>0){
    //Inicializar F1 (más tarde tomará el rol de Fi-2)
    int n1 = 0;
    cout<<n1<<"\t";
    if(n > 1){
      //Inicializar F2 (más tarde tomará el rol de Fi-1)
      int n2 = 1;
      cout<<n2<<"\t";
      if(n > 2){
        //Inicializar variable que almacenará Fi =(Fi-1 + Fi-2)
        int n3;
        for(int i = 0; i < (n-2); i++){
          //Fi =(Fi-1 + Fi-2)
          n3 = n2 + n1;
          //Cambiando el valor de Fi-2 al de la siguiente posición
          n1 = n2 ;
          //Cambiando el valor de Fi-1 al de la siguiente posición
          n2 = n3;
          //Imprimiendo Fi
          cout<<n3<<"\t";
        }

      }
    }
  }
  cout<<endl;
}
