#include <stdio.h>
#include <stdbool.h>

float calc_tax(float income, float low_bound, float up_bound, float rate){
    // If the income is higher than the lower bound, then the income is eligible for taxation at this rate
    // Otherwise, we return 0, because nothing can be taxed on this income
    if (income> low_bound){
        float taxable;
        // If the income is higher than the upper bound, then all of the income can be taxed
        if(income>up_bound){
            // So logically, the part of the income that is possible to tax equals up_bound - low_bound
            taxable = up_bound-low_bound;
        }
        else{
            // If it's not the case, then the taxable amount is income - low_bound
            taxable = income - low_bound;
        } 
        // And we return the taxable income for this level, multiplied by the tax rate of the given level
        return taxable * rate;
    }
    else{
        //If nothing can be taxed, then it returns 0, which means that no money can be taxed in this level
        return 0;
    }
}

float tax(float income){
    float tax = 0;
    float rates[] = {0.0, 0.11,0.30,0.41,0.45};
    float low_bounds[] = {0, 10226, 26071, 74546, 160336};
    float up_bounds[] = {10225,26070,74545,160336, income};

    for(int i=0; i<=5; i++){
        tax+= calc_tax(income, low_bounds[i], up_bounds[i], rates[i]);
    }
    return tax;
}

int main () {
    float income;
    printf("Quel est votre salaire annuel ? ");
    scanf("%f", &income);
    printf("Vous payez %.2f euros d'impôts.\n", tax(30000));
    return 0;
}