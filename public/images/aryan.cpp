#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;
int main(){
    int t;
    cin>>t;
    vector<int> ans;
    for(int i=1;i<=t;i++){
        int k;
        cin>>k;
        ans.push_back(k);
    }
    unordered_map<int,int> m;
    for(int j=0;j<ans.size();j++){
        if(m.find(ans[j])==m.end()){
            m[ans[j]]=1;
        }else{
            m[ans[j]]++;
        }
    }
    if(ans.size()==1 || ans.size()==2){
        cout<<"yes"<<endl;
    }else{
        if(ans.size()%2==0){
            if(m.size()>2){
                cout<<"no"<<endl;
            }else{
                if(m.size()==1){
                    cout<<"yes"<<endl;
                }else{
                    if(m[ans.size()-1]!=m.size()/2){
                        cout<<"no"<<endl;
                    }else{
                        cout<<"yes"<<endl;
                    }
                }
            }
        }else{
            if(m.size()>2){
                cout<<"no"<<endl;
            }else{
                if(m.size()==1){
                    cout<<"yes"<<endl;
                }else{
                    if(m[ans.size()-1]==m.size()/2 || m[ans.size()-1]==m.size()/2+1){
                        cout<<"yes"<<endl;
                    }else{
                        cout<<"no"<<endl;
                    }
                }
            }
        }
    }
    return 0;
}