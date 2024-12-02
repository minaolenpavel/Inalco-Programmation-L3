#include <stdio.h>
#include <stdbool.h>
#include "../funcs.c"

float calc_rest(float up_bound, float sum){
    float rest = sum - up_bound;
    return rest;

}

float tax_calc(float wage, float tax_lvl){
    return wage * tax_lvl;
}

void tax_manager(float wage){
    float final_tax = 0;
    float rest = calc_rest(10225, wage);
    if(is_positive(rest) == true){
        final_tax += tax_calc(rest, 0.11);
        rest = calc_rest(26070, rest);
        printf("tax amount = %f\nreste = %f", final_tax, rest);
        if(is_positive(rest)==true){    
            final_tax += tax_calc(rest, 0.30);
            rest = calc_rest(74545, rest);
            printf("tax amount = %f\nreste = %f", final_tax, rest);
        }
    }
}

int main () {
    tax_manager(30000);
    return 0;
}