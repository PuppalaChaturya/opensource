#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int n, arr[1000];
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    char *s[1000];
    for(int i=0;i<n;i++){
        if(arr[i]<30){
            s[i]="NO";
        }
        else{
            s[i]="YES";
        }
    }
    for(int i=0;i<n;i++){
        printf("%s\n",s[i]);}
    return 0;
}
