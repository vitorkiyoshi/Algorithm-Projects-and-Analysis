#include "shortest_path.hpp"
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n,Q;
    cin >> n >> Q;
    //criar vetor de n*(q+1) + 1, por incluir 0 e vertice inicial
    int nV = n*(Q+1) + 1; //vertice s=0
    Grafo graf(nV); //grafo
    vector<int> V(nV,0);//vetor de verificacao
    vector<vector<int>> moedas(n);//moedas
    int v,p,q;
    for(int i=0; i<n; i++){
        cin >> v >> p >> q; //valor, peso, quantidade
        vector<int> A={v,p,q};
        moedas[i] = A;
    }
    vector<int> pilhaV;
    pilhaV.push_back(0); //vertice 0
    vector<int> pilhaMoedas;
    pilhaMoedas.push_back(0); //indice 0 moeda
    int og;
    int iMoeda;
    int destino;
    int limite;
    while(!pilhaV.empty()){ 
        og = pilhaV.back(); //vertice origem
        iMoeda = pilhaMoedas.back(); //fazer divisão por q+1 para indice q, consigo indices normais
        v = moedas[iMoeda][0];
        p = moedas[iMoeda][1];
        q = moedas[iMoeda][2];
        //retirar elemento da pilha
        pilhaV.pop_back();
        pilhaMoedas.pop_back();
        limite = (Q+1)*(iMoeda+1); //exemplo destino de moeda 0, nn ultrapassa 7, moeda 1 nn pode ultrapassar 14
        for(int i=0; i<=q;i++){//iterando qtdes diferentes da moeda
            /* (1+ 5*1)+1
             * */
            if(iMoeda==0) destino = i*v + (og + (Q+1)*iMoeda) + 1;
            else destino = i*v + (og + (Q+1));//1,7(0,6) 8,14(0,6) d-1, (0,6) (7,13) %7
            if(destino<=limite && destino<nV){//aresta possivel
                graf.adicionaArco(og,destino,p*i);
                if(V[destino]==0 && iMoeda<n-1){ //se o vertice destino ainda nn foi visto suas arestas, e ainda tiver outro tipo de moeda
                    pilhaV.push_back(destino);
                    pilhaMoedas.push_back(iMoeda+1);
                }
            }
            else{
                //tirar elemento da pilha e fazer proxima iteração do while
                break;
            }
        }
        V[og]=1; //vertice que as arestas já foram feitas
    }
    int *dist = graf.caminhoMinimo(0,nV-1);
    if (dist[nV-1]!=INT_MAX){
        cout << dist[nV-1] << endl;
    }
    else{
        int a=nV-1;
        while (dist[a]==INT_MAX){
            a-=1;
            Q-=1;
        }
        cout << Q << " " << dist[a] << endl;
    }
    return 0;
}
