function longestNiceSubstring(s) {
    if (s.length < 2) return "";

    const set = new Set(s);
    for (let i = 0; i < s.length; i++) {
        if (set.has(s[i].toLowerCase()) && set.has(s[i].toUpperCase())) {
            continue;
        }
        const left = longestNiceSubstring(s.slice(0, i));
        const right = longestNiceSubstring(s.slice(i + 1));
        return left.length >= right.length ? left : right;
    }
    return s;
}

// Example usage
console.log(longestNiceSubstring("YazaAay"));  // Output: "aAa"
console.log(longestNiceSubstring("Bb"));       // Output: "Bb"
console.log(longestNiceSubstring("c"));        // Output: ""
