#include <stdio.h>

int main(){

// 년도 입력 받기
int a;
scanf("%d", &a);

if (a%4 == 0 && a%100 != 0){
    printf("1");
}
else if (a%400 == 0){
    printf("1");
}
else{
    printf("0");
}
}