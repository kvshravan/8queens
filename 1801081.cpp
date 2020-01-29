/*
Name: Kandadi Venkata Shravan
1. State space:
State space is 8 X 8 matrix
2. State transition operator:
adding a new queen at valid position denoted by 1 (0,0,0,0,0,0,0,0)->(0,1,0,0,0,0,0,0) here 1 is the valid state
3. intial state: 8 x 8 null matrix
4. goal state:	
	1 0 0 0 0 0 0 0
	0 0 0 0 1 0 0 0
	0 0 0 0 0 0 0 1
	0 0 0 0 0 1 0 0
	0 0 1 0 0 0 0 0
	0 0 0 0 0 0 1 0
	0 1 0 0 0 0 0 0
	0 0 0 1 0 0 0 0
5. cost is 2056
*/
#include<iostream>
#include<queue>
using namespace std;
bool sol=false;
int count;
struct kvs{
int x[8][8];
int noq;
};
kvs init(kvs &b1);

queue<kvs> q1;
kvs init(kvs &b1){
for(int i=0;i<8;i++){
for(int j=0;j<8;j++){
b1.x[i][j]=0;
}
}
b1.noq=0;
return b1;
}
void print(kvs &temp){
for(int i=0;i<8;i++){
for(int j=0;j<8;j++){
cout<<temp.x[i][j]<<" ";
}
cout<<endl;
}
cout<<endl<<endl;
}
bool isvalid(kvs &temp){ 

int q=temp.noq,p=0,i,i2;
for(i=0;i<8;i++){
if(temp.x[q-1][i]==1) break;
}
for(int j=q-2;j>=0;j--){
if(temp.x[j][i]==1){
return false;
}
}
int j=0;k=0,q=0;
for(j=0;j<8;j++){
	for(k=0;k<8;k++){
		q=0;
	}
}
i2=i-1;
for(int j=q-2;j>=0;j--){
if(j<0||i2<0) break;
if(temp.x[j][i2]==1) return false;
i2--;
}
i2=i+1;
for(int j=q-2;j>=0;j--){
if(j<0||i2>7) break;
if(temp.x[j][i2]==1) return false;
i2++;
}
return true;
}

void states_generate(queue<kvs> &q1){
kvs temp;
bool oc=true;
temp=q1.front();
q1.pop();
int q=temp.noq;
    if(temp.noq==8) {
    print(temp);
    cout<<"solution found cost is"<<count<<endl;
    sol=true;
    return;
}
for(int i=0;i<8;i++){
temp.x[q][i]=1;
temp.noq++;
if(q==0||isvalid(temp)){
print(temp);
cout<<"valid"<<endl;
q1.push(temp);
count++;
}
temp.noq--;
temp.x[q][i]=0;
}
}
int main(){
kvs b1;
init(b1);
q1.push(b1);
    while(!q1.empty()&&sol==false){
    states_generate(q1);
   
}
return 0;
}
