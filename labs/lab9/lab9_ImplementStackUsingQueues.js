class MyStack {
    constructor() {
        this.queue1 = [];
        this.queue2 = [];
    }

    push(x) {
        this.queue1.push(x);
    }

    pop() {
        while (this.queue1.length > 1) {
            this.queue2.push(this.queue1.shift());
        }
        const res = this.queue1.shift();
        const temp = this.queue1;
        this.queue1 = this.queue2;
        this.queue2 = temp;
        return res;
    }

    top() {
        while (this.queue1.length > 1) {
            this.queue2.push(this.queue1.shift());
        }
        const res = this.queue1.shift();
        this.queue2.push(res);
        const temp = this.queue1;
        this.queue1 = this.queue2;
        this.queue2 = temp;
        return res;
    }

    empty() {
        return this.queue1.length === 0;
    }
}

// Example usage:
const myStack = new MyStack();
myStack.push(1);
myStack.push(2);
console.log(myStack.top());    // return 2
console.log(myStack.pop());    // return 2
console.log(myStack.empty());  // return false
