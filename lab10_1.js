function negjiinOrtog(n) {
    let ortog = 0;
    for (let i = 1; i <= n; i++) {
        if ((i & (i - 1)) == 0) {
            ortog += i;
        } else {
            ortog += 1;
        }
    }
    let dundajUne = ortog / n;
    return dundajUne;
}

let n = 10;
let dundajUne = negjiinOrtog(n);
console.log(`Daraalliin uildliin negjiin ortog n=${n}: ${dundajUne}`);
