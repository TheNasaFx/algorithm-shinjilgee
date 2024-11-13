const chai = require('chai');
const expect = chai.expect;
const Fibonacci = require('C:\Users\nasan\algo shinjilge\fibonacci.js'); 

describe('Fibonacci', function() {
    let fibonacci;

    beforeEach(function() {
        fibonacci = new Fibonacci();
    });

    it('should return 0 for F(0)', function() {
        expect(fibonacci.fib(0)).to.equal(0);
    });

    it('should return 1 for F(1)', function() {
        expect(fibonacci.fib(1)).to.equal(1);
    });

    it('should return 1 for F(2)', function() {
        expect(fibonacci.fib(2)).to.equal(1);
    });

    it('should return 2 for F(3)', function() {
        expect(fibonacci.fib(3)).to.equal(2);
    });

    it('should return 3 for F(4)', function() {
        expect(fibonacci.fib(4)).to.equal(3);
    });

    it('should return 5 for F(5)', function() {
        expect(fibonacci.fib(5)).to.equal(5);
    });

    it('should return 55 for F(10)', function() {
        expect(fibonacci.fib(10)).to.equal(55);
    });

    it('should return 6765 for F(20)', function() {
        expect(fibonacci.fib(20)).to.equal(6765);
    });

    it('should return 832040 for F(30)', function() {
        expect(fibonacci.fib(30)).to.equal(832040);
    });
});
