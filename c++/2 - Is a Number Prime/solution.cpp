// Is a Number Prime?
// Level: 6 kyu

/**
* Define a function that takes an integer argument and returns a logical value true 
* or false depending on if the integer is a prime.
*
* Per Wikipedia, a prime number ( or a prime ) is a natural number greater than 1 
* that has no positive divisors other than 1 and itself.
*
* - You can assume you will be given an integer input.
* - You can not assume that the integer will be only positive. 
*   You may be given negative numbers as well ( or 0 ).
* Note: 
*     There are no fancy optimizations required, but still the most trivial solutions 
*     might time out. Numbers go up to 2^31 ( or similar, depending on language ). Looping all 
*     the way up to n, or n/2, will be too slow.
*
* Example:
*   is_prime(1)  // false 
*   is_prime(2)  // true  
*   is_prime(-1) // false 
*/

#include <iostream>
#include <cmath>

// Code
bool isPrime(int num) {
    if (num < 2) return false;
    
    if (num % 2 == 0 && num != 2) return false;

    for (int i = 3; i <= sqrt(num); i += 2) {
        if (num % i == 0) return false;
    } 

    return true;
}

// Tests
int main () {
    int test = 29;

    bool solution = isPrime(test);

    if (solution) {
        std::cout << "\nThe number (" << test << ") is prime";
    } else {
        std::cout << "\nThe number (" << test << ") is NOT prime";
    }
    
    bool spected = solution == true;
    
    if (spected) {
        std:: cout << "\nPassed: TRUE";
    } else {
        std:: cout << "\nPassed: FALSE";
    }

    return 0;
}