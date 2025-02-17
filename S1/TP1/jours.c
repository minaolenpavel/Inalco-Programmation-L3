#include <stdio.h>

int main (void) {
    printf("Entrez un nombre de jours : ");
    int days;
    scanf("%d", &days);
    int year = days/365;
    int week = year %7;
    int rem_days = days%7;
    printf("%d jours correspondent à : %d années, %d semaines et %d jours !", days,year, week, rem_days);
    return 0;
}