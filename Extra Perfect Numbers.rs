// Definition
// An extra perfect number is a positive integer whose first and last bits in binary representation are set (i.e., both are 1).
// Task
// Given a positive integer N, return all the extra perfect numbers in the range from 1 to N, inclusive.

fn extra_perfect(n: u32) -> Vec<u32> {
    let mut a = Vec::new();
    for i in 1..n+1{
        if i%2 != 0{
            a.push(i);
        }
    }
    return a
}
