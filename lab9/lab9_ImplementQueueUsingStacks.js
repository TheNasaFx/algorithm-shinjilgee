class MyQueue {
    constructor() {
        this.inStack = [];
        this.outStack = [];
    }

    push(x) {
        this.inStack.push(x);
    }

    pop() {
        this._move();
        return this.outStack.pop();
    }

    peek() {
        this._move();
        return this.outStack[this.outStack.length - 1];
    }

    empty() {
        return this.inStack.length === 0 && this.outStack.length === 0;
    }

    _move() {
        if (this.outStack.length === 0) {
            while (this.inStack.length > 0) {
                this.outStack.push(this.inStack.pop());
            }
        }
    }
}

// Example usage:
const myQueue = new MyQueue();
myQueue.push(1);        // queue is: [1]
myQueue.push(2);        // queue is: [1, 2]
console.log(myQueue.peek());   // return 1
console.log(myQueue.pop());    // return 1, queue is [2]
console.log(myQueue.empty());  // return false
