#include<stdio.h>

int main(void){
    int num = 0;
    int sig_dig = 0;
    int dig1 = 0;
    int dig2 = 0;
    int dig3 = 0;
    int dig4 = 0;
    int q4, q3, q2 = 0;


    printf("Enter number to convert to base 2: ");
    scanf("%lf", &num);

    printf("\n");

    printf("The four digits of that number are as follows: ");
    scanf("%lf", &sig_dig);

    printf("\n");

    //make calculations for each digit
    dig4 = num % 2;
    q4 = num/2;

    dig3 = q4 % 2;

    q3 = q4/2;
    
    dig2 = q3 % 2;

    q2 = q3/2;
    
    dig1 = q2 % 2;

    printf("Most significant digit: ");
    printf("%d\n", dig4);

    printf("\n");

    printf("Next digit: ");
    printf("%d\n", dig3);

    printf("\n");

    printf("Next digit: ");
    printf("%d\n", dig2);

    printf("\n");

    printf("Least significant digit: ");
    printf("%d\n", dig1);
}