#include <iostream>
#include <iomanip>
using namespace std;
int main() {
    //ingreso de variables
    string nombre;
    char inicial;
    int nmagico;
    double estatura;
    long nhermanos;
    int añon;
    string lfavorito;
    string cfavorito;
    char simbolo;
    const double año=2024;
    float edad;
    float suerte;
    const long nunico=1401226426;
    //codigo
    system("cls");
    cout<<"Ingrese el nombre: \n";
    getline(cin, nombre);
    cout<<"Ingrese inicial del apellido:";
    cin>>inicial;
    cout<<"Ingrese un numero magico:";
    cin>>nmagico;
    cout<<"Ingrese su estatura:";
    cin>>estatura;
    cout<<"Ingrese su lugar favorito";
    getline(cin, lfavorito);
    cout<<"ingrese numero de hermanos";
    cin>>nhermanos;
    cout<<"Ingrese año de nacimiento";
    cin>>añon;
    cout<<"Ingrese su lugar favorito:";
    getline(cin,cfavorito);
    cout<<"Ingrese un simbolo que lo represente:";
    cin>>simbolo;
    //DNI
    cout<<setfill('=') << setw(60) <<"=" << endl;

    cout<<"Nombre:"<<nombre<<endl;
    cout<<"Inicial del apellido:"<<inicial<<endl;
    edad= año-añon;
    cout<<"Edad:"<<edad<<endl;
    suerte=nmagico*edad;
    cout<<"Numero de la suerte:"<<suerte<<endl;
    cout<<"Numero unico"<<nunico<<endl;
    cout<<"Lugar favorito"<<lfavorito<<endl;
    cout<<"Hermanos/as"<<nhermanos<<endl;
    cout<<"Color favortio"<<cfavorito<<endl;
    cout<<"Simbolo representativo"<<simbolo<<endl;

    cout<<setfill('=') << setw(60) <<"=" << endl;
    return 0;
}
