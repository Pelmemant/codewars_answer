// Write function heron which calculates the area of a triangle with sides a, b, and c.

fn heron(a: u32, b: u32, c: u32) -> f64 {
    let s = (a + b + c) as f64 / 2.0;
    let sa = s - a as f64;
    let sb = s - b as f64;
    let sc = s - c as f64;
    (s * sa * sb * sc).sqrt()
}
